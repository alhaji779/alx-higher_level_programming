const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$(document).ready(function () {
    $.getJSON(url, function(data){
        const cName = data.name;
        $('#character').text(cName);
    })
});
