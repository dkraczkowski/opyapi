# opyapi
Opyapi is a python framework build around [Open API](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#dataTypes) 
specification to provide toolset for rapid REST api development.

### Beauty of opyapi
No bloat. Just code. 



## Quick start

```python
from opyapi import annotations

@annotations.Api(
    title="Example rest application",
    description="This application greets users",
)
class Application:
    pass

@annotations.Operation(
    "/users/{name}",
    method="get"
)
def hello_user(name: str):
    return f"Hello {name}"

```

## Related specs
[Open api specs](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#dataTypes)


[Json schema specs](http://json-schema.org/latest/json-schema-validation.html)
