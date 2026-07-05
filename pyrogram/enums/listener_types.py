from .auto_name import AutoName
from enum import auto

class ListenerTypes(AutoName):
    MESSAGE = auto()
    "message"
    CALLBACK_QUERY = auto()
    "callback_query"