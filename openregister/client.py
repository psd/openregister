import logging
import requests
from cachecontrol import CacheControl
from cachecontrol.caches.file_cache import FileCache
from io import BytesIO
from zipfile import ZipFile
from .item import Item


class RegisterClient(object):

    """
    Access register items from an openregister server.
    """

    def __init__(self, config={}, cache=None):
        self.config = config
        if cache is None:
            cache = FileCache(".cache", forever=True)
        self.session = CacheControl(requests.Session(), cache=cache)

    def get(self, url, params=None):
        response = self.session.get(url, params=params)
        logging.info("GET: %s [%s]" % (response.url, response.status_code))
        return response

    def load(
        self,
        store,
        name,
        domain=".register.gov.uk",
        protocol="https",
        path="download-register",
    ):
        url = "{protocol}://{name}{domain}/{path}".format(
            protocol=protocol, name=name, domain=domain, path=path
        )

        response = self.get(url)

        zipfile = ZipFile(BytesIO(response.content))

        for info in zipfile.infolist():
            if info.filename.startswith("item/"):
                item = Item()
                item.json = zipfile.open(info.filename).read().decode("utf-8")
                store.put(item)
