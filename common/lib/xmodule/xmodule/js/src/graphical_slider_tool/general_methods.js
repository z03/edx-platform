define('GeneralMethods', [], function () {
    if (!String.prototype.trim) {
        // http://blog.stevenlevithan.com/archives/faster-trim-javascript
        String.prototype.trim = function trim(str) {
            return str.replace(/^\s\s*/, '').replace(/\s\s*$/, '');
        };
    }

    return {
        'module_name': 'GeneralMethods',
        'module_status': 'OK'
    };
});
