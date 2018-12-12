$(document).ready(function() {
    document.session = $('#session').val();
    setTimeout(requestInventory, 100);

    $('#add-button').click(function(event) {
        $.ajax({
            url: '//10.5.1.49:8000/cart',
            type: 'POST',
            data: {
                session: document.session,
                action: 'add'
            },
            //dataType: 'json',
            beforeSend: function(xhr, settings) {
                $(event.target).attr('disabled', 'disabled');
            },
            success: function(data, status, xhr) {
                console.log('1');
                $('#add-to-cart').hide();
                $('#remove-from-cart').show();
                $(event.target).removeAttr('disabled');
            },
            error: function(XMLHttpRequest, textStatus, errorThrown){
                console.log(textStatus);
            },
        });
    });

    $('#remove-button').click(function(event) {
        jQuery.ajax({
            url: '//10.5.1.49:8000/cart',
            type: 'POST',
            data: {
                session: document.session,
                action: 'remove'
            },
            //dataType: 'json',
            beforeSend: function(xhr, settings) {
                $(event.target).attr('disabled', 'disabled');
            },
            success: function(data, status, xhr) {
                $('#remove-from-cart').hide();
                $('#add-to-cart').show();
                $(event.target).removeAttr('disabled');
            }
        });
    });
});

function requestInventory() {
    jQuery.getJSON('//10.5.1.49:8000/cart/status', {session: document.session},
        function(data, status, xhr) {
            $('#count').html(data['inventoryCount']);
            setTimeout(requestInventory, 0);
        }
    );
}
