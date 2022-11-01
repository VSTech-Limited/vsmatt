from .geo_mapquest import GeoMapQuest
from .geocorder import GeoCoder
from .place_search import Search
from .reverse import Reverse


class GeoMapQuestFactory:
    @staticmethod
    def createGeocoder(api_key: str) -> GeoCoder:
        return GeoCoder(api_key)

    @staticmethod
    def createReverse(api_key: str) -> Reverse:
        return Reverse(api_key)

    @staticmethod
    def createPlaceSearch(api_key: str) -> Search:
        return Search(api_key)
