# opyapi [![Build Status](https://travis-ci.org/dkraczkowski/opyapi.svg?branch=master)](https://travis-ci.org/dkraczkowski/opyapi) [![codecov](https://codecov.io/gh/dkraczkowski/opyapi/branch/master/graph/badge.svg)](https://codecov.io/gh/dkraczkowski/opyapi)
Opyapi is a python framework build around [Open API](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#dataTypes)
specification to provide toolset for rapid REST api development.

## Beauty of opyapi
No bloat. Just code.

### Features
  - Automated documentation generation
  - Routing
  - Mock server
  - Built-in serialization/deserialization mechanisms
  - WSGI compatibility


## Quick start

```python
from opyapi.api import *
from opyapi.http import *

@OpenApi(
    title="Example rest application",
    description="This application greets users",
)
class Application:
    pass


@Operation(
    "/users/{name}",
    method="get",
    responses=TextResponse(200),
    summary="Says hello with username provided in the route"
)
def hello_user(request: HttpRequest):
    return f"Hello {request.route['name']}"

```

## Running application

## Schema

### Boolean `opyapi.schema.types.Boolean`
Represent boolean values.

```python
from opyapi.schema.types import Boolean

is_hungry = Boolean()
```

**Arguments:**
 - `default` assigns default value if none is passed in the request
 - `nullable` accepts nulls, nones as value
 - `description` sets open api description for the field
 - `deprecated` deprecates field in the schema
 - `read_only` sets property to read only mode (POST, PUT, PATCH methods cannot mutate property)
 - `write_only` sets property to write only mode (property is hidden from all GET requests)

### Integer `opyapi.schema.types.Integer`
Represent integer numbers.

```python
from opyapi.schema.types import Integer

age = Integer()
```

**Arguments:**
 - `minimum` sets minimum accepted value
 - `maximum` sets maximum accepted value
 - `multiple_of` accepts value if it is multiplication of a given number
 - `default` assigns default value if none is passed in the request
 - `nullable` accepts nulls, nones as value
 - `description` sets open api description for the field
 - `deprecated` deprecates field in the schema
 - `read_only` sets property to read only mode (POST, PUT, PATCH methods cannot mutate property)
 - `write_only` sets property to write only mode (property is hidden from all GET requests)

### Number `opyapi.schema.types.Number`
Represents any valid number, like:
 - integer
 - rational number
 - float
 - double

```python
from opyapi.schema.types import Number

money = Number()
```

**Arguments:**
 - `minimum` sets minimum accepted value
 - `maximum` sets maximum accepted value
 - `multiple_of` accepts value if it is multiplication of a given number
 - `default` assigns default value if none is passed in the request
 - `nullable` accepts nulls, nones as value
 - `description` sets open api description for the field
 - `deprecated` deprecates field in the schema
 - `read_only` sets property to read only mode (POST, PUT, PATCH methods cannot mutate property)
 - `write_only` sets property to write only mode (property is hidden from all GET requests)

### String `opyapi.schema.types.String`
Represent string values.

```python
from opyapi.schema.types import String

email = String(string_format="email")
```

**Arguments:**
 - `string_format` sets format for the input, for more details check format list
 - `min_length` sets minimum accepted length
 - `max_length` sets maximum accepted length
 - `pattern` sets regex pattern that value must match, when pattern set format should be omitted
 - `default` assigns default value if none is passed in the request
 - `nullable` accepts nulls, nones as value
 - `description` sets open api description for the field
 - `deprecated` deprecates field in the schema
 - `read_only` sets property to read only mode (POST, PUT, PATCH methods cannot mutate property)
 - `write_only` sets property to write only mode (property is hidden from all GET requests)

#### Available formats

##### `datetime`
Makes string type to accept only ISO8601 valid date time format.

##### `date`
Makes string type to accept only ISO8601 valid date format.

##### `time`
Makes string type to accept only ISO8601 valid time format.

##### `email`
Makes string type to accept only valid email address.

 | Please note: that this format can be mean to some special cases of email addresses.

##### `hostname`
Makes string type to accept only valid email hostname.

##### `uri`
Makes string type to accept only valid uri.

##### `url`
Makes string type to accept only valid url, must starts with valid scheme (http/https/ftp).

##### `uuid`
Makes string type to accept only valid uuid.

### Enum `opyapi.schema.types.Boolean`
Defines enumerated value.

```python
from opyapi.schema.types import Enum
colors = Enum("red", "green", "blue", "yellow")
```

**Arguments:**
 - `default` assigns default value if none is passed in the request
 - `nullable` accepts nulls, nones as value
 - `description` sets open api description for the field
 - `deprecated` deprecates field in the schema
 - `read_only` sets property to read only mode (POST, PUT, PATCH methods cannot mutate property)
 - `write_only` sets property to write only mode (property is hidden from all GET requests)


### Array
Defines iterable/collection item in the schema.

```python
from opyapi.schema.types import Array, Enum

colors = Array(items=Enum("red", "green", "blue", "yellow"))
```

**Arguments:**
 - `items` sets valid schema for each item contained in the array
 - `min_length` sets minimum valid length for the array
 - `max_length` sets maximum valid length for the array
 - `nullable` accepts nulls, nones as value
 - `description` sets open api description for the field
 - `deprecated` deprecates field in the schema
 - `read_only` sets property to read only mode (POST, PUT, PATCH methods cannot mutate property)
 - `write_only` sets property to write only mode (property is hidden from all GET requests)


### Object


## Input handling


## Working with output


## Generating documentation


## Related specs
[Open api specs](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#dataTypes)


[Json schema specs](http://json-schema.org/latest/json-schema-validation.html)
