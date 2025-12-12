En [[Git]] hay dos formas de dar marcha atrás: revert y [[git reset|reset]]. La principal diferencia es que restore devuelve un archivo a un commit anterior, revert crea un nuevo commit con los cambios inversos al commit anterior.

```shell
git revert <commitsh>
```

Revert requiere de un elemento comparable a un commit, cómo por ejemplo usar un sha de un commit. Rever creará un proceso de construcción de un nuevo commit *que puede tener conflictos con el estado actual* que deben ser resueltos. El estado de revert exige resolve conflictos, añadirlos a la rama y continuar con el revert, cómo un [[conflictos en git|rebase o un merge]].

> [!tip]
> Lo fantástico de revert es que permite dar marcha atrás sin comprometer el estado de ramas remotas u otros repositorios al alterar el historial borrando un commit.
