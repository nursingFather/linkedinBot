from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

EMAIL = "your email"
PASSWORD= "your password"

option = Options()
option.add_argument("--window-size=1420, 1200")

chrome_driver_path = r"C:\Users\Olu\Desktop\Data Analysis\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s, options=option)
driver.get("https://www.linkedin.com/jobs/search?keywords=junior%20data%20analyst&location=Deutschland&geoId=101282230&trk=guest_homepage-basic_jobs-search-bar_search-submit&position=1&pageNum=0")

log_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
log_in.click()

time.sleep(5)

driver.find_element(By.ID, "username").send_keys(EMAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

time.sleep(5)

# enter = driver.find_element(By.CSS_SELECTOR, 'div.jobs-s-apply span')
# enter.click()

job_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in job_list:
    job.click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a/div/div/li-icon/svg')
    driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card").click()
    driver.find_element(By.ID,"#urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3259320145,67705067,multipleChoice)").send_keys(EMAIL)


