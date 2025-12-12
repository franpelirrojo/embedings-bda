Junto a la capacidad de autoregeneración de los [[git commit|commits]], las ramas son la segunda característica más poderosa, y a veces compleja de [[Git|git]].

Trabajando colaborativamente no debes trabajar sobre `main`, aunque cuando uno trabaja sólo y conoce bien git suele trabajar sobre `main`. Las ramas tienen un coste cero a tanto en computación cómo en espacio, esto es gracias al sistema de [[git log|hashes]] sobre el que se construye git. A la hora de la verdad una rama es simplemente un archivo más dentro de `.git`, en concreto un sha más en `refs/heads/`, en consecuencia: un subárbol, u n puntero hacia un commit.

Para crear una nueva rama usamos `git branch <name>`, este comando creará una rama en el commit en el que te encuentras, la rama apunta a este commit, pero _no cambiará de rama_.

```shell
commit 4c7afeb2969c1361288ebdac9fd47407ca7899f3 (HEAD -> master, foo)
Author: franpelirrojo <franfc.00@gmail.com>
Date:   Tue Apr 22 11:04:31 2025 +0200

    A
```

Para cambiar de rama podemos usar `git checkout <name>` o `git switch <name>`. Si hacemos commit tras cambiar de rama, estos no están en la principal. Apreciamos abajo que foo está adelantado a master.

```shell
* commit ad3846c0916ab0732b108738b3c0bb54742146ff (HEAD -> foo)
| Author: franpelirrojo <franfc.00@gmail.com>
| Date:   Tue Apr 22 11:12:15 2025 +0200
|
|     C
|
* commit 6779aaa22fd4123a1803d8f533d7950bfe027bdf
| Author: franpelirrojo <franfc.00@gmail.com>
| Date:   Tue Apr 22 11:11:50 2025 +0200
|
|     B
|
* commit 4c7afeb2969c1361288ebdac9fd47407ca7899f3 (master)
  Author: franpelirrojo <franfc.00@gmail.com>
  Date:   Tue Apr 22 11:04:31 2025 +0200

      A
```

Si continuamos editando la rama master, tendremos dos _ramas divergentes_, siendo dos ramas con un mismo ancestro que tienen commits únicos.

```shell
git log --oneline foo
ad3846c (foo) C
6779aaa B
4c7afeb A

git log --oneline master
8a28121 (HEAD -> master) E
d83d11c D
4c7afeb A
```

Las dos forma principales de unificar ramas, de integrar los cambios de una en otra, son:  [[git merge]] y [[git rebase]].

### HEAD
Cada vez que hacemos `checkout` HEAD apunta a la rama hacia la que lo hacemos. Es un puntero al commit actual. Tan simple cómo que es una referencia más en `.git`.

```shell
cat .git/HEAD
ref: refs/heads/foo
cat .git/refs/heads/foo
ad3846c0916ab0732b108738b3c0bb54742146ff <-- ¡Maravilla, un commit!
```

El comando `git relog` nos muestra las diferentes posicones de la cabeza, en definitiva, un log de todo lo que se ha hecho. Parece mágico, pero es simplemente un log en un fichero. Sabiendo esto, es fácil [[recuperacion en git|recuperar]] información perdida.

### Referencias
[Everything You'll Need to Know About Git - ThePrime (https://frontendmasters.com/courses/everything-git/)