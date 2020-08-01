from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.amazon.in/")
driver.implicitly_wait(3)

#This is SignIn Function for Amazon Webpage
def Sign_In():   
    email = "email/mobile number"
    password = "password"
    driver.find_element_by_xpath('//*[@id="nav-link-accountList"]').click()
    driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="continue"]').click()
    driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="signInSubmit"]').click() 
	
#Function which opens the webpage of product and add it to cart
def Add_Product_To_Cart():
    product_url = "https://www.amazon.in/Samsung-Galaxy-Ocean-128GB-Storage/dp/B07HGGYWL6/ref=psdc_1805560031_t1_B07HGBMHTR"
    driver.get(product_url)
    driver.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()

#Function to verify that the product is added to cart
def View_Product_In_Cart():
    try:
        driver.find_element_by_xpath('//*[@id="attach-sidesheet-view-cart-button"]/span/input')
    except NoSuchElementException:
        driver.find_element_by_xpath('//*[@id="hlb-view-cart-announce"]').click()    
    driver.find_element_by_xpath('//*[@id="attach-sidesheet-view-cart-button"]/span/input').click()	

#Main function to call all functions 
def main():
    Sign_In()
    Add_Product_To_Cart()
    View_Product_In_Cart()
    
#To call main function
if __name__ == "__main__":
    main()