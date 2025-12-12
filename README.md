# Embeddings con chromadb en docker

### Entorno de ejecución
La aplicación está dockerizada.

```bash
docker build -t gradio-chroma:v3 .
docker run --rm -p 7860:7860 gradio-chroma:v3
```

Ahora puedes abrir [http://localhost:7860/](http://localhost:7860/)

> [!INFO]
> En el repositorio, en el la carpeta ejemplos hay una serie de documentos sobre
> git que puedes usar de ejemplo. Son markdown, la aplicación unicamente acepta:
> txt, json y markdown.
