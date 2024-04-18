import datetime, time
from datetime import date
import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

print('>>> SOS Download Data Automated <<<')

def turn_on_driver(target_dir):
    
    preferences = {
        "download.default_directory": target_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    }

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--incognito')
    options.add_experimental_option("prefs", preferences)

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(20)
        
        return 0, driver
    except Exception as e:
        print('Chrome driver is cannot active - ', e)
        driver.quit()
        return 1

def automation(driver, url, username, password):
    try:
        print('>>> Access CAT SOS Web')
        driver.get(url)
        print('>>> Web opened')

        print(">>> Insert Username then submit")
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sign-in-name']"))).click()
        driver.find_element(By.ID, "sign-in-name").send_keys(username)
        driver.find_element(By.ID, "next").click()
    
        print(">>> Insert Password then submit")
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']"))).click()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "next").click()
        print('>>> Allhamdulillah logged in')
    
        print('>>> Accepting cookies')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='html']/body/div[1]/div/div/div/div[3]/button"))).click()
        print('>>> Cookies ting is done')

        print('>>> On to the Report Download...')
        
        print('>>> Accessing the donwload tab')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ui-view']/div/div[2]/ul/li[4]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ui-view']/div/div[2]/div/div[4]/div/div/div/div[3]/span"))).click()
        
        print('>>> Filling the download form...')
        
        print('>>> Filling the Start Date')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportForm']/div[1]/div[2]/div/s-template-form/div[1]/div/div[2]/s-date/div/input"))).click()
        driver.find_element(By.XPATH, "//*[@id='reportForm']/div[1]/div[2]/div/s-template-form/div[1]/div/div[2]/s-date/div/input").send_keys(start_date)
        
        print('>>> Filling the End Date')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportForm']/div[1]/div[2]/div/s-template-form/div[2]/div/div[2]/s-date/div/input"))).click()
        driver.find_element(By.XPATH, "//*[@id='reportForm']/div[1]/div[2]/div/s-template-form/div[2]/div/div[2]/s-date/div/input").send_keys(end_date)
        
        print('>>> Filling the Interp. type')
        sleep(3)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportForm']/div[1]/div[2]/div/s-template-form/div[3]/div/div[2]/div[1]/button"))).click()
        driver.implicitly_wait(60)
        interp_button = driver.find_element(By.XPATH, "//*[@id='html']/body/ul[2]/li[1]")
        # wait = WebDriverWait(driver, timeout=60)
        # wait.until(lambda d : interp_button.is_displayed())
        driver.find_element(By.XPATH, "//*[@id='html']/body/ul[2]/li[1]").click()

        print('>>> Filling the Overall interp')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportForm']/div[1]/div[2]/div/s-template-form/div[11]/div/div[2]/div[1]/button"))).click()
        driver.find_element(By.XPATH, "//*[@id='html']/body/ul[9]/li[1]").click()
        
        print('>>> Form has been filled')

        print('>>> Download file is starting now...')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportForm']/div[2]/button[1]"))).click()
        sleep(240)
        print(">>> Download finish!")

        return 0
    except Exception as e:
        print('> Error occured - ', e)
        return 1
    
def automation_2():
    print('>>> On to downloading Track Sample Report file..')
    try:
        print('>>> Clicking Track Your Sample tab')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ui-view']/div/div[2]/div/div[4]/div/div/div/div[5]/span"))).click()
        print('>>> Filling the Track Your Sample form...')
        print('>>> Filling the Start Date')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportForm']/div[1]/div[2]/div/s-template-form/div[1]/div/div[2]/s-date/div/input"))).click()
        driver.find_element(By.XPATH, "//*[@id='reportForm']/div[1]/div[2]/div/s-template-form/div[1]/div/div[2]/s-date/div/input").send_keys(start_date)
            
        print('>>> Filling the End Date')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportForm']/div[1]/div[2]/div/s-template-form/div[2]/div/div[2]/s-date/div/input"))).click()
        driver.find_element(By.XPATH, "//*[@id='reportForm']/div[1]/div[2]/div/s-template-form/div[2]/div/div[2]/s-date/div/input").send_keys(end_date)

        print('>>> Download Track Your Sample file is starting...')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reportForm']/div[2]/button[1]"))).click()
        sleep(30)
        print(">>> Download Track Your Samples Report has finished!")
        return 0
    except Exception as e:
        print('> Error occurred - ', e)
        return 1

if __name__ == "__main__":
    print('>>> Set up all variables..')
    ### Generating date ###
    today = datetime.date.today()
    today_dt = datetime.datetime.now()
    today_stf = today_dt.strftime("%m/%d/%Y")
    partition_date = today_dt.strftime("%Y%m%d")
    day_min_3_dt =  today_dt - datetime.timedelta(days=1)
    day_min_3_stf = day_min_3_dt.strftime("%m/%d/%Y")

    start_date = day_min_3_stf
    end_date = today_stf

    print(f'>>> Automate downloading SOS data from {start_date} to {end_date} - mm/dd/yy')

    username = "m.negara@petrosea.com"
    password = "Sepinggan@41"
    status = 0
    url = 'https://soswebmc.cat.com/cat-sos/reports'
    
    ### Target Directory ###
    ### Uncomment one to be used either Dev or Prod
    target_directory = "/app"
    expected_file = "/app/sample-extract.xlsx"

    # target_directory = "/home/ehazard/cobham/sos_scrapping/results"
    # expected_file = "/home/ehazard/cobham/sos_scrapping/results/sample-extract.xlsx"
    ###

    print('>>> Chorme driver activate..')
    is_active, driver = turn_on_driver(target_directory)

    if is_active == 0:
        print('>>> Chrome driver is active and running')
        is_automated = automation(driver, url, username, password)
        if is_automated == 0:
            print('>>> Checking the downloaded file...')
            created_datetime = os.path.getctime(expected_file)
            created_date = date.fromtimestamp(created_datetime)
            if created_date == today:
                print('>>> Downloaded file is found!')
                is_automted_2 = automation_2()

                if is_automted_2 == 0:
                    print('You dun now cuz!')
                else:
                    print('ERROR')
                
            else:
                print('> Downloaded file is not found!')
                print('> Please rerun the process..')
                status = 1
    else:
        exit()
