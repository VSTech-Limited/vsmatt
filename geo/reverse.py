from geo.geo_mapquest import GeoMapQuest


class Reverse(GeoMapQuest):
    """
        http://www.mapquestapi.com/geocoding/v1/reverse?key=2dVBKmPmnGAdhlP4AG9HPv7X4dAznIYt
        &location=-1.1139084362152138, 37.0106327842076&includeRoadMetadata=true&
        includeNearestIntersection=true
    """
    base_url = "http://www.mapquestapi.com/geocoding/v1/reverse"
