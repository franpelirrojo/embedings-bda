Pull es una forma más conveniente de mantener sincronizarse con el [[git remote|repositorio remoto]] que [[git fetch]], pull altera el estado del repositorio al traerse los cambios. Aun así fetch es una operación útil para realizar habitualmente.

```shell
git pull <remote> <branch>
```

Un error común es el no especificar el repositorio remoto y la rama la primera vez que se  usa pull, es molesto, pero de facto, git no tiene por qué asociar dos ramas que se llamen igual, una remota otra local; y es bueno. 

Prime advierte de que por defecto pull realiza un merge, pero que el prefiere usar [[git rebase]]. `git pull --rebase` 
1. Permite tener una rama más limpia sin commits de merge.
2. Tener tus cambios en las hojas del árbol permite un trabajo más cómodo y testear los cambios contra el estado correcto de master.
3. Es fácil unificar todos los commits en uno solo antes de hacer [[git push]]
4. Planificar para el fallo, no para el exito.
### Referencias
[Everything You'll Need to Know About Git - ThePrime](https://frontendmasters.com/courses/everything-git/)