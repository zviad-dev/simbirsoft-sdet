from playwright.sync_api import expect


class FormPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(
            'https://practice-automation.com/form-fields/', timeout=60000)

    def fill_element_input_name(self):
        self.page.locator('#name-input').fill("Zviad")

    def fill_element_input_password(self):
        self.page.locator(
            'xpath=//label[contains(text(), "Password")]//input[@type="password"]').fill("Password1!")

    def fill_element_input_drink(self):
        self.page.get_by_text("Milk").click()
        self.page.get_by_text("Coffee").click()

    def fill_element_input_color(self):
        self.page.get_by_text("Yellow", exact=True).click()

    def fill_element_input_auto(self):
        self.page.get_by_test_id("automation").select_option("yes")

    def fill_element_input_email(self):
        self.page.get_by_test_id("email").fill("name@example.com")

    def fill_element_input_message(self):

        def data_for_message(data):
            text_auto = self.page.get_by_test_id(
                "automation").text_content().split()
            return max(data, key=len) + ' ' + str(len(data))

        text_auto = self.page.locator(
            'label:has-text("Automation tools") + ul li').all_inner_texts()
        self.page.get_by_test_id("message").fill(data_for_message(text_auto))

    def click_submit(self):

        def handle_dialog(dialog):
            assert (dialog.message == 'Message received!')
            dialog.accept()

        self.page.on("dialog", handle_dialog)
        self.page.get_by_test_id("submit-btn").click()
