from selenium import webdriver
from time import sleep
from random import random
from secrets import email, password
from beauty_predict import scores

import requests, os

ROOT = os.path.dirname(os.path.abspath(__file__))

class TinderBot():
    def __init__(self):
        print("TINDER BOT")

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.set_window_size(1250, 700)

        self.begining = True

        self.driver.get("https://www.tinder.com")

        sleep(2)

    def login(self):
        pop_up1 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        pop_up1.click()

        sleep(2)

        print("Trying to do the Facebook login")
        login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_btn.click()

        sleep(2)
        
        facebook = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        facebook.click()

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

        while n<50:
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
                    self.match()
                except Exception:
                    try:
                        self.pop_up()
                    except Exception:
                         print("Error: {}".format(err))

    def ai_swipe(self):
        n = 0            

        while n<50:
            sleep(2)

            try:
                n = n + 1

                self.choose(n)
            except Exception as err:
                try:
                    self.pop_up()
                except Exception:
                    try:
                        self.match()
                    except Exception:
                         print("Error: {}".format(err))

    def choose(self, n):
        scores = self.current_scores()
        choice = "DISLIKE"
        
        x = True
        i = 0
        
        while i<len(scores):
            for score in scores:
                # If there are several faces, they must all have better score than 6.5
                if score < 6.5:
                    x = False 
        
        if len(scrs) == 0:
            self.dislike(n)
        #elif [score > 6.5 for score in scores] == len(scores) * [True]: 
        elif x == True:
            self.like(n)  
            choice = "LIKE"
        else:
            self.dislike(n)

        print("Scores : ", scrs, " | Choice : ", choice)

    def current_scores(self):
        url = self.get_image_path()
        
        images_path = os.path.join(ROOT, 'images', os.path.basename(url))

        download_image(url, images_path)
        
        return scores(images_path)

    def get_image_path(self):
        body = self.driver.find_element_by_xpath('//*[@id="Tinder"]/body')
        bodyHTML = body.get_attribute('innerHTML')

        # Example: <div aria-label="NAME" class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox" style="background-image: url(&quot;https://url_from_imagers;); background-position: 49.4737% 0%; background-size: 117.431%;"></div>
        start_marker = '<div class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox" style="background-image: url(&quot;'
        end_marker = '&'

        if not self.begining:
            url_start = bodyHTML.rfind(start_marker)
            url_start = bodyHTML[:url_start].rfind(start_marker) + len(start_marker)
        else:
            url_start = bodyHTML.rfind(start_marker) + len(start_marker)

        self.begining = False

        url_end = bodyHTML.find(end_marker, url_start)

        return bodyHTML[url_start:url_end]

    def download_image(url, images_path):
        image_data = requests.get(url).content
        
        with open(images_path, 'wb') as out:
            out.write(image_data)

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

    def message(seld):
        print("Going to do some messaging")
        message_btn = self.driver.find_element_byxpath('//*[@id="c328424210"]')
        message_btn.click()

        while True:
            match = self.driver.find_element_by_class_name('matchListItem')

            if len(match) < 2:
                break

            match[0].click()
            
            sleep(1)

            try:
                message_text = self.driver.find_element_by_xpath('//*[@id="c-2060350467"]')
                message_text.send_keys('hola')

                sleep(1)

                send = self.driver.find_element_by_xpath('//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
                send.click()

                sleep(1)

                message_btn.click()
                
                sleep(2)
            except Exception as err:
                print("Error: {}".format(err))
                sleep(2)

bot = TinderBot()
bot.login()
bot.swipe()
bot.ai_swipe()
bot.message()