import json
from sanic import response
from sanic.views import HTTPMethodView


async def favicon(request):
    return response.text("")


class DataView(HTTPMethodView):
    name = "data"

    def __init__(self, server, filename, callback):
        self.server = server
        self.filename = filename
        self.callback = callback

    async def get(self, request, suffix):
        data = self.callback()
        if suffix == ".json":
            headers = {}
            content_type = "application/json"
            representation = json
            return response.HTTPResponse(
                representation.dumps(data), content_type=content_type, headers=headers
            )


class ItemView(HTTPMethodView):
    def __init__(self, server, name, callback):
        self.server = server
        self.name = name
        self.callback = callback

    async def get(self, request, key, suffix):
        print('key:', key)
        print('suffix:', suffix)
        item = self.callback(key)
        if suffix == ".json":
            headers = {}
            content_type = "application/json"
            data = item.json
            return response.HTTPResponse(data, content_type=content_type, headers=headers)
