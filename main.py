import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import telegram_msg

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    return driver

def check_checkbox(driver):
    try:
        checkbox = driver.find_element(By.ID, "condition")
        driver.execute_script("arguments[0].scrollIntoView();", checkbox)

        if not checkbox.is_selected():
            checkbox.click()

    except Exception as e:
        print("checkbox error: ", e)
        #telegram_msg.send_telegram_msg("checkbox error: " + str(e))

def go_to_booking_page(driver):
    try:
        button_xpath = "//*[@id='submit_Booking']/input[1]"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath)))\
        .click()
    
    except Exception as e:
        print("go to next page error: ", e)
        #telegram_msg.send_telegram_msg("go to next page error: " + str(e))

def check_availability(driver):
    try:
        # wait until the next page is loaded
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "header_Booking")))

        no_available_text = "Il n'existe plus de plage horaire libre pour votre demande de rendez-vous. Veuillez recommencer ultérieurement."
        if no_available_text in driver.page_source:
            return False
        else:
            print("potentially available slot")
            return True
    
    except Exception as e:
        print("check avalability error: ", e)
        #telegram_msg.send_telegram_msg("check avalability error: " + str(e))


if __name__ == "__main__":
    
    start_time = time.time()

    # url for appointment
    prefecture_domain =  "https://www.seine-saint-denis.gouv.fr/booking/create/"

    deposer_demande = prefecture_domain + "9636"
    renouvellement_rcpc = prefecture_domain + "16743"
    remise_titre = prefecture_domain + "17088"

    list_url = [deposer_demande, renouvellement_rcpc, remise_titre]
    list_url_name = ["deposer demande", "renouvellement rcpc", "remise titre"]

    # initialize Chrome driver
    chrom_driver = init_driver()

    # loop through the url while no available slot
    while True:
        for i, url in enumerate(list_url):
            
            chrom_driver.get(url)
            check_checkbox(chrom_driver)
            go_to_booking_page(chrom_driver)
            available = check_availability(chrom_driver)
            
            if available:
                msg = "maybe new slot available: " + list_url_name[i]
                telegram_msg.send_telegram_msg(msg)
                print(msg)
                break

            sleep_time = random.randint(20, 30)
            msg = list_url_name[i] + " no available slot, sleep for " + str(sleep_time)
            print(msg)
            time.sleep(sleep_time)
        
        # send a message to telegram every hour to check if the script is still running
        if time.time() - start_time > 60*60:
            telegram_msg.send_telegram_msg("mummy I am still running")
            start_time = time.time()