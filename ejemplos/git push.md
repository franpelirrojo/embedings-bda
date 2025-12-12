Lo contrario de [[git pull]], `git push`. Análogo ha hacer un fetch y un merge, pero desde otro lado.
#### Empujando en local. Se terminó la magia.
Trabajando con [[git remote|repositorios remotos]] en local es normal recibir un error del repositorio remoto al empujar. Esto puede resultar increíble al estar acostumbrados al uso de Github, que hace merge automáticamente.

```shell
git push origin master
Enumerando objetos: 15, listo.
Contando objetos: 100% (14/14), listo.
Compresión delta usando hasta 12 hilos
Comprimiendo objetos: 100% (7/7), listo.
Escribiendo objetos: 100% (9/9), 1.03 KiB | 1.03 MiB/s, listo.
Total 9 (delta 2), reusados 0 (delta 0), pack-reusados 0
remote: error: refusing to update checked out branch: refs/heads/master
remote: error: Por defecto, actualizar la rama actual en un repositorio no vacío
remote: está denegado, porque eso haría el índice y el árbol de trabajo inconsistentes
remote: con lo que ya se ha empujado, y requeriría 'git reset --hard' para arreglar
remote: el árbol de trabajo con HEAD.

[...]

To ../myrepo/
 ! [remote rejected] master -> master (branch is currently checked out)
error: falló el empuje de algunas referencias a '../myrepo/'
```

Lo que está ocurriendo es que estamos tratando de hacer [[git merge|merge]]
sobre una rama que está en uso, la rama sobre la que se está trabajando (!),
haciendo peligrar la integridad del árbol de trabajo. Lo que debemos hacer, y es
lo que hace Github automáticamente, es hacer checkout sobre otra rama, empujar
los cambios y después mergearlos con la principal.

```shell
/myrepo$ git checkout bar
Cambiado a rama 'bar'

/remote-git$ git push origin master
Enumerando objetos: 15, listo.
Contando objetos: 100% (14/14), listo.
Compresión delta usando hasta 12 hilos
Comprimiendo objetos: 100% (7/7), listo.
Escribiendo objetos: 100% (9/9), 1.03 KiB | 1.03 MiB/s, listo.
Total 9 (delta 2), reusados 0 (delta 0), pack-reusados 0
To ../myrepo/
	8d0547d..14f0f81  master -> master
```