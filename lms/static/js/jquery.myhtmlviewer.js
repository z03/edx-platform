define(["jquery"], function($) {
    $.fn.myHTMLViewer = function(options) {
        var urlToLoad = null;
        if (options.url) {
            urlToLoad = options.url;
        }
        var chapterUrls = null;
        if (options.chapters) {
            chapterUrls = options.chapters;
        }
        var chapterToLoad = 1;
        if (options.chapterNum) {
            // TODO: this should only be specified if there are
            // chapters, and it should be in-bounds.
            chapterToLoad = options.chapterNum;
        }
        var anchorToLoad = null;
        if (options.chapters) {
            anchorToLoad = options.anchor_id;
        }

        var onComplete = function() {};
        if(options.notesEnabled) {
            onComplete = function(url) {
                return function() {
                    $('#viewerContainer').trigger('notes:init', [url]);
                };
            };
        }

        loadUrl = function htmlViewLoadUrl(url, anchorId) {
            // clear out previous load, if any:
            parentElement = document.getElementById('bookpage');
            while (parentElement.hasChildNodes())
                parentElement.removeChild(parentElement.lastChild);
        // load new URL in:
            $('#bookpage').load(url, null, onComplete(url));

        // if there is an anchor set, then go to that location:
            if (anchorId != null) {
        // TODO: add implementation....
            }

        };

        loadChapterUrl = function htmlViewLoadChapterUrl(chapterNum, anchorId) {
            if (chapterNum < 1 || chapterNum > chapterUrls.length) {
                return;
            }
            var chapterUrl = chapterUrls[chapterNum-1];
            loadUrl(chapterUrl, anchorId);
        };

        // define navigation links for chapters:
        if (chapterUrls != null) {
            var loadChapterUrlHelper = function(i) {
                return function(event) {
                    // when opening a new chapter, always open to the top:
                    loadChapterUrl(i, null);
                };
            };
            for (var index = 1; index <= chapterUrls.length; index += 1) {
                $("#htmlchapter-" + index).click(loadChapterUrlHelper(index));
            }
        }

        // finally, load the appropriate url/page
        if (urlToLoad != null) {
            loadUrl(urlToLoad, anchorToLoad);
        } else {
            loadChapterUrl(chapterToLoad, anchorToLoad);
        }

    };
    return $.fn.myHTMLViewer;
});
