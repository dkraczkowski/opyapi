def wrapper(cls, *args, **kwargs):
    print(cls.__dict__)


_ANNOTATIONS = "__opyapi_annotations__"


class Application:
    def __init__(self, title: str, servers: list = [], version: str = "1.0.0"):

        self.title = title
        self.servers = servers
        self.version = version

    def __call__(self, target):
        print("call")
        print(target)
        if not hasattr(target, _ANNOTATIONS):
            setattr(target, _ANNOTATIONS, {})

        target.__dict__[_ANNOTATIONS]["application"] = self
        print(target.__dict__)

        return target


class Server:
    def __init__(self, url, description: str = "", variables: list = []):
        print("init")

    def __call__(self, *args, **kwargs):
        print("call")
        return wrapper


class Schema:
    def __init__(self, title: str, schema_type: str = None, schema_format: str = None):
        print("init")

    def __call__(self, *args, **kwargs):
        print("call")
        return wrapper


class Property:
    def __init__(self, name: str = None, type: str = None):
        print("init")

    def __call__(self, *args, **kwargs):
        print("call")
        return wrapper
