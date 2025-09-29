from playwright.sync_api import Page
from pages.form_page import FormPage
import allure


@allure.story('Form Page')
def test_formpage(page):
    formpage = FormPage(page)
    formpage.open()
    formpage.fill_element_input_name()
    formpage.fill_element_input_password()
    formpage.fill_element_input_drink()
    formpage.fill_element_input_color()
    formpage.fill_element_input_auto()
    formpage.fill_element_input_email()
    formpage.fill_element_input_message()
    formpage.click_submit()
