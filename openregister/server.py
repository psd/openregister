from sanic import Sanic
import urllib.parse
from .views import DataView, ItemView, favicon
from .config import DEFAULT_CONFIG


class RegisterServer:
    def __init__(self, config=None, store=None):
        self._config = dict(DEFAULT_CONFIG, **(config or {}))
        self.store = store

    def absolute_url(self, request, path):
        url = urllib.parse.urljoin(request.url, path)
        if url.startswith("http://") and self.config("force_https"):
            url = "https://" + url[len("http://") :]
        return url

    def config_view(self):
        return DataView.as_view(self, "config", lambda: self._config)

    def item_view(self, name):
        return ItemView.as_view(self, name, lambda key: self.store.item(key))

    def server(self):
        server = Sanic(__name__)

        server.add_route(favicon, "/favicon.ico")
        server.add_route(self.config_view(), r"/config<suffix:(\.json)?$>")
        server.add_route(
            self.item_view("item"), r"/item/<key:[a-z0-9]+><suffix:(\.json)?$>"
        )

        return server
