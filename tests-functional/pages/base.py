# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pypom import Page

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected


class BasePage(Page):

    _sidebar_locator = (By.CSS_SELECTOR, '#content-deck #sidebar-box')
    _sidebar_frame_locator = (By.ID, '#web-panels-browser')

    def switch_to_sidebar(self):
        """ switches to the sidebar frame if available """
        # switch to browser chrome
        self.selenium.set_context('chrome')
        # switch to sidebar frame
        self.wait.until(expected.frame_to_be_available_and_switch_to_it(
            self._sidebar_locator
        ))

    def switch_to_sidebar_frame(self):
        """ switches to the web panels browser if available """
        self.switch_to_sidebar()
        # switch to browser chrome
        self.selenium.set_context('chrome')
        # switch to sidebar content
        self.wait.until(expected.frame_to_be_available_and_switch_to_it(
            self._sidebar_frame_locator
        ))
