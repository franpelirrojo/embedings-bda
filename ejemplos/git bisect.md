Bisect es una herramienta para encontrar fallos o cambios lógicos a lo largo del historial de commits. Los [[git commit|commits]] están ordenados por tiempo, por lo que podemos considerarlos un array ordenado, bisect ejecuta una búsqueda binaria hasta encontrar el commit "sano". Bisect puede funcionar gracias a nuestras indicaciones manuales o usando un comando. El flujo de trabajo es el siguiente:
1. Iniciamos con `git bisect start`.
2. Seleccionas un commit donde el comportamiento es erróneo mediante `git bisect bad` para usar el actual, y otro donde sepamos que es correcto con `git bisect goood <commit>`.
3. Continuar marcando commits con hasta que encontremos el punto en el tiempo que buscamos.

> [!tip]
> Bisect es muy poderoso, pero puede ser lento.

Pero no todo es tan tedioso, podemos proporcionar un script de test a bisect para que funcione automáticamente en un shell.

```shell
git bisect run <cmd>
```
