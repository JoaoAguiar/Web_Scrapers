from selenium import webdriver
from time import sleep
from secrets import phone, password
from selenium.webdriver.common.keys import Keys
import random

class TwiterBot():
    def __init__(self):
        print("TWITER BOT")

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.set_window_size(1250, 750)
        self.driver.get("https://twitter.com/home?lang=pt_pt")

        sleep(2)

    def login(self):
        print("Trying to do the login")

        sleep(5)

        print("Phone ...")
        phone_in = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        phone_in.send_keys(phone)

        sleep(2)

        print("Making the Login ...")
        log = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        log.click()

        sleep(2)

        print("Password ...")
        password_in = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')
        password_in.send_keys(password)

        sleep(2)

        print("Making the Login ...")
        log_in = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        log_in.click()

        sleep(5)

    def look(self):
        pop_up = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div[2]')
        pop_up.click()

        print("Chose which keyword you want to look:")
        value = input()

        sleep(2)

        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]')
        search.click()

        sleep(2)

        search_keyword = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
        search_keyword.send_keys(value)
        search_keyword.send_keys(Keys.RETURN)

        sleep(5)

    def like(self):
        print("Lets start to do the like thing!")

        for i in range(1,3):
            sleep(5)

            hearts = self.driver.find_elements_by_xpath("//div[@data-testid='like']")

            sleep(5)

            for heart in hearts:
                random_prob = random.random()

                if random_prob >= 0.5:
                    heart.click()

                sleep(5)

            sleep(5)

bot = TwiterBot()
bot.login()
bot.look()
bot.like()

