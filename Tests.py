import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

s = Service('/usr/local/bin/chromedriver')
chromeOptions = Options()
Options.headless = False

driver = webdriver.Chrome(service=s,options=chromeOptions)

driver.get("file:///Users/vishnu/PycharmProjects/Resolver_test/QE-index.html")

time.sleep(3)

#TEST 1
print('*************** TEST 1 ***************')
userName = driver.find_element(By.ID, 'inputEmail')
password = driver.find_element(By.ID, 'inputPassword')
signInButton = driver.find_element(By.XPATH, '//*[@id="test-1-div"]/form/button')

#assert the text input fields are displayed and placeholder matches
assert userName.is_displayed()
assert password.get_attribute("placeholder") == "Password"
#assert the signin button in enabled
assert signInButton.is_enabled()

userName.send_keys('abcd@gmail.com')
password.send_keys('01210')
print('Email Id & Password has been entered')
time.sleep(3)

#TEST2
print('*************** TEST 2 ***************')
list_group = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div/ul')

list_values = []
for e in list_group:
    list_values.extend(e.text.split('\n'))

#print(list_values)
#length of list
print('Number of Values in list : '+str(len(list_values)))
assert len(list_values) == 3

#gets item value and badge
def val(i):
    item_values = list_values[i].split(' ')
    badge = item_values.pop()
    item = ' '.join(item_values)
    return item, badge

#prints the 2nd list item value,change argument value for desired item in list group
print('The 2nd list item value :  '+val(1)[0])
#asserting the 2nd list item is " List Item 2"
assert val(1)[0] == 'List Item 2'

#prints the 2nd list item's badge value,change argument value for desired item in list group
print('The 2nd list badge value : '+val(1)[1])
#asserting the 2nd item's badge value is 6
assert val(1)[1] == '6'
time.sleep(3)

#TEST 3
print('*************** TEST 3 ***************')

dropdown_button = driver.find_element(By.ID, 'dropdownMenuButton')

#As this does not have a Options like a dropdown, treating it as button and click
#printing the default value of dropdown
print(dropdown_button.text)
#asserting the dropdown button text
assert dropdown_button.text == 'Option 1'
dropdown_button.click()
time.sleep(2)

dropdown_option3 = driver.find_element(By.XPATH, '//*[@id="test-3-div"]/div/div/a[3]')
dropdown_option3.click()
#print(dropdown_button.text)
print("3rd option for the dropdown selected")
#asserting the 3rd option has been selected
assert dropdown_button.text == 'Option 3'
time.sleep(3)

#TEST 4
print('*************** TEST 4 ***************')
enabledButton = driver.find_element(By.XPATH,'//*[@id="test-4-div"]/button[1]')
disabledButton = driver.find_element(By.XPATH,'//*[@id="test-4-div"]/button[2]')
print('The 1st button in Enabled & 2nd button is disabled')

#asserting the 1st button is enabled and 2nd button in disabled
assert enabledButton.is_enabled()
assert disabledButton.get_property('disabled')
time.sleep(3)

#TEST 5
print('*************** TEST 5 ***************')
#wating for the button to be available to be clicked
wait = WebDriverWait(driver, 30)
button5 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="test5-button"]')))
button5.click()

alert = driver.find_element(By.ID, 'test5-alert')
print('The Alert message pops up after button click')

#asserting the success message has been displayed
assert alert.text == 'You clicked a button!'
assert button5.get_property('disabled')
time.sleep(3)

#TEST 6
print('*************** TEST 6 ***************')
# Calculating the length of the rows and columns of the table
rows = len(driver.find_elements(By.TAG_NAME, 'tr'))
cols = len(driver.find_elements(By.TAG_NAME, 'th'))

#function to return the value at any cell in the grid
def cell_value(r,c):
    # check if the entered coordinates are within the range of the table
    if r >= rows or c >= cols:
        value = 'Please input valid coordinates !!!'
    else:
        # incrementing the r,c as the first row is header
        value = driver.find_element(By.XPATH, '//*[@id="test-6-div"]/div/table/tbody/tr[' + str(r + 1) + ']/td[' + str(c + 1) + ']').text
    return value

#printing the value of cell at (2,2)
print('The value of cell at (2,2) : '+cell_value(2, 2))
#asserting the value at (2,2)
assert cell_value(2, 2) == 'Ventosanzap'
time.sleep(3)
driver.quit()
print('*************** END ***************')










