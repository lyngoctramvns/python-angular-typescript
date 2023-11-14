from seleniumbase import BaseCase
from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By

passwordSite = '1'
productElement = "CardLink-template--16197650317472__product-grid-6791024148640"
quantityBoxID = 'Quantity-template--16197650514080__main'
productQuantity = 5



class SiteTest(BaseCase):
	def setUp(self): #setUp and super().setUp() will determine which action done before each test. The opposite is tearDown()
		super().setUp()
		self.driver = webdriver.Chrome()
		#open site
		self.open("https://test-tram-site-4.myshopify.com")
		#enter password, then click the button
		self.find_element("password", by="id", timeout=10).send_keys(passwordSite)
		self.click('button:contains("Enter")')	
	def test_pass_page(self):
		#Check the new url
		self.assert_url("https://test-tram-site-4.myshopify.com/")
		self.sleep(1)
	def test_catalog_page(self):
		self.open("https://test-tram-site-4.myshopify.com/collections/all")
		self.click(productElement, by="id", timeout=None)
		self.sleep(1)
	def test_product_page(self):
		self.open("")