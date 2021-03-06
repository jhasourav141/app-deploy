from typing import Any, Dict, Generic, Iterator, Mapping, Optional, Sequence, Type, TypeVar

class ConnectionProxy:
    def __init__(self, connections: Mapping[str, Any], alias: str) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...

class ConnectionDoesNotExist(Exception): ...

_T = TypeVar("_T")

class BaseConnectionHandler(Generic[_T]):
    settings_name: Optional[str] = ...
    exception_class: Type[Exception] = ...
    thread_critical: bool = ...
    def __init__(self, settings: Optional[Any] = ...) -> None: ...
    @property
    def settings(self) -> Dict[str, Any]: ...
    def configure_settings(self, settings: Optional[Dict[str, Any]]) -> Dict[str, Any]: ...
    def create_connection(self, alias: str) -> _T: ...
    def __getitem__(self, alias: str) -> _T: ...
    def __setitem__(self, key: str, value: _T) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def all(self) -> Sequence[_T]: ...
