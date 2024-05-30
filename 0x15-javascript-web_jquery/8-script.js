const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$(document).ready(function () {
    $.getJSON(url, function(data){
        data.results.forEach(function(mov){
            const mTitle = mov.title;

            const fulList = $('<li></li>').text(mTitle);

            $('ul#list_movies').append(fulList);
        });
    });
});
