from seleniumbase import BaseCase
from selenium import webdriver #Set a custom webdriver to open on Chrome
# Alternative: from seleniumwire import webdriver


class SiteTest(BaseCase):
	def test_pass_page(self):
		driver = webdriver.Chrome()
		self.driver = driver
		#open site
		self.open("https://test-tram-site-4.myshopify.com")
		#enter password, then click the button
		self.find_element("password", by="id", timeout=10).send_keys("1")
		self.click()
		#Check the new url
