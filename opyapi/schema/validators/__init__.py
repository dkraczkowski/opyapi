from .capacity import Capacity
from .date import Date
from .date_time import DateTime
from .email import Email
from .falsy import Falsy
from .hostname import Hostname
from .ipv4 import Ipv4
from .ipv6 import Ipv6
from .length import Length
from .multiple_of import MultipleOf
from .range import Range
from .sem_ver import SemVer
from .time import Time
from .truthy import Truthy
from .uri import Uri
from .url import Url
from .uuid import Uuid
from .validator import Validator


class Validators:
    date = Date()
    date_time = DateTime()
    email = Email()
    falsy = Falsy()
    hostname = Hostname()
    ipv4 = Ipv4()
    ipv6 = Ipv6()
    sem_ver = SemVer()
    time = Time()
    truthy = Truthy()
    uri = Uri()
    url = Url()
    uuid = Uuid()


validators = Validators()
