# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pypom import Page

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected


class Sidebar(Page):

    _sidebar_visible_locator = (By.CSS_SELECTOR,
            '#content-deck #sidebar-box[sidebarcommand="viewWebPanelsSidebar"]')  # noqa E501

    @property
    def current_step(self):
        return self.selenium.execute_script("""
            var cta = document.querySelector('#sidebar').contentDocument
                              .querySelector('#web-panels-browser').contentDocument
                              .querySelector('main button');
            return cta.dataset.step;
        """)

    @property
    def content_container_id(self):
        return self.selenium.execute_script("""
            var container = document.querySelector('#sidebar').contentDocument
                              .querySelector('#web-panels-browser').contentDocument
                              .querySelector('body > section');
            return container.getAttribute('id');
        """)

    def claim_prize(self):
        return self.selenium.execute_script("""
            var button = document.querySelector('#sidebar').contentDocument
                              .querySelector('#web-panels-browser').contentDocument
                              .querySelector('footer #prize');
            button.click();
        """)

    def click_cta(self):
        return self.selenium.execute_script("""
            var cta = document.querySelector('#sidebar').contentDocument
                              .querySelector('#web-panels-browser').contentDocument
                              .querySelector('main button');
            cta.click();
        """)

    def wait_for_sidebar_visible(self):
        """ Enures that the sidebar is visible """
        return self.wait.until(
            expected.presence_of_element_located(
                self._sidebar_visible_locator
            )
        )
