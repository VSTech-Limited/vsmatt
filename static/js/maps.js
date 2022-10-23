let map, infoWindow;
let markersArray = [];
function myMap() {
    let vstecPosition = new google.maps.LatLng(-1.1139084362152138, 37.0106327842076)
    let mapOptions = {
        //disables default map controls which are Zoom ,Pan , MapType , Street View
        //disableDefaultUI: true,
        center: vstecPosition,
        zoom: 9,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        //addming all the controls
        panControl: true,
        zoomControl: true,
        mapTypeControl: true,
        scaleControl: true,
        streetViewControl: true,
        overviewMapControl: true,
        rotateControl: true,
        //modifying controls
        mapTypeControlOptions: {
            //style has a default too
            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
            // position: google.maps.ControlPosition.TOP_CENTER
        }
    };

    //create map object
    map = new google.maps.Map(document.getElementById("googleMap"), mapOptions);
    //add vstec marker
    const vstecMarker = new google.maps.Marker({
        position: vstecPosition,
        map: map,
        icon: { url: "{% static 'markers/6.png' %}", scaledSize: new google.maps.Size(70, 70) },
    });
    //add vstec infowindow
    new google.maps.InfoWindow({ content: "vstec limited company" }).open(map, vstecMarker);

    let infoWindow = new google.maps.InfoWindow();
    // create button and give it styling
    const locationButton = document.createElement("button");
    locationButton.textContent = "Pan to Current Location";
    locationButton.className = "custom-map-control-button btn btn-success btn-lg text-dark fw-bold"
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
                    infoWindow.setContent("your current Location found.");
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
                markersArray = []
                let business = result['business'];
                for (const bs of business) {
                    console.log(bs)
                    marker = new google.maps.Marker({
                        position: new google.maps.LatLng(bs.latitude, bs.longitude),
                        map: map,
                        animation: google.maps.Animation.BOUNCE,
                        title: bs.name,
                        //icon: { url: bs.marker, scaledSize: new google.maps.Size(50, 50) },
                    });
                    marker.addListener("click", ()=>{
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

    //     {% for bs in bus %}
    //     marker = new google.maps.Marker({
    //         position: new google.maps.LatLng({{ bs.geolocation }}),
    //         map: map,
    //             icon: { url: "{{bs.marker.url}}", scaledSize: new google.maps.Size(50, 50) },

    // });
    // google.maps.event.addListener(marker, 'click', function () {
    //     //display business
    //     info_window.setContent("{{bs}}");
    //     info_window.open(map, marker);
    //     //zoom on marker clicked
    //     map.setZoom(9);
    //     map.setCenter(marker.getPosition());
    // });
    // {% endfor %}

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