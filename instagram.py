from selenium import webdriver
from time import sleep
from secrets import email, password, username

class InstagramBot():
    def __init__(self):
        print("INSTAGRAM BOT")

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.set_window_size(1250, 750)
        self.driver.get("https://www.instagram.com/?hl=pt")

        sleep(2)
    
    def login(self):
        # Closing Pop-Up
        pop_up = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]')
        pop_up.click() 

        print("Trying to do the login")
        print("Email ...")
        email_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input') 
        email_in.send_keys(email)

        print("Password ...")
        password_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_in.send_keys(password)

        sleep(4)

        print("Making the Login ...")
        log_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        log_in.click()

        sleep(4)

    def getProfile(self):
        # Closing Pop-Up 1
        pop_up1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        pop_up1.click() 

        sleep(4)

        # Closing Pop-Up 2
        pop_up2 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        pop_up2.click() 

        sleep(2)

        print("Going to your profile ...")
        profile = self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(username))
        profile.click() 

        sleep(2)

    def getFollowers(self, followers):
        followers_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_link.click() 

        sleep(2)

        print("Getting your followers names ...")
        followers = self.getNames(1)

        sleep(2)

        return followers

    def getFollowing(self, following):
        following_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following_link.click() 

        sleep(2)

        print("Getting your following names ...")
        following = self.getNames(2)

        sleep(2)

        return following

    def getNames(self, x):
        if x == 1:
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]")
        else:
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]")

        last_height = 0
        height = 1
        
        while last_height != height:
            last_height = height
            
            sleep(1)

            # JavaScript script to scroll all the scroll box, where the scroll_box is arguments[0]
            height = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", scroll_box)
        
        name_links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in name_links if name.text != '']
        
        close_button = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/button")
        close_button.click()
        
        return names

    def printNames(self, followers, following):
        notFollowingBack = [user1 for user1 in following if user1 not in followers]
        
        self.driver.close()

        print(notFollowingBack)

        with open('persons.txt', 'w') as f:
            f.write('\n'.join(notFollowingBack))

followers = []
following = []

bot = InstagramBot()
bot.login()
bot.getProfile()
followers = bot.getFollowers(followers)
following = bot.getFollowing(following)
bot.printNames(followers, following)