from typing import Any

# Any: Union of possible plugin values is too complex
class Plugin(dict[str, Any]):
    # __init__ wraps dict.__init__  w/o changing the type signature
    def __setitem__(self, key: str, value: Any) -> None: ...

class PluginVersion(str):
    def __init__(self, version: str) -> None: ...
    def __le__(self, version: object) -> bool: ...
    def __lt__(self, version: object) -> bool: ...
    def __ge__(self, version: object) -> bool: ...
    def __gt__(self, version: object) -> bool: ...
    def __eq__(self, version: object) -> bool: ...
    def __ne__(self, version: object) -> bool: ...