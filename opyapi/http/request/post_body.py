from .body import RequestBody


class PostBody(RequestBody):
    pass


class Field:
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content

    def __int__(self):
        return int(self.content)

    def __str__(self):
        return str(self.content)

    def __float__(self):
        return float(self.content)

    def __bool__(self):
        return bool(self.content)

    def __len__(self):
        return len(self.content)
