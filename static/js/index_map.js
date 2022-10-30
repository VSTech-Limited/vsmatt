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

    const vstecMarker = new google.maps.Marker({
        position: vstecPosition,
        map: map,
        //icon: { url: "./..markers/6.png", scaledSize: new google.maps.Size(70, 70) },
    });
    new google.maps.InfoWindow({ content: "VSTech Limited Company" }).open(map, vstecMarker);
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
                        icon: { url: "{% static 'markers/1.png' %}", scaledSize: new google.maps.Size(50, 50) },
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


    let marker;

    setInterval(() => {
        //alert("Hellow")
        $.ajax({
            url: 'http://127.0.0.1:8000/shops/business/',
            method: 'GET',
            success: (result, status, resp) => {
                clearOverlays()
                let business = result['business'];
                for (const bs of business) {
                    console.log(`'http://127.0.0.1:8000/media/${bs.marker}'`)
                    marker = new google.maps.Marker({
                        position: new google.maps.LatLng(bs.latitude, bs.longitude),
                        map: map,
                        animation: google.maps.Animation.BOUNCE,
                        title: bs.name
                        //icon: { url: `'${bs.marker}'`, scaledSize: new google.maps.Size(50, 50) },
                    });
                    marker.addListener("click", () => {
                        //add window info
                    });
                    markersArray.push(marker)
                }

            },
            error: (result, status, resp) => {
                console.log(result.status);
            }
        });
    },
        2000);
    google.maps.event.addListener(map, 'click', function (event) {
        placeMarker(map, event.latLng);
    });

    function placeMarker(map, location) {
        var marker = new google.maps.Marker({
            position: location,
            map: map,
            icon: { url: "{% static 'markers/2_1.png' %}", scaledSize: new google.maps.Size(50, 50) },
        });
    }
}

function clearOverlays() {
    for (var i = 0; i < markersArray.length; i++) {
        markersArray[i].setMap(null);
    }
    markersArray.length = 0;
}

function mapBusinessMarkers(map){
    $.ajax({
        url: "http://127.0.0.1:8000/api/businesses/",
        method: 'GET',
        success: (data, status, resp)=>{
            console.log(data)
        },
        error: (data, status, resp) =>{
          console.log(data)
        }
        
      })
}