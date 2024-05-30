$(document).ready(function() {
    // Function to fetch translation of hello
    function fetchTranslation() {
        // Get the language code from the input field
        const langCode = $('#language_code').val();

       
        const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

        
        $.getJSON(url, function(data) {
            
            const helloTranslation = data.hello;
            
            $('#hello').text(helloTranslation);
        });
    }

    
    $('#btn_translate').click(fetchTranslation);

    $('#language_code').keypress(function(event) {
        if (event.keyCode === 13) {
            fetchTranslation();
        }
    });
});
