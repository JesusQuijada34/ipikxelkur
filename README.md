# influent iPikxel Kursor Editor

Fuente preparada para Influent Package Maker.

## Clasificación

iPikxel Kursor Editor se clasifica como **AlphaCube** porque el entrypoint utiliza únicamente Python estándar y no contiene llamadas Linux-only o Windows-only; puede ejecutarse en Linux y Windows con Python 3.8 o posterior. El proyecto actual conserva un entrypoint mínimo (`main`) que devuelve estado correcto, por lo que no se debe presentar como un editor de cursor funcional hasta que se implemente esa interfaz.

El actualizador es portable y ahora limita descargas a 100 MB, rechaza rutas ZIP inseguras y usa argumentos estructurados al cerrar procesos en Linux o Windows. No requiere `sudo` para iniciar el entrypoint.

## Ejemplo de uso
python3 ipikxelkur.py

##