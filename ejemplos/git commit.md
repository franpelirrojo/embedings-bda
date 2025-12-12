---
aliases:
  - commit
---
Es el comando central de [[Git|git]], con él añadimos los cambios en el estado del repositorio al árbol de git. Es habitual y una buena práctica usar `git status` antes de lanzar un commit para vitar cagarla. La forma normal del comando es: `git commit -m 'mensaje'`. El resultado será el siguiente:

```shell
git commit -m 'segundo commit'

[master b8afb00] segundo commit
 2 files changed, 1 insertion(+)
 rename test.txt => first.md (100%)
 create mode 100644 second.md
```

El commit te da los primeros siete caracteres del sha generado: `b8afb00`. Con estos ya se puede buscar el commit usando [[git log#git cat-file|cat-file]].
