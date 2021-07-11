 autocomplete = new google.maps.places.Autocomplete(document.getElementById("autocomplete",
{
    componentRestrictions: {country: 'GB'},
    fields: ['geometry', 'name']
}));