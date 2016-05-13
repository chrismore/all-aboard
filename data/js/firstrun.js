(function() {
    var fxAccountsContainer = document.querySelector('.fxaccounts');
    var addonContent;
    var contentContainer;
    var heading;
    var mainContainer;

    // template strings
    var dialog = '<section id="all-aboard" class="dialog">' +
                 '<header>' +
                 '<h2>I’ve used Firefox in the last 30 days?</h2>' +
                 '<div class="form-elements">' +
                 '<label for="yup">' +
                 '<input type="radio" name="isNewUser" value="yes" id="yup" />yup</label>' +
                 '<label for="nope">' +
                 '<input type="radio" name="isNewUser" value="no" id="nope" checked />nope</label>' +
                 '</div>' +
                 '</header>' +
                 '<main class="what-matters">' +
                 '<h2>I’m happiest knowing that me browser:</h2>' +
                 '<label for="features">' +
                 '<input type="radio" name="whatMatters" value="features" id="features" checked />Has unique capabilities and features</label>' +
                 '<label for="values">' +
                 '<input type="radio" name="whatMatters" value="values" id="values" />Is backed by a non-profitwith a mission to...</label>' +
                 '</main>' +
                 '<footer>' +
                 '<a href="about:home" id="dismiss">No thanks</a>' +
                 '<button type="button" class="button">Go!</button>' +
                 '</footer>' +
                 '</section>';

    // shows the default heading and the Fx accounts widget
    function showFxAccountWidget() {
        document.querySelector('#all-aboard').style.display = 'none';
        // show the default heading and the Fx accounts widget
        heading.style.display = 'block';
        mainContainer.style.display = 'block';
    }

    // hide the default heading and the Fx accounts widget
    function hideFxAccountWidget() {
        heading.style.display = 'none';
        mainContainer.style.display = 'none';
    }

    /**
     * Shows the questions dialog on the /firstrun page
     */
    function showDialog() {
        contentContainer = document.querySelector('#intro .container');
        contentContainer.insertAdjacentHTML('beforeend', dialog);
        contentContainer.focus();

        // listen for a click event on the 'No Thanks' link and send preference
        contentContainer.querySelector('#dismiss').addEventListener('click', function() {
            self.port.emit('onboardingDismissed', 'true');
        });

        submitHandler();
    }

    /**
     * Handles submission of form elements in dialog
     */
    function submitHandler() {
        var addonContent = document.querySelector('#all-aboard');
        var button = addonContent.querySelector('button');

        button.addEventListener('click', function() {
            checkedElems = addonContent.querySelectorAll('input[type="radio"]:checked');

            for (var i = 0,l = checkedElems.length; i < l; i++) {
                self.port.emit(checkedElems[i].name, checkedElems[i].value);
            }

            showFxAccountWidget();
        });
    }

    // see whether a Firefox Accounts section exists
    if (fxAccountsContainer) {
        heading = document.querySelector('#intro header h2');
        mainContainer = document.querySelector('main');

        hideFxAccountWidget();
        showDialog();
    }
})();