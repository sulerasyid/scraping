# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

# create webdriver object
driver = webdriver.Chrome(ChromeDriverManager().install())

# get google.co.in
driver.get('https://www.linkedin.com/login')

# Enter your email address and password
driver.find_element_by_id('username').send_keys('your_email@example.com')
driver.fin
driver.find_element_by_id('password').send_keys('your_password')
# Submit the login form
driver.find_element_by_css_selector('.login__form_action_container button').click()