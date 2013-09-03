define(['logme'], function (logme) {
    return Container;

    function Container(state) {
        state.containerEl = $(
            '<div ' +
                'style=" ' +
                    'clear: both; ' +
                    'width: 665px; ' +
                    'margin-left: auto; ' +
                    'margin-right: auto; ' +
                '" ' +
            '></div>'
        );

        $('#inputtype_' + state.problemId).before(state.containerEl);
    }
}); // End-of: define(['logme'], function (logme) {
