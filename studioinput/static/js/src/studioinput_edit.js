function StudioInputEditXBlock(runtime, element) {
    $(element).find('.save-button').bind('click', function() {
        var handlerUrl = runtime.handlerUrl(element, 'studio_submit');


        /* Every flashcard (input-item) has two input fields, "front" and "back" */
        var input_list = {};
        var items = document.getElementsByClassName('input-item');

        for (var i = 0; i < items.length; i++) {
            var inputs = items[i].getElementsByTagName('input');
            input_list[inputs[0].value] = inputs[1].value;
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
        var addFieldButton = document.getElementById("more_fields");
    var input_number = 1;

    function add_fields() {
        input_number++;
        var fields = '<div class="input-item">\n\
        <label class="label setting-label" for="flashcards">Input (' + input_number + ')</label>\n\
        <input class="input setting-input" name="text-'+input_number+'" placeholder="Text" type="text" />\n\
        </div>';
    }

    addFieldButton.addEventListener("click", add_fields);
}
