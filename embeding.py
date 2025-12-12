from dataclasses import dataclass
import chromadb
import gradio as gr
import hashlib
import sys 
import os

@dataclass
class File_t:
    name: str
    path: str
    content: str

l_file_t: list[File_t]= []
collection = chromadb.Client().create_collection(name="documentos")

def read_file(files): 
    added=""
    for file in files:
        with open(file, encoding="utf-8", buffering=1) as fd:
            name = os.path.basename(fd.name)
            path = fd.name
            content = fd.read()
            l_file_t.append(File_t(name, path, content))

            added = added + "- " + name + "\n"

    return added

def embed():
    documents, metadatas, ids = [], [], []
    for file in l_file_t:
        documents.append(file.content)
        metadatas.append({"name" : file.name})
        ids.append(hashlib.sha256(file.name.encode("utf-8")).hexdigest())

    collection.add(documents = documents, metadatas = metadatas, ids = ids)  

def consultar(query):
    results = collection.query(query_texts=[query], n_results=1)

    return str(results["documents"][0][0])

def main():
    types=[".md", ".txt", ".json"]

    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column(scale=2):
                file_loader = gr.Files(file_types=types, label=f"Selecciona un archivo {" ".join(types)}")
                upload_button = gr.Button("Cargar archivos", variant="primary")
            with gr.Column(scale=2):
                added_files = gr.Markdown()

        with gr.Row():
            with gr.Column(scale=4):
                insert_button = gr.Button("Insertar archivos", variant="primary")

        with gr.Row():
            with gr.Column(scale=4):
                consulta = gr.Textbox(label="Consulta", placeholder="Escribe tu consulta…", lines=2)
                respuesta = gr.Markdown(label="Respuesta")

        upload_button.click(fn=read_file, inputs=file_loader, outputs=added_files)
        insert_button.click(fn=embed) 
        consulta.submit(fn=consultar, inputs=consulta, outputs=respuesta)
    demo.launch()
    
    return 0

if __name__ == '__main__': 
    raise SystemExit(main())
