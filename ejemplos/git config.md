`config` es el comando más simple de [[Git|git]] y el primero que se debe usar en una instalación fresca, ya que es vital **que git conozca el usuario y correo**, para poder marcar cada commit a la persona.

La configuración de git tiene dos alcances: global y local, esta última es únicamente para el repositorio en concreto. 
- Todas las claves de la configuración se asocian a un valor. Es importante recordar que la estructura de la clave es: `<sección>.<clave>`. *Olvidar el punto genera errores muy extraños.*
- Para añadir un valor `git config --add --global <key> <value>`
- Para conocer un valor `git config --get <key>`

La configuración de git es conocida por tener ciertas aristas desconcertantes, incluso arcanas. *A pesar de esto, hay que recordar que lo único que hacemos es escribir en un archivo que se encuentra en `.git`*. Veamos un proceso de configuración:

1. Añadimos una clave y un valor nuevo. `git config --add fem.dev "es genial"` ¡Exacto podemos añadir nuestros propios valores!
2. Listamos los valores para comprobar que existe.

```shell
git config --list
rerere.enabled=true
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
fem.dev=es genial
```
3. Si añadimos otro valor con la misma clave, se añadirá sin problemas. Efectivamente git tiene esta cosa de poder repetir claves, y podemos listarlas mediante  `git config --get-all fem.dev`, ya que si usamos `git config --get fem.dev` devolverá el último valor asignado.
4. La última cosa extraña de git respecto a esto es que si usamos `git config --unset` recibiremos un error ya que hay múltiples valores, debemos usar `git config --unset-all` es obligatorio eliminar todas las instancias de la clave.

A pesar de lo dicho, **existen decenas de opciones y comandos**, esto es lo básico y algunos elementos relevantes, para un buen uso y un buen carácter cómo programador, lo mejor es acudir siempre a [[man]].