`git stash` coge todos los cambios de los que [[Git|git]] hace seguimiento (el
indice y cambios al work tree) y los guarda en una zona especial, los aísla.
Para conceptualizarlo mejor debemos entenderlo cómo un **stack** de cambios.

> [!quote] man stash
> Use git stash when you want to record the current state of the working directory and the index, but want to go back to a clean working directory. The command saves your local modifications away and reverts the working directory to match the HEAD commit.

Para hacer push al stack usamos  `git stash -m "my lovely message here"`, el
mensaje es opcional, pero ayuda. Podemos hacer `git stash pop` tanto para sacar
el último stash o indices concretos.

Stash es muy útil para ocasiones en las que teneos que importar cambios mientras estamos trabajando en nuestra rama y evitar [[conflictos en git|confictos]].
1. Hacemos stash de nuestros cambios (sin commitear)
2. Hacemos el pull al remoto
3. Sacamos nuestro trabajo del stash.