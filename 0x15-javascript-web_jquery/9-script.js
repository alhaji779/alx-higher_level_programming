const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(document).ready(function () {
    $.getJSON(url, function(data){
        const getHello = data.hello;

        $('#hello').text(getHello);
    });
});
