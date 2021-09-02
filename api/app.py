from fastapi import FastAPI

from api import __version__
from api.routes import postfix


def create_app() -> FastAPI:
    app = FastAPI(
        title='TCC',
        description='Resolvendo expressões matemáticas com visão computacional e funções postfix',
        version=__version__
    )

    app.include_router(postfix.router)

    return app
