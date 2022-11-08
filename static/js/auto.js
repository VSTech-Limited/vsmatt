
var places = [];
var coords = [];

function aheadOfTimeSearch(country) {
    if (country.length > 2) {
        $.getJSON(
            `http://www.mapquestapi.com/search/v3/prediction?key=2dVBKmPmnGAdhlP4AG9HPv7X4dAznIYt&limit=5&collection=adminArea,poi,address,category,franchise,airport&q=${country}`,
            (resp) => {
                results = resp['results'];
                places[country] = []
                for (const result of results) {
                    const s = result['displayString']
                    const c = result['place']
                    if (places.indexOf(s) === -1 && c) {
                        places.push(s);
                        coords.push(c)
                    }
                    /*
                    places[country].push({
                        'displayString': result['displayString'],
                        'name': result['name']

                    })
                    //console.log(displayString)
                    // console.log(places)

*/
                }
            },
        );
    }
}



function onReady() {
    $("#locationSearch").autocomplete({
        //called on input event
        source: (request, response) => {
            //works for now but inefficient, to be improved later
            const seachLocation = request.term;
            aheadOfTimeSearch(seachLocation)
            const p = places.filter(function (place) {
                const lowerp = place.toLowerCase()
                return lowerp.includes(seachLocation.toLowerCase())
            })
            response(p);
            /*
            //checks if location had already been queried before reducing server calls
            if (seachLocation in places) {
                const p = places[seachLocation]
                .map(function(place){
                    //console.log(place)
                    return place['displayString'];
                })
                response(p);
                return;
            }
            aheadOfTimeSearch(seachLocation)
            //check after update if thee exist search place in result
            if(seachLocation in places){
                const p = places[seachLocation]
                .map(function(place){
                    return place['displayString'];
                })
                response(p);
                return;
            }
            // response(places);
            // console.log(places);
            //response(places)
            // return places1
            */
        },
        minLength: 2,
        autofocus: true,
        // delay: 500,
    });
    
}

function onEnter(event, map, markerIcon) {
    if (event.code == 'Enter') {
        event.preventDefault();
        const currIndex = places.indexOf($('#locationSearch').val())
        if (currIndex !== -1) {
            const lng = coords[currIndex]['geometry']['coordinates'][0]
            const lat = coords[currIndex]['geometry']['coordinates'][1]
            // alert(coords[currIndex]['geometry']['coordinates'])
            // // alert(map)
            const position = new google.maps.LatLng(lat, lng);
            placeAndZoom(map, position, markerIcon)
        }
    }
}

function placeAndZoom(map, position, markerIcon) {
    new google.maps.Marker({
        position: position,
        draggable:true,
        map: map,
        icon: { url: markerIcon, scaledSize: new google.maps.Size(70, 70) },
        animation: google.maps.Animation.BOUNCE,
    });
    map.setCenter(position);
    map.setZoom(16);

}



