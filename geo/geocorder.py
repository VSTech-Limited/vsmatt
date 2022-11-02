from geo.geo_mapquest import GeoMapQuest


class GeoCoder(GeoMapQuest):
    """
        http://www.mapquestapi.com/geocoding/v1/address?key=2dVBKmPmnGAdhlP4AG9HPv7X4dAznIYt&
        location=Washington,DC

    """
    base_url = "http://www.mapquestapi.com/geocoding/v1/address"

    def getPoint(self, location: str):
        self.query_params.update({'location': location})
        resp = self.get()
        if resp.status_code == 200:
            json_data = resp.json()
            if json_data['info']['statuscode'] == 0:
                results = json_data['results']
                for result in results:
                    locations = result['locations']
                    for location in locations:
                        return location['latLng']['lat'], location['latLng']['lng']
