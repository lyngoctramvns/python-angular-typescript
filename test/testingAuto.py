from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

passwordSite = '1'
productElementID = 'CardLink-template--16197650317472__product-grid-6791024148640'
quantityBoxID = 'Quantity-template--16197650514080__main'
productQuantity = 5

# Set driver options so that Chrome will not close after test end
driver_options = Options()
driver_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = driver_options)

# Documentation https://selenium-python.readthedocs.io/getting-started.html
# Install selenium by pip isntall selenium (or python<version> -m pip install selenium)
# https://googlechromelabs.github.io/chrome-for-testing/#stable Chrome webdriver download here!


driver.get("https://test-tram-site-4.myshopify.com/")
driver.implicitly_wait(8)
element = driver.find_element(By.ID, 'password')
element.send_keys(passwordSite)
button = driver.find_element(By.XPATH, '//button[text() = "Enter"]')
button.click()
driver.implicitly_wait(8)

# Enter the homepage
driver.get("https://test-tram-site-4.myshopify.com/collections/all")
productTest = driver.find_element(By.ID, productElementID)
productTest.click()
# Enter the product page
quantityTest = driver.find_element(By.ID, quantityBoxID)
quantityTest.clear()
quantityTest.send_keys(productQuantity)
div = driver.find_element(By.ID, "price-template--16197650514080__main")
div.click()
plusQuantity = driver.find_element(By.NAME, "plus")
plusQuantity.click()
