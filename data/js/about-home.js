'use strict';

var defaultSnippetContainer = document.querySelector('#snippetContainer');
var searchIconAndTextContainer = document.querySelector('#searchIconAndTextContainer');

/**
 * Load and injects the snipet for the current cotent step
 * @param {int} contentStep - The content step to display
 */
function showSnippet(contentStep) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/data/tmpl/values/content' + contentStep + '-snippet.html', true);
    xhr.responseType = 'DOMString';

    xhr.onload = function() {
        if (this.status === 200) {
            searchIconAndTextContainer.insertAdjacentHTML('afterend', this.responseText);
        }
    };
    xhr.send();
}

// listen for the modify event emitted from the add-on, and only then,
// start executiion of the code.
self.port.on('modify', function(contentStep) {
    // see whether a default snippet container exists
    if (defaultSnippetContainer) {
        defaultSnippetContainer.style.display = 'none';
        showSnippet(contentStep);
    }
});
