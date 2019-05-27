#!/usr/bin/env python
# clone the country register

from io import BytesIO
from zipfile import ZipFile
import requests
from cachecontrol import CacheControl
from cachecontrol.caches.file_cache import FileCache
from openregister import Item
from openregister.stores.memory import MemoryStore

cache = CacheControl(requests.Session(), cache=FileCache(".cache", forever=True))


def load_register(
    store, name, domain="register.gov.uk", protocol="https", path="download-register"
):
    url = "{protocol}://{name}.{domain}/{path}".format(
        protocol=protocol, name=name, domain=domain, path=path
    )

    response = cache.get(url)

    zipfile = ZipFile(BytesIO(response.content))

    for info in zipfile.infolist():
        if info.filename.startswith("item/"):
            item = Item()
            item.json = zipfile.open(info.filename).read().decode("utf-8")
            store.put(item)


store = MemoryStore()

load_register(store, name="register")
registers = [store.item(item).get("register") for item in store.items]

for register in registers:
    print("loading .. ", register)
    if register is not None:
        load_register(store, name=register)

# for item in store.items:
# print(item, store.item(item).json)

print(len(store.items))
