Rebase es un herramienta muy poderosa pero también polémica, cómo suele ocurrir
en tecnología, principalmente por el uso generalizado de una herramienta sin
comprender realmente que está ocurriendo. Su nombre es ciertamente algo
descriptivo: rebasa. Lo que nos va a ayudar es a pasar del estado primero al
estado segundo, de unificar ramas:

```
   B --- C                foo
 /
A --- D --- E --- X --- Y master

                           B --- C                foo
                         /
A --- D --- E --- X --- Y                         master
```

**Rebase permite aplicar todos los cambios de una rama en otra.** En este caso
lo que hace rebase es actualizar el puntero de foo para que apunte a la cabeza
de master, y así pode realizar un merge directo, simplificando el grafo. Lo que
permite esta herramienta es cambiar el tiempo, *adaptar los cambios a la realidad
del proyecto.* 

El ciclo básico que realiza rebase es el siguiente:
1. Ejecutamos el `git rebase <target>`.
2. Viaja al ancestro común.
3. Recorre la rama guardando todos los diff en archivos temporales.
4. Hace `checkout` en la rama objetivo hacia la que estamos haciendo rebase, *la que estamos sobre pasando*.
5. Aplica cada cambio en orden.

> [!tip] Es importante orientarse: la dirección
> Cara comprender la "dirección" del rebase, es interesante entender que estamos sobrepasando *hacia* otra rama. La rama objetivo es hacia donde queremos mover la rama en la que estamos.

```
git checkout -b foo-rebase-master

git rebase master
Rebase aplicado satisfactoriamente y actualizado refs/heads/foo-rebase-master.

git log --oneline --graph
* 94e2944 (HEAD -> foo-rebase-master) C
* 0ce9d35 B
* 9bede59 (master, bar) Y
* 90ae10e X
* 8a28121 E
* d83d11c D
* 4c7afeb A
```

Ahora no tenemos una rama que diverge, sino una rama lineal que empuja el historial hacia delante. Esto que acabamos de hacer es *alterar la historia*, precisamente porque al resolver los diff en el proceso, crea nuevos [[git commit|commit]], cuyo sha está determinado por el tiempo. Por un lado ofrece un historial más limpio para trabajar, sin embargo genera problemas, cómo que en una instancia remota, *hay una rama con el mismo nombre pero con un historial diferente*, esto es lo que solucionamos con el famoso, recurrente y terrible `git push --force`.

> [!warning] En producción
> A nivel de higiene de git, par evitar esto, **rebasa en ramas privadas, unifica
en ramas públicas**.

### Referencias
1. [Everything You'll Need to Know About Git - ThePrime](https://frontendmasters.com/courses/everything-git/)
2. Pro Git - Scott Chancon & Ben Straub