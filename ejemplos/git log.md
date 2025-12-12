Comando de [[Git|git]] que muestra el historial del repositorio desde el commit padre. Es importante conocer el comando y estar cómodo con su uso para trabajar de una manera adecuada. Algunos argumentos útiles son:

- `--graph` muestra junto al log un esquema gráfico de las ramas del árbol. 
- `--oneline`mostrará una versión reducida, los punteros de rama, los primero siete dígitos del sha y el mensaje de commit.
- `--decorated` a la hora de guardar un log en un fichero es importante este argumento para que se escriba toda la información en forma de texto. Forzar a git a mostrarlo todo por el stdout del comando log.
- `--parents` añade los sha del padre o padres del commit a la representación.
Realmente útil para la legibilidad.

En el log de un [[git commit|commit]] aparecerá siempre un sha(secure hash algorithm), representado por el gran string de hexadecimales.

```shell
* commit 5c833c95e28b3b9c4d6cc9dfe2911f48f5d36cd8 (HEAD -> master)
  Author: franpelirrojo <franfc.00@gmail.com>
  Date:   Mon Apr 21 19:33:50 2025 +0200

      batman
```

```
commit 5c833c95e28b3b9c4d6cc9dfe2911f48f5d36cd8
-------^ Esto es el sha
```

Si tratamos de buscar dentro de `.git` nuestro sha encontraremos que dentro del directorio `/objects` con lo siguiente:

```shell
.git/objects/5c
.git/objects/5c/833c95e28b3b9c4d6cc9dfe2911f48f5d36cd8
```

Cada commit se encuentra dentro de objects y *los primeros dos caracteres de un sha son una carpeta dentro de objects/*. Al intentar leer el archivo recibimos un sinsentido, esto es porque la información ha sido comprimida, al mantener  `.git` el estado del repositorio, esto es fundamental.

### git cat-file

Git contiene herramientas propias para leer el contenido, la más sencilla es `git cat-file`.

```shell
git cat-file -p 5c833c95e28b3b9c4d6cc9dfe2911f48f5d36cd8

tree 1c452cbd820cda95c0f99b36364e3b546811833a
author franpelirrojo <franfc.00@gmail.com> 1745256830 +0200
committer franpelirrojo <franfc.00@gmail.com> 1745256830 +0200

batman
```

Esto no parece gran cosa, pero es en este punto donde se comienza a desplegar y se ve evidente la estructura interna de git: sigamos los hashes. 

```shell
git cat-file -p 1c452cbd820cda95c0f99b36364e3b546811833a
100644 blob 358f6e1f281ccf21fdf564dbb0d61b6887371e66    first.md

git cat-file -p 358f6e1f281ccf21fdf564dbb0d61b6887371e66
hola git <---- aquí está el contenido!!
```

Primero buscando el commit, después mirando en el árbol, luego el fichero y después su contenido hemos podido *reconstruir el estado completo del repositorio.* Para moverse por el historial de git es útil asociar  "tree" a un directorio y "blob" a un fichero. **Git no guarda cambios, guarda el estado completo del código del proyecto.** 

Añadido otro fichero y realizando otro commit, podremos profundizar más en esto. 

```shell
git log --graph
* commit b8afb00e51b7b1db22a86ec3f01a179b63000732 (HEAD -> master)
| Author: franpelirrojo <franfc.00@gmail.com>
| Date:   Mon Apr 21 20:39:00 2025 +0200
|
|     segundo commit
|
* commit 5c833c95e28b3b9c4d6cc9dfe2911f48f5d36cd8
  Author: franpelirrojo <franfc.00@gmail.com>
  Date:   Mon Apr 21 19:33:50 2025 +0200

      batman

git cat-file -p b8afb00e51b7b1db22a86ec3f01a179b63000732
tree 433e9bc3c42de1dd46d5fadefd762f482789f5f8
parent 5c833c95e28b3b9c4d6cc9dfe2911f48f5d36cd8
author franpelirrojo <franfc.00@gmail.com> 1745260740 +0200
committer franpelirrojo <franfc.00@gmail.com> 1745260740 +0200

segundo commit

git cat-file -p 433e9bc3c42de1dd46d5fadefd762f482789f5f8
100644 blob 358f6e1f281ccf21fdf564dbb0d61b6887371e66    first.md
100644 blob 8890e4cdc43b90a29778ea121e22e826c7a8a412    second.md
```

Aquí observamos cosas muy interesantes. Primero, existe un nuevo campo en el commit, el padre de este, el nodo previo del árbol. Segundo, dentro del subárbol del commit a aparecido el archivo que hemos añadido, pero lo relevante es que el sha del primer archivo es el mismo que el del commit anterior (!). **Aunque no hemos alterado el primer archivo, el commit sigue conteniendo un puntero al contenido del archivo**, la consecuencia de esto es que: desde un único commit podemos reconstruir todo nuestro proyecto.
### Buscar
Buscar en los logs es una estrategia muy directa para encontrar errores. Esto es útil sobre todo cuando se conoce el archivo o módulo donde ocurre el error y sobre todo si los mensajes de commit son coherentes. Es más complicado cuando hay muchos commits o si no conseguimos dar con una palabra clave sobre la que buscar.

> [!tip]
> En el lenguaje clásico de computación "buscar" es grep.

```shell
git log --grep "<term>" -p #-p muestra los diff
```

Podemos buscar directamente sobre un único archivo.

```shell
git log -p -- <file1> <file2>
```

Podemos buscar en texto dentro del propio cambio.

```shell
git log -S "<codigo>"
```

Esta es una herramienta que es útil conocer pero que en repositorios complejos puede depender mucho de la suerte. Para un proceso de búsqueda/depuración más complejo usamos [[git bisect]].
### Referencias
[Everything You'll Need to Know About Git - ThePrime](https://frontendmasters.com/courses/everything-git/)
