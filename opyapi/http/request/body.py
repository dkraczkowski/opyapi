class RequestBody:
    _body: dict = {}

    def get(self, name: str, default=None):
        if name in self._body:
            return self._body[name]

        return default

    def __getitem__(self, name):
        return self._body[name]

    def __contains__(self, name):
        return name in self._body
