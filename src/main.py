import click
from src import api
from src.api.web.command import web_cmd
from src.container import Container
from src.settings import Settings


@click.group()
def cmd() -> None: ...


cmd.add_command(web_cmd)

container = Container()
settings = Settings()
container.config.from_pydantic(settings)
container.wire(packages=[api])

if __name__ == "__main__":
    cmd()
