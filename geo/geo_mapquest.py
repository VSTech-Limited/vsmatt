import requests
from requests import Response


class GeoMapQuest:
    base_url: str = ""
    query_params: dict = {}
    """
    """

    def __init__(self, api_key: str):
        self._api_key = api_key

    @property
    def apiKey(self):
        return self._api_key

    @apiKey.setter
    def apiKey(self, value):
        self._api_key = value

    def get_url(self) -> str:
        return self.base_url

    def get_query_params(self) -> dict:
        return self.query_params

    def _construct_url(self) -> str:
        qp = self.get_query_params()
        qp.update({'key': self._api_key})
        params = [f"{key}={qp[key]}" for key in qp]
        return f'{self.get_url()}?{"&".join(params)}'

    def getJson(self):
        return self.get().json()

    def get(self) -> Response:
        return requests.get(self._construct_url())
