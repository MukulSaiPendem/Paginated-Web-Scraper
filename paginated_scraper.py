from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaginatedScraper:
    def __init__(self, start_url, next_button_css_selector, email_pattern=None):
        self.start_url = start_url
        self.next_button_css_selector = next_button_css_selector
        self.email_pattern = email_pattern or r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.all_emails = set()

    def extract_emails_from_page(self):
        page_source = self.driver.page_source
        emails = re.findall(self.email_pattern, page_source)
        return emails

    def go_to_next_page(self):
        try:
            next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.next_button_css_selector))
            )
            next_button.click()
            time.sleep(5)  # Adjust based on the website's content load time
            return True
        except Exception as e:
            print(f"No more pages or an error occurred: {e}")
            return False

    def run(self):
        self.driver.get(self.start_url)
        time.sleep(5)  # Allow page to load

        while True:
            emails = self.extract_emails_from_page()
            self.all_emails.update(emails)
            if not self.go_to_next_page():
                break

        print(f"Total unique emails found: {len(self.all_emails)}")
        for email in self.all_emails:
            print(email)

        self.driver.quit()

# Usage:
# You can replace the start_url and next_button_css_selector with the actual values from the website.
scraper = PaginatedScraper(
    start_url="https://example.com/paginated-page",  # Replace with the actual URL
    next_button_css_selector='a.nextpostslink[rel="next"]'  # Replace with the actual CSS selector for the "Next" button
)
scraper.run()
