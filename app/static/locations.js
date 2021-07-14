input = document.getElementById("autocomplete")
options = {
    componentRestrictions: {country: 'GB'},
    fields: ["geometry", "name"],
}

autocomplete = new google.maps.places.Autocomplete(input, options);