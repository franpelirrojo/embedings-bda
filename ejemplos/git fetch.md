Con fetch obtenemos toda la información del repositorio remoto. Pero no
actualizará las ramas del repositorio, las guardará en el sistema de git, dentro
de `.git/origin/`.

```shell
git fetch
remote: Enumerando objetos: 30, listo.
remote: Contando objetos: 100% (30/30), listo.
remote: Comprimiendo objetos: 100% (19/19), listo.
remote: Total 30 (delta 5), reusados 0 (delta 0), pack-reusados 0
Desempaquetando objetos: 100% (30/30), 2.25 KiB | 575.00 KiB/s, listo.
Desde ../myrepo
 * [nueva rama]      bar               -> origin/bar
 * [nueva rama]      foo               -> origin/foo
 * [nueva rama]      foo-rebase-master -> origin/foo-rebase-master
 * [nueva rama]      master            -> origin/master
 * [nueva rama]      trunk-merge-foo   -> origin/trunk-merge-foo
```

Pero nuestro repositorio, nuestra rama master, sigue divergiendo de la rama
remota. Si hacemos un [[git log]] veremos un mensaje desconcertante: no hay
ningún commit.

```
git log
fatal: tu rama actual 'master' no tiene ningún commit todavía
```

Sin embargo sí que tenemos los cambios. Lo que ocurre es que *únicamente* hemos
obtenido los cambios, pero no hemos "mergeado" los cambios. Podemos comprobar
que tenemos el historial, accediendo directamente a la rama de `origin`.

```shell
git log origin/master --graph --oneline
* 5e05d4b (origin/master) baz
* 9bede59 (origin/bar) Y
* 90ae10e X
* 8a28121 E
* d83d11c D
* 4c7afeb A
```

```
git branch -a
  remotes/origin/bar
  remotes/origin/foo
  remotes/origin/foo-rebase-master
  remotes/origin/master
  remotes/origin/trunk-merge-foo
```

Destacar que **origin/master** es el nombre completo de la rama, no una carpeta
(que también, es las dos cosas). Ramas cuya estructura es `<remote>/<name>`
representan el último estado conocido del repositorio remoto, que puede
desactualizarse en cualquier momento, pero no es un problema, es la gracia de
git.

Siguiendo la lógica de git, es fácil deducir cómo conseguir los cambios que
queremos, el código. En nuestra rama principal, hacemos un [[git merge|merge]] (un merge directo).

```shell
git merge origin/master 
git log --oneline --graph
* 5e05d4b (HEAD -> master, origin/master) baz
* 9bede59 (origin/bar) Y
* 90ae10e X
* 8a28121 E
* d83d11c D
* 4c7afeb A
```