from selenium import webdriver

driver = webdriver.Chrome()

# Documentation https://selenium-python.readthedocs.io/getting-started.html
# Install selenium by pip isntall selenium (or python<version> -m pip install selenium)
# https://googlechromelabs.github.io/chrome-for-testing/#stable Chrome webdriver download here!

driver.get("https://test-tram-site-4.myshopify.com/")
element = driver.find_element_by_id('password')