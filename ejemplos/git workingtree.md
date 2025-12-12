[[git stash]] es incómodo y te hace infeliz. Los arboles de trabajo son la alternativa, cuando hablamos de workingtree, nos referimos a `linked working tree`. Cuando creamos un proyecto con [[git init]] creamos el `workingtree principal`, un `workingtree`no es más que una rama  del árbol principal. Es una rama con su propio estado y `.git`se transforma en un fichero, un fichero que contiene una referencia al directorio `.git`principal.

- Para crear una rama, `git worktree add <path>` crea una rama en el directorio, hace checkout de esta y hace `basename`para dar bautizarla.
- Para listar los arboles usamos `git worktree list`.
- Para eliminar el árbol, `git worktree remove <path>`, o eliminar la carpeta y después usar `git worktree prune`.

Al ser el árbol un simple puntero, al no necesitar reproducir otro historial de git, la creación es instantánea, prácticamente gratis. El mayor inconveniente es si uno tiene un coste de levantar un proyecto de muchos minutos, esto puede ser un problema d tiempo. *La idea es que el cambio de rama es un antipatrón, la buena práctica es trabajar con diferentes directorios con su árbol y se eliminan conforme se va terminando el trabajo.*