from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service()
driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome()
driver.get("https://google.com")

title = driver.title

driver.implicitly_wait(0.5)

# search_box = driver.find_element(by=By.NAME, value="q")
# search_button = driver.find_element(by=By.NAME, value="btnK")

# search_box.send_keys("Selenium")
# search_button.click()

# value = search_box.get_attribute("value")

driver.quit()
