// jquery append

$(document).ready(function () {
    $('#add_item').click(function () {
       const addList = $('<li>Item</li>')
       $('ul.my_list').append(addList); 
    });
});
