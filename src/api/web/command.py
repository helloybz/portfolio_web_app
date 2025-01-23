import click
import uvicorn

from src.api.web.app import create_web_app


@click.group("web")
def web_cmd(): ...


@web_cmd.command("run")
def run():
    app = create_web_app()
    config = uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
    uvicorn.Server(config).run()
