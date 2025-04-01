from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome WebDriver (Headless Mode for Railway)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without opening a browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# Open the website
URL = "https://scalacube.com/cp#/bill/node/4307733/testRenew"  # Change this to your site
driver.get(URL)

while True:
    try:
        # Wait until the button is enabled and clickable
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='renew()']")))

        # Remove 'disabled' attribute if needed
        driver.execute_script("arguments[0].removeAttribute('disabled');", button)

        # Click the button
        button.click()
        print("Button clicked!")

        # Wait for 5 seconds (adjust delay as needed)
        time.sleep(5)

        # Refresh the page
        driver.refresh()
        print("Page refreshed!")

    except Exception as e:
        print("Error:", e)
        break  # Stop if there's an issue

driver.quit()
