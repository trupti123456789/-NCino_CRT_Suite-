from robot.api.deco import library, keyword
from selenium.webdriver.common.by import By
from robot.libraries.BuiltIn import BuiltIn
import os

@library
class UploadFile:

    def __init__(self):
        pass

    def _get_driver(self):
        """
        Get active WebDriver instance from CRT
        """
        selenium_lib = BuiltIn().get_library_instance('SeleniumLibrary')
        return selenium_lib.driver

    @keyword("Upload File Using Full Path")
    def upload_file_using_full_path(self, file_path, upload_button_xpath=None):
        """
        Upload file using absolute file path

        Args:
        file_path : Absolute path resolved in Robot
        upload_button_xpath (optional) : XPath of upload button
        """

        driver = self._get_driver()

        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")

        if upload_button_xpath:
            driver.find_element(By.XPATH, upload_button_xpath).click()

        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(file_path)
