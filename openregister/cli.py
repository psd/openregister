import logging
import click
from click_default_group import DefaultGroup
import hupper
from .stores.memory import MemoryStore
from .client import RegisterClient
from .server import RegisterServer


@click.group(cls=DefaultGroup, default="serve", default_if_no_args=True)
@click.version_option()
def cli():
    """
    OpenRegister:  publishing tools for GOV.UK style registers.
    """


@cli.command()
@click.option(
    "-h", "--host", default="127.0.0.1", help="host for server, defaults to 127.0.0.1"
)
@click.option("-p", "--port", default=8088, help="port for server, defaults to 8088")
@click.option("-d", "--debug", is_flag=True, help="More verbose logging")
@click.option("--reload", is_flag=True, help="Reload if a file change is detected")
def serve(host, port, debug, reload):

    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if reload:
        hupper.start_reloader("openregister.cli.cli")

    store = MemoryStore()
    client = RegisterClient()
    client.load(store, name="register")

    server = RegisterServer(config=None, store=store)

    click.echo("Serving on port {}".format(port))

    server.server().run(host=host, port=port, debug=debug)
