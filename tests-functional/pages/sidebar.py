# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected

from pages.base import BasePage


class Sidebar(BasePage):

    _cta_locator = (By.CSS_SELECTOR, 'main button')
    _sidebar_visible_locator = (By.CSS_SELECTOR,
            '#content-deck #sidebar-box[sidebarcommand="viewWebPanelsSidebar"]')  # noqa E501

    @property
    def current_step(self):
        self.switch_to_sidebar_frame()
        cta = self.find_element(*self._cta_locator)
        return cta.get_attribute('data-step')

    @property
    def content_container(self):
        return self.selenium.execute_script("""
            var container = document.querySelector('#sidebar').contentDocument
                              .querySelector('#web-panels-browser').contentDocument
                              .querySelector('body > section');
            return container;
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

    def ensure_reward_sidebar_loaded(self):
        """ Enures that reward sidebar was loaded """
        self.wait_for_content_container_present()
        return self.content_container_id

    def wait_for_content_container_present(self):
        """ Enures reward sidebar content is visible """
        return self.wait.until(expected.visibility_of(self.content_container))

    def wait_for_sidebar_visible(self):
        """ Enures that the sidebar is visible """
        return self.wait.until(
            expected.presence_of_element_located(
                self._sidebar_visible_locator
            )
        )
