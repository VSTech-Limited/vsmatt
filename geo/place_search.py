from geo.geo_mapquest import GeoMapQuest


class Search(GeoMapQuest):
    base_url = "http://www.mapquestapi.com/search/v3/prediction"
    """
    "http://www.mapquestapi.com/search/v3/prediction?key=2dVBKmPmnGAdhlP4AG9HPv7X4dAznIYt&limit=5" \
    "&collection=adminArea,poi,address,category,franchise,airport&q=mi "
    """

