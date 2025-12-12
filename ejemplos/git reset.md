
Reset es una herramienta muy poderosa para deshacer commits o rehacerlos sin errores, pero muy peligrosa, ya que podemos comprometer el historial de [[Git]].

Un **soft** reset, desanda tu rama tu rama contigo, olvidando tu commit, y ese commit que has olvidado se convertirá un cambio en el working-tree y el indice.  Muy útil para editar un commit que ya está terminado, es decir, *deshace un commit*.

```shell
git reset --soft HEAD~1
```

> [!warning] Cuidado con el historial
> Al hacer commit de los cambios, podemos destrizar el historia. `commit --amend`aplicará los cambios retrospectivamente al commit original.

Un **hard** reset hace lo mismo pero destruyendo los cambios traqueados no hechos commit. Se des hace del indice y el working-tree.
