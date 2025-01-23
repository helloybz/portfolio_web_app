import click
from src.api.web.command import web_cmd


@click.group()
def cmd(): ...


cmd.add_command(web_cmd)

if __name__ == "__main__":
    cmd()
