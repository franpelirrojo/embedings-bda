Los repositorios remotos es la forma que tenemos en [[Git|git]] para acceder al
código de terceros, por algo git es un sistema de control de versiones
**distribuido**. `remote`es simplemente *una copia del repo en otro lugar*, lo
que implica, que no tiene porqué ser remoto no ser en Github, los archivos
pueden estar en el ordenador de otras personas.

```
git remote add <name-remote> <URI>
```

- Una buena práctica es denominar al `origin`. Trabajando con un fork, el repositorio autorizado se suele denominar `upstream`, para no confundirlo en local.
- URI puede ser una dirección web, un ssh o un path en el ordenador.

Un ejemplo de creación de un repositorio y añadir un repositorio remoto en el mismo ordenador:

```
git remote add origin ../myrepo/
git remote -v
origin  ../myrepo/ (fetch)
origin  ../myrepo/ (push)
```

Este proceso *únicamente* denomina al repositorio remoto, ahora debemos traernos los cambios, esto se puede hacer mediante: [[git fetch]] o [[git pull]]. Si tratamos de usar log, veremos que no cambios.

```
git log
fatal: tu rama actual 'master' no tiene ningún commit todavía
```