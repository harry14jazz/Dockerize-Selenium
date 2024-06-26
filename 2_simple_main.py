from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

def get_top_10_search_results(keyword, headless=False):
    # Chrome options
    options = Options()
    if headless:
        options.add_argument("--headless")  # Run in headless mode if specified
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}

    # Initialize the webdriver
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open Google and search for the keyword
    driver.get("https://www.google.com/")
    search_box = driver.find_element(By.XPATH, "//*[@id='APjFqb']")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    sleep(2)  # Let the page load

    # Get the top 10 search results
    search_results = driver.find_elements(By.CLASS_NAME, "tF2Cxc")
    top_10_results = [result.text for result in search_results[:10]]

    # Close the webdriver
    driver.quit()

    return top_10_results

# Example usage:
keyword = "Chelsea FC"
top_10_results = get_top_10_search_results(keyword, headless=True)
for idx, result in enumerate(top_10_results, 1):
    print(f"{idx}. {result}")

print('You dun now cuz!')