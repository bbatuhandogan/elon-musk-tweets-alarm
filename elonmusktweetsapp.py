import time
import webbrowser
import winsound
import os
from datetime import datetime
from selenium import webdriver
from selenium import *
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
times = []

chrome_options = Options()
# chrome_options.add_argument("--headless")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)
today = datetime.now()
tdy = today.strftime('%Y-%m-%d %H:%M:%S')
tdy2 = str(tdy)
print(tdy2)

while True:
    try:
        driver.get("https://twitter.com/elonmusk/with_replies")
        try:
            element = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "//time")))
        except:
            print("//time konumu bulunamadi devam ediliyor")
        times = driver.find_elements_by_xpath("//time")
        if len(times) == 0:
            print("//time konumunda veri olmadigi icin tekrar taraniyor")
            continue
        thand = times[0].get_attribute('datetime')
        rcvd_dt = datetime.strptime(thand.split('.')[0], '%Y-%m-%dT%H:%M:%S')
        rcvd_str = str(rcvd_dt)
        if len(times) != 1:
            thand2 = times[1].get_attribute('datetime')
            rcvd_dt2 = datetime.strptime(thand2.split('.')[0], '%Y-%m-%dT%H:%M:%S')
            rcvd_str2 = str(rcvd_dt2)
        else:
            rcvd_str2 = "0000-00-00 00:00:00"
        print(datetime.now())
        if rcvd_str > tdy2 or rcvd_str2 > tdy2:
            os.startfile("alarm.mp3")
            webbrowser.open("https://twitter.com/elonmusk/with_replies")
            print("NEW TWEEET----------->")
            print(rcvd_str)
            print(rcvd_str2)
            print(datetime.now())
            for i in range(1, 15):
                winsound.Beep(2000, 200)
                winsound.Beep(3000, 200)
            break
        time.sleep(1.5)
    except:
        print("except'e dustu")
        winsound.Beep(1000, 200)
        driver.close()

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH, options=chrome_options)
        driver.get("https://twitter.com/elonmusk/with_replies")
