from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class JobPortalBot():
    def __init__(self):
        print("JOB PORTAL BOT")

        self.job = input("Position, competence or company (Android Developer) : ")
        self.city = input("City, state or postal code (European Union): ")
        self.scrolls = input("Number of scrolls that you want to do (1 scroll = 25 job searches): ")

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.set_window_size(1250, 750)
        self.driver.get("https://www.linkedin.com/jobs/search/")

        sleep(2)

    def look(self):
        sleep(5)

        pop_up = self.driver.find_element_by_xpath('//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]')
        pop_up.click()

        sleep(2)

        job_in = self.driver.find_element_by_xpath('/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input')
        job_in.send_keys(self.job)

        sleep(2)

        exit_button = self.driver.find_element_by_xpath('/html/body/div[1]/header/nav/section/section[2]/form/section[2]/button')
        exit_button.click()

        sleep(2)

        city_in = self.driver.find_element_by_xpath('/html/body/div[1]/header/nav/section/section[2]/form/section[2]/input')
        city_in.send_keys(self.city)

        sleep(2)

        ok = self.driver.find_element_by_xpath('/html/body/div[1]/header/nav/section/section[2]/form/button')
        ok.click()

        sleep(5)

        for i in range(1, int(self.scrolls)):
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

            sleep(2)

        list_names = self.driver.find_element_by_xpath('//*[@id="main-content"]/section/ul')
        jobs_name = list_names.find_elements_by_tag_name('li')
        names = [name.text for name in jobs_name if name.text != '']

        i = 0

        while i < len(names):
            names[i] = names[i].replace("\n", " | ")
            new_name = names[i].split(" | ")
            names[i] = ""
            names[i] = names[i] + new_name[0] + " | " + new_name[2]

            i = i + 1


        with open('jobs.txt', 'w') as f:
            f.write('\n'.join(names))

bot = JobPortalBot()
bot.look()