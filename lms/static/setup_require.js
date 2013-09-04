var require = {
    baseUrl: "/suite/lms/include",
    paths: {
        "jquery": "xmodule_js/common_static/js/vendor/jquery.min",
        "jquery.ui" : "xmodule_js/common_static/js/vendor/jquery-ui.min",
        "jquery.cookie": "xmodule_js/common_static/js/vendor/jquery.cookie",
        "jquery.flot": "xmodule_js/common_static/js/vendor/flot/jquery.flot",
        "xmodule": "xmodule_js/src/xmodule",
        "codemirror": "xmodule_js/common_static/js/vendor/CodeMirror/codemirror"
    },
    shim: {
        "jquery.ui": {
            deps: ["jquery"],
            exports: "jQuery.ui"
        },
        "jquery.cookie": {
            deps: ["jquery"],
            exports: "jQuery.fn.cookie"
        },
        "jquery.flot": {
            deps: ["jquery"]
        },
        "xmodule": {
            exports: "XModule"
        },
        "codemirror": {
            exports: "CodeMirror"
        }
    },
    // load these automatically
    deps: []
};
