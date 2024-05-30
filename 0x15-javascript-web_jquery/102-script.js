$(document).ready(function() {
    $('#btn_translate').click(function() {
        // Get the language code from the input field
        const langCode = $('#language_code').val();

        // Construct the URL for the API request
        const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

        $.getJSON(url, function(data) {
        
            const helloTranslation = data.hello;

            $('#hello').text(helloTranslation);
        });
    });
});
