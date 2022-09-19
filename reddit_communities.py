from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

class RedditBot():
    def __init__(self):
        print("REDDIT BOT")

        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1 })

        self.driver = webdriver.Chrome(chrome_options=option, executable_path="chromedriver.exe")
        self.driver.set_window_size(1250, 750)
        self.driver.get("https://www.reddit.com/subreddits/leaderboard/")

        sleep(2)

    def getCommunities(self):
        pop_up = self.driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[3]/div[1]/section/div/section/section/form[2]/button')
        pop_up.click()

        sleep(5)

        for i in range(1,4):
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

            sleep(2)

        list_names = self.driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/ol')
        communities_name = list_names.find_elements_by_tag_name('li')
        names = [name.text for name in communities_name if name.text != '']

        j = 0

        while j < len(names):
            n = names[j].index("r")
            m = names[j].index("Aderir")
            name = names[j]
            names[j] = name[n:m-1]
            j = j + 1 
        
        with open('communities.txt', 'w') as f:
            f.write('\n'.join(names))

bot = RedditBot()
bot.getCommunities()