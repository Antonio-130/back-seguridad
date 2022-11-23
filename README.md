## Principales Tecnologias utilizadas

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [FastApi-mail](https://sabuhish.github.io/fastapi-mail/)
- [SqlAlchemy](https://www.sqlalchemy.org/)
- [Bycrypt](https://pypi.org/project/bcrypt/)
- [PyJWT](https://pypi.org/project/PyJWT/)
- [Uvicorn](https://www.uvicorn.org/)

## Requrimientos

Python 3.6+ [https://www.python.org/downloads/](https://www.python.org/downloads/)
## Instalación

```bash
pip install -r requirements.txt
```
post-data: Es recomendable crear un entorno virtual para instalar las dependencias.
Puedes usar venv: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html), virtualenv: [https://virtualenv.pypa.io/en/latest/](https://virtualenv.pypa.io/en/latest/), o conda: [https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).


## Ejecucución

```bash
uvicorn app:app
```
Para actualizar los cambios en el código sin tener que reiniciar el servidor, puedes usar la flag `--reload`:
```bash
uvicorn app:app --reload
```

El servidor se ejecutará en [http://localhost:8000](http://localhost:8000)

## Documentación

La documentación de la API se encuentra en la ruta `/docs` de la API.

La misma se genera automáticamente con [FastAPI](https://fastapi.tiangolo.com/) a travez de la librería [Swagger](https://swagger.io/).
