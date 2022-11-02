from decimal import Decimal
from typing import Tuple, Any
from geo.models import GeoData
from requests import Response

from geo.geo_mapquest import GeoMapQuest


class Reverse(GeoMapQuest):
    """
        http://www.mapquestapi.com/geocoding/v1/reverse?key=2dVBKmPmnGAdhlP4AG9HPv7X4dAznIYt
        &location=-1.1139084362152138, 37.0106327842076&includeRoadMetadata=true&
        includeNearestIntersection=true
    """
    base_url = "http://www.mapquestapi.com/geocoding/v1/reverse"

    def reverse(self, latLng: tuple[Decimal, Decimal]) -> Tuple[GeoData, Response]:
        # TODO WORK ON RETURN TYPE
        if len(latLng) > 1:
            self.query_params.update({'location': f"{latLng[1]}, {latLng[0]}"})
            self.query_params.update({'includeRoadMetadata': 'true'})
            self.query_params.update({'includeNearestIntersection': 'true'})
            response = self.get()
            return GeoData.from_dict(response.json()), response

    def getLocations(self, latLng: tuple[Decimal, Decimal]):
        resp, data = self.reverse(latLng)
        # 400 if no result
        if resp.status_code == 200:
            json_data = resp.json()
            if json_data['info']['statuscode'] == 0:
                results = json_data['results']
                for result in results:
                    locations = result['locations']
                    for location in locations:
                        return location
        # return json_data

    def getAddress(self, latLng: tuple[Decimal, Decimal]):
        # TODO,KINDLY REVISIT
        location = self.reverse(latLng)
        if location:
            return f"{location['postalCode']} {location['street']} {location['adminArea5']} "
