import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# Visit the URL
url = "https://test.sharebus.co/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# Navigate to login page by clicking the "Sign in" button
# login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Sign in"]')))
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.sb-btn-lg.sb-btn-secondary.rounded-pill.py-1.px-3.fw-normal')))
login_button.click()

# Login with email and password-----------------------------------------------------------------------
email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
email_input.send_keys("brainstation23@yopmail.com")

password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
password_input.send_keys("Pass@1234")

# submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Log in"]')))
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='col-12 mx-auto mt-4']")))
submit_button.click()

driver.implicitly_wait(5)
# ------------------------------------------------------------------------------------------------------
menu_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.p-dropdown-trigger-icon.pi.pi-chevron-down')))
menu_dropdown.click()

sharelead_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='sharelead']//div")))
sharelead_option.click()

# continue button after sharelead select
con_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                         ".btn.btn-primary.btn.btn-success.text-white.align-self-center.rounded-pill.fw-bolder.px-4.my-3.d-flex.justify-content-between.align-items-center.mt-3")))
con_button.click()
time.sleep(5)

share_bus = driver.find_element(By.XPATH, "//span[normalize-space()='Set up a Sharebus']")
# Scroll to the element using JavaScriptExecutor
driver.execute_script("arguments[0].scrollIntoView();", share_bus)
# Wait for 3 seconds
time.sleep(3)
# Click the element
share_bus.click()
time.sleep(3)


#Insert required Trips details and click "Continue" [Please use location address as: From="Oslo,Norway" and To="Kolbotn, Norway"]
from_input = driver.find_element(By.XPATH, "//input[@id='startPoint']")
from_input.send_keys("Oslo")
time.sleep(3)
from_input.send_keys(Keys.DOWN)
time.sleep(3)
from_input.send_keys(Keys.ENTER)

to_input = driver.find_element(By.XPATH, "//input[@id='destination']")
to_input.send_keys("Kolbotn")
time.sleep(3)
to_input.send_keys(Keys.DOWN)
time.sleep(3)
to_input.send_keys(Keys.ENTER)
time.sleep(3)

# scrolling----------------------------------------------------------------------------------------------------

scroll_down = driver.find_element(By.XPATH,"//label[@for='returnTripswitch']")
driver.execute_script("arguments[0].scrollIntoView();", scroll_down)
time.sleep(3)
scroll_down.click()
time.sleep(3)

driver.find_element(By.XPATH,"//input[@placeholder='Departure Date']").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[1]/td[7]/span").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div/form/div[1]/div[3]/div[1]/div[1]/div/div[2]/span/input").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='Continue']").click()
time.sleep(5)

driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//i[@class='fi fi-chevron-down']").click()
time.sleep(5)

n_element = driver.find_element(By.XPATH,"//span[normalize-space()='Continue']")
driver.execute_script("arguments[0].scrollIntoView();",n_element)
driver.find_element(By.XPATH, "//li[normalize-space()='NTNUI']").click()
time.sleep(5)
n_element.click()
time.sleep(3)


no_element = driver.find_element(By.XPATH,"//button[@class='btn gray-white-bg ship-gray btn-discount-size rounded-end']")
driver.execute_script("arguments[0].scrollIntoView();",no_element)
time.sleep(3)
no_element.click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='btn gray-white-bg ship-gray btn-discount-size rounded-end']").click()
driver.find_element(By.XPATH,"//button[@type='submit']")
time.sleep(3)


create_share_bus = driver.find_element(By.XPATH,"//span[normalize-space()='Create Sharebus']")
create_share_bus.click()
time.sleep(8)


driver.find_element(By.XPATH,"//div[contains(@class,'publish-sb ship-gray extended-light-green-bg text-start px-4 py-4 mt-3 rounded')]//button[contains(@class,'d-flex justify-content-center align-items-center')]").click()
time.sleep(5)

driver.find_element(By.XPATH,"//div[contains(@class,'col-sm-12 col-md-6 my-4')]//input[contains(@class,'form-control rounded')]").send_keys("pleasure Trip")
driver.find_element(By.XPATH,"//p[normalize-space()='Vacation']").click()
time.sleep(3)

preview_publish = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/form/div[5]/button/span[1]")
driver.execute_script("arguments[0].scrollIntoView();", preview_publish)
time.sleep(3)
preview_publish.click()
time.sleep(3)

driver.find_element(By.XPATH,"//span[normalize-space()='Publish']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//*[@id=\"app\"]/nav/div/ul/li[1]/button").click()
time.sleep(3)
