En el flujo de trabajo con un equipo, normalmente te pedirán que hagas "squash" a tus commits antes de mergear con la rama principal, con esto de lo que hablamos es de "interacting [[git rebase]] squashing"; en definitiva convertir todos tus cambios en un único y limpio commit sobre el que hacer un [[git merge#Estrategias de merge|merge directo]]. Aunque un rebase interactivo se puede usar para una gran cantidad de tareas, cómo eliminar un commit o cambiar el historial, pero principalmente para lo que nos interesa: aplastar commits.

Para iniciar un rebase interactivo necesitamos darle un lugar en el tiempo en el que hacer el rebase. Lo más directo es mover el HEAD. El comando require un elemento equivalente a un commit, un `HEAD~n` representa un commit n anterior a HEAD.

```shell
git rebase -i <commitish>
git rebase -i HEAD~3
```

Durante el proceso interactivo git pedirá información sobre qué tiene que hacer. La parte más importante es en la que especificamos que commits permanecen y cuales son aplastados contra los existentes. En este caso 2 y 3 son machacados en 1.

```shell
pick 76937aa 1
s 224de95 2
s ae98cc2 3
```

```shell
* f2e993a (HEAD -> master) 1 através de 3
* 6684f6e A + 10
* 34ace5e (origin/master) E+9
*   a3466fc merge ours E + 8
|\
| * d587e85 A + 7
```