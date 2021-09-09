from selenium import webdriver
from time import sleep
from random import random
from secrets import email, passwordF

class TinderBot():
    def __init__(self):
        print("TINDER BOT")
        print("Gettin ChromeDriver ...")

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.set_window_size(1250, 700)
        self.driver.get("https://www.tinder.com")

        sleep(2)

    def login(self):
        pop_up1 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        pop_up1.click()

        sleep(2)

        print("Trying to do the login")
        login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_btn.click()

        sleep(2)
        
        print("Facebook login")
        google = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        google.click()

        sleep(4)

        base_window = self.driver.window_handles[0]
        other_window = self.driver.window_handles[1]

        self.driver.switch_to.window(other_window)

        sleep(2)

        pop_up2 = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]')
        pop_up2.click()

        sleep(2)

        print("Email ...")
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)

        print("Password ...")
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(passwordF)

        sleep(2)

        print("Making the Login ...")
        log_in = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        log_in.click()

        sleep(5)

        self.driver.switch_to.window(base_window)

    def swipe(self):
        print("Swiping ...")
        
        sleep(5)

        pop_up1 = self.driver.find_element_by_xpath('//*[@id="c1564682258"]/div/div/div/div/div[3]/button[1]')
        pop_up1.click()

        sleep(2)

        pop_up2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
        pop_up2.click()

        sleep(2)

        like_count = 0
        dislike_count = 0
        n = 0

        while True:
            sleep(2)

            try:
                rand = random()

                if rand < 0.73:
                    like_count = like_count + 1
                    print('{}th like' .format(like_count))

                    self.like(n)

                    n = n + 1

                    sleep(1)
                else:      
                    dislike_count = dislike_count + 1
                    print('{}th dislike' .format(dislike_count))

                    self.dislike(n)

                    n = n + 1

                    sleep(1)
            except Exception:
                try:
                    self.pop_up()
                except Exception:
                    self.match()

    def like(self, n):
        if n == 0:
            like_click = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
            like_click.click()
        else:
            like_click = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
            like_click.click()
        
    def dislike(self, n):
        if n == 0:
            dislike_click = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
            dislike_click.click()
        else: 
            dislike_click = self.driver.find_element_by_xpath('//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
            dislike_click.click()

    def match(self): 
        print("Closing the match ...")
        match = self.driver.find_element_byxpath("/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button")
        match.click()

    def pop_up(self): 
        print("Closing a pop up ...")
        pop_up = self.driver.find_element_byxpath('/html/body/div[2]/div/div/div[2]/button[2]')
        pop_up.click()

bot = TinderBot()
bot.login()
bot.swipe()