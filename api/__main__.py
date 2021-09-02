import uvicorn

from api import settings
from api.app import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        '__main__:app',
        host=settings.api.HOST,
        port=settings.api.PORT,
        debug=settings.api.DEBUG,
        reload=settings.api.RELOAD,
    )
