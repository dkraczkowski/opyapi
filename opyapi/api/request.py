class Request:
    def __init__(self, schema, description: str = "", headers: list = None):
        self.headers = headers
        self.description = description
        self.schema = schema
