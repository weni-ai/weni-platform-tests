from abc import ABCMeta, abstractproperty
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from authenticators import OIDCAuth


class ClientInterface(metaclass=ABCMeta):
    @abstractproperty
    def _base_url(self) -> "str":
        pass

    @abstractproperty
    def _authenticator(self) -> "OIDCAuth":
        pass


class ClientBase(object):
    def _get_url(self, endpoint: str) -> str:
        assert endpoint.startswith("/"), f"The endpoint must contain a leading slash: /{endpoint}"
        return self._base_url + endpoint
