let map, infoWindow;
let markersArray = [];
function myMap() {

    let vstecPosition = new google.maps.LatLng(-1.1139084362152138, 37.0106327842076)
    let mapOptions = {
        center: vstecPosition,
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        panControl: true,
        zoomControl: true,
        mapTypeControl: true,
        scaleControl: true,
        streetViewControl: true,
        overviewMapControl: true,
        rotateControl: true,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
        }
    };
    map = new google.maps.Map(document.getElementById("googleMap"), mapOptions);
    getLiveData(map)
    const vstecMarker = new google.maps.Marker({
        position: vstecPosition,
        map: map,
        //icon: { url: "./..markers/6.png", scaledSize: new google.maps.Size(70, 70) },
    });

    const input = document.getElementById("pac-input");
    //var searchBox = new google.maps.places.SearchBox(input);
    let infoWindow = new google.maps.InfoWindow();
    // create button and give it styling
    const locationButton = document.createElement("button");
    locationButton.textContent = "Find my location";
    locationButton.className = "custom-map-control-button btn btn-light bg-white shadow m-3 p-3 btn-sm text-muted fw-light";
    //add the created butTon on the map at the specified position(TOP_CENTER) BY PUSHING IT TO ITS STACK
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);

    $(locationButton).click(function () {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const pos = {
                        lat: position.coords.latitude,
                        lng: position.coords.longitude,
                    };
                    // infoWindow.setPosition(pos);
                    infoWindow.setContent("Your current Location.");
                    let currentPositionMarker = new google.maps.Marker({
                        position: pos,
                        map: map,
                        //icon: { url: "{% static 'markers/1.png' %}", scaledSize: new google.maps.Size(50, 50) },
                    });
                    map.setZoom(15)
                    infoWindow.open(map, currentPositionMarker);
                    map.setCenter(pos);
                    //set marker on current position

                },
                (error) => {
                    //user doent allow the location permision
                    handleLocationError(true, infoWindow, map.getCenter());
                    showError(error)
                }
            );
        } else {
            // Browser doesn't support Geolocation
            handleLocationError(false, infoWindow, map.getCenter());
        }
    });

    function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(
            browserHasGeolocation
                ? "Error: The Geolocation service failed."
                : "Error: Your browser doesn't support geolocation."
        );
        infoWindow.open(map);
    }

    function showError(error) {
        //could be used in place for above handleLocationError
        switch (error.code) {
            case error.PERMISSION_DENIED:
                alert("User denied the request for Geolocation.");
                break;
            case error.POSITION_UNAVAILABLE:
                alert("Location information is unavailable.");
                break;
            case error.TIMEOUT:
                alert("The request to get user location timed out.");
                break;
            case error.UNKNOWN_ERROR:
                alert("An unknown error occurred.");
                break;
        }
    }
    setInterval(() => {
        getLiveData(map)
    },
        5000);
}
function clearOverlays() {
    for (var i = 0; i < markersArray.length; i++) {
        markersArray[i].setMap(null);
    }
    markersArray.length = 0;
}
function getLiveData(map) {
    $.ajax({
        url: "http://127.0.0.1:8000/api/businesses/",
        method: 'GET',
        success: (businesses, status, resp) => {
            clearOverlays()
            for (const business of businesses) {
                const branches = business['branch'];
                for (const branch of branches) {
                    const markerIcon = branch['category']['marker'];
                    const lat = branch['latitude'];
                    const lng = branch['longitude'];
                    const name = branch['name'];
                    const address = branch['address'];
                    const category = branch['category']['title']
                    const bs = { 'name': name, "address": address, "category": category }
                    placeBusinessMarkers(map, lat, lng, markerIcon, bs);

                }
            }
        },
        error: (data, status, resp) => {
            console.log(result.status);
        }

    })
}
function placeBusinessMarkers(map, lat, lng, markerIcon, business) {
    let position = new google.maps.LatLng(lat, lng)
    var marker = new google.maps.Marker({
        position: position,
        map: map,
        title: business['name'],
        animation: google.maps.Animation.BOUNCE,
        icon: { url: markerIcon, scaledSize: new google.maps.Size(50, 50) },
    });
    //add listener on marker
    google.maps.event.addListener(marker, 'click', (event) => {
        map.setCenter(position);
        map.setZoom(12)
        let info = new google.maps.InfoWindow({
            content: `${business['name']} ${business['address']} ${business['category']}`
        });
        //add listener on info window
        google.maps.event.addListener(info, 'click', (event) => {
            alert("yes yes")
        });

        info.open(map, marker);
    });
    markersArray.push(marker)
}