---
aliases:
  - merge
---
Para unificar las dos ramas del ejemplo de [[git branching]], podemos hacer un
`merge`, pero esta operación tiene dos resultados posible.

Un merge intenta combinar dos ramas que divergieron en el pasado, en nuestro caso ambas ramas comparten `A`, este se conoce cómo el primer ancestro en común
o _merge base_. Al unificar git recorre desde la cabeza de ambas ramas, los dos
commits que quires "mergear" y recorre e árbol hasta encontrar el primer commit
en común. Luego crea un nuevo commit en la rama que se está unificando con todos
los cambios en un sólo commit que tiene dos padres. Esto se denomina *3 way merge* ya que realiza la fusión entre los dos últimos commits de cada rama y el ancestro común.

A la hora de hacerlo, usamos `git merge <source branchname>`, siendo la rama en la que te encuentras la rama objetivo y la rama `source`que es la rama la quieres fusionar. Se puede decir que con `git merge` _te traes la rama_ que quieres fusionar. Veamos cómo funciona con el ejemplo anterior.

```shell
git checkout -b trunk-merge-foo
Cambiado a nueva rama 'trunk-merge-foo'

git merge foo
Merge made by the 'ort' strategy.
 second.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 second.md

git log
commit e9f522352f30ec7bb2e35363498c86917c4c665c (HEAD -> trunk-merge-foo)
Merge: 8a28121 ad3846c
Author: franpelirrojo <franfc.00@gmail.com>
Date:   Tue Apr 22 11:41:38 2025 +0200

    Merge branch 'foo' into trunk-merge-foo 

git log --oneline --decorate --graph --parents
*   e9f5223 8a28121 ad3846c (HEAD -> trunk-merge-foo) Merge branch 'foo' into trunk-merge-foo
|\
| * ad3846c 6779aaa (foo) C
| * 6779aaa 4c7afeb B
* | 8a28121 d83d11c (master) E
* | d83d11c 4c7afeb D
|/
* 4c7afeb A
```

Por partes:

1. Primero nos creado un rama nueva por motivos de mantener el ejemplo, pero de
   normal sería en `master`, y entonces nos traemos la orama foo con `git merge
   foo`.
2. En el momento de crear el commit del merge, nos pedirá un mensaje y que
   resolvamos [[conflictos en git|conflictos]] si existen.
3. En el log posterior podemos ver que el commit creado tiene dos sha de dos
   padres. Son los commits de E y de C respectivamente.

#### Estrategias de merge
Más arriba habíamos hablado de que `git merge` podía generar dos resultados, hasta ahora hemos visto el primero, un merge de dos ramas divergentes, que crea un commit de merge con una estrategia conocida cómo "3 way merge" o "ort" (en el mensaje de merge inicial podemos ver que pone esto).

La otra forma de mergear es la directa, que ocurre cuando aunque hay dos ramas, no son divergentes, esto es cuando el __merge base__ es el último commit de la rama target. Mira este ejemplo que hemos añadido al estado de nuestro repo, en master hemos creado una nueva rama llamada bar con dos commits, *el ancestro común de bar es el final de master*.

```shell
* 9bede59 (HEAD -> bar) Y
* 90ae10e X
* 8a28121 (master) E
* d83d11c D
* 4c7afeb A
```
Al realizar el merge, no nos pedirá realizar un commit, git simplemente cambiará
un par de puntero para unificar las lineas. En el mensaje de shell podemos ver
que el tipo de merge es "Fast-forward".

```shell
git checkout master
Cambiado a rama 'master'

git merge bar
Actualizando 8a28121..9bede59
Fast-forward
 bar.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 bar.md

git log --graph --oneline
* 9bede59 (HEAD -> master, bar) Y
* 90ae10e X
* 8a28121 E
* d83d11c D
* 4c7afeb A
```