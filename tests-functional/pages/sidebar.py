# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pypom import Page


class Sidebar(Page):

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

    @property
    def prize_button(self):
        return self.selenium.execute_script("""
            var button = document.querySelector('#sidebar').contentDocument
                              .querySelector('#web-panels-browser').contentDocument
                              .querySelector('footer #prize');
            return button;
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
