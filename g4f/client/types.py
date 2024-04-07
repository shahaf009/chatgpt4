from ..providers.types import BaseProvider, ProviderType, FinishReason
from typing import Union, Iterator

ImageProvider = Union[BaseProvider, object]
Proxies = Union[dict, str]
IterResponse = Iterator[Union[ChatCompletion, ChatCompletionChunk]]

class ClientProxyMixin():
    def get_proxy(self) -> Union[str, None]:
        if isinstance(self.proxies, str):
            return self.proxies
        elif self.proxies is None:
            return os.environ.get("G4F_PROXY")
        elif "all" in self.proxies:
            return self.proxies["all"]
        elif "https" in self.proxies:
            return self.proxies["https"]

class Client(ClientProxyMixin):
    def __init__(
        self,
        api_key: str = None,
        proxies: Proxies = None,
        provider: ProviderType = None,
        image_provider: ImageProvider = None,
        **kwargs
    ) -> None:
        self.api_key: str = api_key
        self.proxies: Proxies = proxies
