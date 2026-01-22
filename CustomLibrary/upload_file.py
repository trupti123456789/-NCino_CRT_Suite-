from robot.api.deco import library, keyword
from selenium.webdriver.common.by import By
import os

@library
class UploadFile:

    def __init__(self, driver=None):
        self.driver = driver

        # Resolve Git project root dynamically
        self.project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )

    @keyword
    def upload_file_from_data_folder(self, upload_button_xpath, file_name):
        
        # Build full file path
        full_path = os.path.join(self.project_root, "Data", file_name)

        # Click upload button if required
        if upload_button_xpath:
            self.driver.find_element(By.XPATH, upload_button_xpath).click()

        # Locate file input
        file_input = self.driver.find_element(By.XPATH, "//input[@type='file']")

        #  Upload file
        file_input.send_keys(full_path)
