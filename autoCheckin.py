from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from win10toast import ToastNotifier

def startAutoCheckin(env):
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)

    url = "https://adalove.inteli.edu.br/feed"

    driver.get(url)

    email = env['EMAIL_ADALOVE']
    password = env['PASSWORD_ADALOVE']

    emailInput = driver.find_element(By.XPATH, '//*[@id=":r5:"]')
    emailInput.send_keys(email)

    passwordInput = driver.find_element(By.XPATH, '//*[@id=":r6:"]')
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.RETURN)

    time.sleep(15)

    checkinButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/header/ul/ul/li[1]/button').click()
    time.sleep(5)

    toaster = ToastNotifier()
    try:
        comfirmCheckin = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[6]/div/button[1]').click()
        toaster.show_toast("Sucesso!", "Checkin realizado com sucesso.", duration=10)
        time.sleep(10)
    except:
        # Retorno erros Adalove
        message = driver.find_elements(By.XPATH,"/html/body/div[5]/div[3]/div/div/div[2]/p/p")[0].text
        toaster.show_toast("Erro ao realizar o checkin!", message, duration=10)

    driver.quit()

