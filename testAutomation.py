from selenium import webdriver

from login import Login


driver = webdriver.Firefox()
driver.get("http://www.amazon.in/")

driver.find_element_by_xpath("//div[@id='nav-tools']//a//span[@class=contains(.,'Hello. Sign in')]").click()

login = Login(driver)
login.username("akshayanilsharma9@hotmail.com")
login.password("kqp901S8*")
