from typing import List, Any


class Copyright:
    text: str
    image_url: str
    image_alt_text: str

    def __init__(self, text: str, image_url: str, image_alt_text: str) -> None:
        self.text = text
        self.image_url = image_url
        self.image_alt_text = image_alt_text

    @classmethod
    def from_dict(cls, obj: Any) -> 'Copyright':
        _text = str(obj.get("text"))
        _imageUrl = str(obj.get("imageUrl"))
        _imageAltText = str(obj.get("imageAltText"))
        return cls(_text, _imageUrl, _imageAltText)

    def __str__(self):
        return str(self.__dict__)


class Info:
    statuscode: int
    copyright: Copyright
    messages: List[str]

    def __init__(self, statuscode: int, copyright: Copyright, messages: List[Any]) -> None:
        self.statuscode = statuscode
        self.copyright = copyright
        self.messages = messages

    @classmethod
    def from_dict(cls, obj: Any) -> 'Info':
        _statuscode = int(obj.get("statuscode"))
        _copyright = Copyright.from_dict(obj.get("copyright"))
        _messages = list(obj.get("messages"))
        return cls(_statuscode, _copyright, _messages)

    def __str__(self):
        return str(self.__dict__)


class Options:
    max_results: int
    ignore_lat_lng_input: bool

    def __init__(self, max_results: int, ignore_lat_lng_input: bool) -> None:
        self.max_results = max_results
        self.ignore_lat_lng_input = ignore_lat_lng_input

    @classmethod
    def from_dict(cls, obj: Any) -> 'Options':
        _maxResults = int(obj.get("maxResults"))
        _ignoreLatLngInput = bool(obj.get("ignoreLatLngInput"))
        return cls(_maxResults, _ignoreLatLngInput)

    def __str__(self):
        return str(self.__dict__)


class LatLng:
    lat: float
    lng: float

    def __init__(self, lat: float, lng: float) -> None:
        self.lat = lat
        self.lng = lng

    @classmethod
    def from_dict(cls, obj: Any) -> 'LatLng':
        _lat = float(obj.get("lat"))
        _lng = float(obj.get("lng"))
        return cls(_lat, _lng)

    def __str__(self):
        return str(self.__dict__)


class Location:
    street: str
    admin_area6: str
    admin_area6_type: str
    admin_area5: str
    admin_area5_type: str
    admin_area4: str
    admin_area4_type: str
    admin_area3: str
    admin_area3_type: str
    admin_area1: str
    admin_area1_type: str
    postal_code: str
    geocode_quality_code: str
    geocode_quality: str
    drag_point: bool
    side_of_street: str
    link_id: str
    unknown_input: str
    type: str
    lat_lng: LatLng
    display_lat_lng: LatLng
    map_url: str

    def __init__(
            self, street: str, admin_area6: str, admin_area6_type: str, admin_area5: str, admin_area5_type: str,
            admin_area4: str, admin_area4_type: str, admin_area3: str, admin_area3_type: str, admin_area1: str,
            admin_area1_type: str, postal_code: str, geocode_quality_code: str, geocode_quality: str,
            drag_point: bool, side_of_street: str, link_id: str, unknown_input: str, type: str, lat_lng: LatLng,
            display_lat_lng: LatLng, map_url: str
    ) -> None:
        self.street = street
        self.admin_area6 = admin_area6
        self.admin_area6_type = admin_area6_type
        self.admin_area5 = admin_area5
        self.admin_area5_type = admin_area5_type
        self.admin_area4 = admin_area4
        self.admin_area4_type = admin_area4_type
        self.admin_area3 = admin_area3
        self.admin_area3_type = admin_area3_type
        self.admin_area1 = admin_area1
        self.admin_area1_type = admin_area1_type
        self.postal_code = postal_code
        self.geocode_quality_code = geocode_quality_code
        self.geocode_quality = geocode_quality
        self.drag_point = drag_point
        self.side_of_street = side_of_street
        self.link_id = link_id
        self.unknown_input = unknown_input
        self.type = type
        self.lat_lng = lat_lng
        self.display_lat_lng = display_lat_lng
        self.map_url = map_url

    @classmethod
    def from_dict(cls, obj: Any) -> 'Location':
        _street = str(obj.get("street"))
        _adminArea6 = str(obj.get("adminArea6"))
        _adminArea6Type = str(obj.get("adminArea6Type"))
        _adminArea5 = str(obj.get("adminArea5"))
        _adminArea5Type = str(obj.get("adminArea5Type"))
        _adminArea4 = str(obj.get("adminArea4"))
        _adminArea4Type = str(obj.get("adminArea4Type"))
        _adminArea3 = str(obj.get("adminArea3"))
        _adminArea3Type = str(obj.get("adminArea3Type"))
        _adminArea1 = str(obj.get("adminArea1"))
        _adminArea1Type = str(obj.get("adminArea1Type"))
        _postalCode = str(obj.get("postalCode"))
        _geocodeQualityCode = str(obj.get("geocodeQualityCode"))
        _geocodeQuality = str(obj.get("geocodeQuality"))
        _dragPoint = bool(obj.get('dragPoint'))
        _sideOfStreet = str(obj.get("sideOfStreet"))
        _linkId = str(obj.get("linkId"))
        _unknownInput = str(obj.get("unknownInput"))
        _type = str(obj.get("type"))
        _latLng = LatLng.from_dict(obj.get("latLng"))
        _displayLatLng = LatLng.from_dict(obj.get("displayLatLng"))
        _mapUrl = str(obj.get("mapUrl"))
        return cls(
            _street, _adminArea6, _adminArea6Type, _adminArea5, _adminArea5Type, _adminArea4,
            _adminArea4Type, _adminArea3, _adminArea3Type, _adminArea1, _adminArea1Type, _postalCode,
            _geocodeQualityCode, _geocodeQuality, _dragPoint, _sideOfStreet, _linkId, _unknownInput, _type,
            _latLng, _displayLatLng, _mapUrl
        )

    def __str__(self):
        return str(self.__dict__)


class ProvidedLocation:
    lat_lng: LatLng

    def __init__(self, lat_lng: LatLng) -> None:
        self.lat_lng = lat_lng

    @classmethod
    def from_dict(cls, obj: Any) -> 'ProvidedLocation':
        _latLng = LatLng.from_dict(obj.get("latLng"))
        return cls(_latLng)

    def __str__(self):
        return str(self.__dict__)


class Result:
    provided_location: ProvidedLocation
    locations: List[Location]

    def __init__(self, provided_location: ProvidedLocation, locations: List[Location]) -> None:
        self.provided_location = provided_location
        self.locations = locations

    @classmethod
    def from_dict(cls, obj: Any) -> 'Result':
        _providedLocation = ProvidedLocation.from_dict(obj.get("providedLocation"))
        _locations = [Location.from_dict(y) for y in obj.get("locations")]
        return cls(_providedLocation, _locations)

    def __str__(self):
        return str(self.__dict__)


class GeoData:
    info: Info
    options: Options
    results: List[Result]

    def __init__(self, info: Info, options: Options, results: List[Result]) -> None:
        self.info = info
        self.options = options
        self.results = results

    @classmethod
    def from_dict(cls, obj: Any) -> 'GeoData':
        _info = Info.from_dict(obj.get("info"))
        _options = Options.from_dict(obj.get("options"))
        _results = [Result.from_dict(y) for y in obj.get("results")]
        return cls(_info, _options, _results)

    def __str__(self):
        return str(self.__dict__)
