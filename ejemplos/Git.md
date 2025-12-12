---
aliases:
  - git
---
Hay 147 comandos en Git, según Prime, existen 37 importantes para un
desarrollador, el resto vuelven las cosas muy complicadas. Se pueden estudiar todas
en [[man]]. En Git existe comandos de alto nivel y de bajo nivel, de "porcelana
("porcelain") y de "plomo"("plumbing").

Una de los encantos de git es que es un sistema de control de versiones
*distribuido*,  frente a los tradicionales que eran completamente locales. Así
la versión en tu equipo es tuya  y no tiene por qué representar el estado de un
repositorio remoto, hasta que decidas sincronizar.

- Repo: un proyecto controlado por git. Cara repositorio es un árbol, "main working tree".
- [[git commit]]: un punto en el tiempo que representa el estado de todo el proyecto. *Esto suele ser confuso para quienes ya lo usan sin conocer cómo funciona por dentro*, pero efectivamente, un commit no es un simple registro de cambios.
- Index: El indice es la zona que se denomina "stage", la zona donde se preparan los cambios para el próximo commit.
- Squash: convertir varios commits en uno solo. 

Git es un grafo acíclico, lo que quiere decir que cada commit es un nodo y  cada
puntero es un puntero de padre a hijo, a nivel teórico esto significa que de un
vértice  *v* no hay un camino directo que empiece y termine en *v*. Tiende a
verse lineal, cómo una lista enlazada, pero no debe olvidarse uno de que es la
constante del tiempo lo que empuja a la grafo a tender a ser lineal, pero sigue
siendo un grafo acíclico: un árbol.

### Referencias
[Everything You'll Need to Know About Git - ThePrime](https://frontendmasters.com/courses/everything-git/)
