function StudioInputEditXBlock(runtime, element) {
    $(element).find('.save-button').bind('click', function() {
        var handlerUrl = runtime.handlerUrl(element, 'studio_submit');

        var input_list = {};
        var items = document.getElementsByClassName('input-item');

        for (var i = 0; i < items.length; i++) {
            var inputs = items[i].getElementsByTagName('input');
            input_list[i] = inputs[i].value;
        }

        var data = {
            inputs: input_list
        };

        var test = JSON.stringify(data);

        runtime.notify('save', {state: 'start'});
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            runtime.notify('save', {state:'end'});
        });
    });

    $(element).find('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
    });
}
