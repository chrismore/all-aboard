'use strict';

var defaultSnippetContainer = document.querySelector('#snippetContainer');
var searchIconAndTextContainer = document.querySelector('#searchIconAndTextContainer');

/**
 * Load and injects the snipet for the current cotent step
 * @param {string} snippetContent - The content to inject
 */
function showSnippet(snippetContent) {
    var button;
    searchIconAndTextContainer.insertAdjacentHTML('afterend', snippetContent);

    button = document.querySelector('#allaboard_button');
    button.addEventListener('click', function() {
        // pass the button intent to the add-on
        self.port.emit('intent', button.dataset['intent']);
    });
}

// listen for the modify event emitted from the add-on, and only then,
// start executiion of the code.
self.port.on('modify', function(snippetContent) {
    // see whether a default snippet container exists
    if (defaultSnippetContainer) {
        defaultSnippetContainer.style.display = 'none';
        showSnippet(snippetContent);
    }
});
