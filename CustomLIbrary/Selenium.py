from SeleniumLibrary.base import LibraryComponent, keyword
import os

class selenium(LibraryComponent):

    @keyword
    def upload_file_lightning(self, locator, file_path):
        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")

        element = self.find_element(locator)
        element.send_keys(file_path)
