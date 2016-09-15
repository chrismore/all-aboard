# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.all_aboard import AllAboard
from pages.firstrun import Firstrun
from pages.sidebar import Sidebar


@pytest.fixture
def complete_firstrun(base_url, selenium):
    """ Completes /firstrun interactions to start on-boarding"""
    page = Firstrun(selenium, base_url).open()
    page.complete_firstrun_values_flow()
    return page


@pytest.mark.nondestructive
@pytest.mark.capabilities(firefox_args=['-foreground'])
def test_successful_values_flow(base_url,
                                selenium,
                                complete_firstrun):
    """Tests that a user can successfully complete the values track"""
    # switch to browser chrome
    selenium.set_context('chrome')

    all_aboard = AllAboard(selenium, timeout=20)
    sidebar = Sidebar(selenium)

    all_aboard.wait_for_action_button_present()
    sidebar.wait_for_sidebar_visible()

    all_aboard.load_next_sidebar()

    previous_step = 0
    while int(sidebar.current_step) < 5:
        all_aboard.load_next_sidebar()
        # ensure that the sidebar is shown after click on ActionButton
        assert all_aboard.sidebar.get_attribute('hidden') == 'false'
        # ensure that the correct sidebar is shown
        assert int(sidebar.current_step) == previous_step + 1
        # store the current step for the next iteration
        previous_step = int(sidebar.current_step)
        # move the experience on to the next step
        sidebar.click_cta()

    # click the claim prize button
    sidebar.claim_prize()
    assert sidebar.ensure_reward_sidebar_loaded() == 'reward'
