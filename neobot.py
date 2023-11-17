from selenium import webdriver # version 4.3.0
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from time import sleep
from datetime import datetime
# import chrome_options as options
from selenium.webdriver.common.action_chains import ActionChains
import os

os.environ['WDM_LOCAL'] = '1'
os.environ['WDM_SSL_VERIFY'] = '0'


# TODO: set up functionality for running certain parts of the function at dif times of day
# Example: computer executes this file at a certain time
# The program will not close until it completes all of the function calls inside
#TODO: Inventory management when inventory gets too full

class NeoBot:
    def __init__(self, un, pw):
        self.un = un
        self.pw = pw
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        options = selenium.webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        # self.driver = webdriver.Chrome(chrome_options=options service=ChromeService(ChromeDriverManager().install()))
        self.driver = webdriver.Chrome(chrome_options=options, service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        self.driver.get("http://www.neopets.com/login/")
        sleep(2)

        self.driver.find_element("id", "loginUsername").send_keys(un)
        self.driver.find_element("id", "loginPassword").send_keys(pw)
        self.driver.find_element("id", "loginButton").click()
        sleep(4)

        #TODO
        # exit bot with message if login unsuccessful

        # put method calls here
        self.bank_interest()
        self.coltzan()
        self.fruit_machine()
        self.anchor_management()
        self.trudy_surprise()
        self.advent_calendar()
        self.close_bot()

    def bank_interest(self):
        self.driver.get("https://www.neopets.com/bank.phtml")
        sleep(2)

        try:
            self.driver.find_element('xpath', '//*[@id="frmCollectInterest"]/input[3]').click()
            print("Interest collection success")
        except:
            print("Bank interest collection failed")

    def coltzan(self):
        self.driver.get("https://www.neopets.com/desert/shrine.phtml")
        sleep(1)
        try:
            approach_shrine = self.driver.find_element('xpath', '/html/body/div[3]/div[3]/table/tbody/tr/td[2]/div[2]/div/form[1]/input[2]')
            # ActionChains(driver).move_to_element(driver.sl.find_element_by_id('my-id')).perform()
            ActionChains(self.driver).move_to_element(approach_shrine).perform()
            self.driver.execute_script("arguments[0].click();", approach_shrine)
            print("Coltzan's shrine success")
        except:
            print("Coltzan shrine failed")

    def tombola(self):
        self.driver.get("https://www.neopets.com/island/tombola.phtml")
        sleep(2)

        closed = str(self.driver.find_element('xpath', '//*[@id="container__2020"]/center/p/b').text)
        if "Closed. Back in an hour or so" in closed:
            print("Tombola is closed")
            return

        try:
            play = self.driver.find_element('xpath', '//*[@id="container__2020"]/center/form/input')
            self.driver.execute_script("arguments[0].click();", play)
            print("Tombola success")
        except:
            print("Tombola failed")

    def fruit_machine(self):
        self.driver.get("https://www.neopets.com/desert/fruit/index.phtml")
        sleep(2)

        try:
            play = self.driver.find_element('xpath', '//*[@id="content"]/table/tbody/tr/td[2]/div[2]/form/input[3]')
            self.driver.execute_script("arguments[0].click();", play)
            sleep(10)
            print("Fruit machine success")
        except:
            print("Fruit machine failed")

    def forgotten_shore(self):
        # causing problems with invalid xpath selector for text
        self.driver.get("https://www.neopets.com/pirates/forgottenshore.phtml")
        sleep(2)

        text_maybe = self.driver.find_element('xpath', '//*[@id="content"]/table/tbody/tr/td[2]/center/text()[1]')
        print(text_maybe)
        if text_maybe != "A deserted shore stretches along in front of you, but there's nothing of interest to be found today.":
            print("Something is probably in the forgotten shore. Double check")
            return

        try:
            # should work *if* the treasure is an a link
            self.driver.find_element('xpath', '//*[@id="shore_back"]/a').click()
            print("Found item on forgotten shore!!")
        except:
            print("Nothing in forgotten shore")

    def anchor_management(self):
        self.driver.get("https://www.neopets.com/pirates/anchormanagement.phtml")
        sleep(2)

        try:
            self.driver.find_element('xpath', '//*[@id="btn-fire"]/a').click()
            print("anchor success")
        except:
            print("anchor fail")

    def trudy_surprise(self):
        self.driver.get("https://www.neopets.com/trudys_surprise.phtml")
        # Get play button into view - browser size 574 x 638
        # sleep(2)

    def advent_calendar(self):
        # Note: This function is optimized for PST
        today = datetime.today()
        if today.month == 12:
            print("It's advent time! :D")
            try:
                self.driver.get("https://www.neopets.com/winter/adventcalendar.phtml")
                advent_button = self.driver.find_element("xpath", "/html/body/div[14]/form/button")
                ActionChains(self.driver).move_to_element(advent_button).perform()
                self.driver.execute_script("arguments[0].click();", advent_button)
                print("worked?")
            except Exception as e:
                print("Getting advent link failed", repr(e))

        else:
            print("It is not advent season")

    def close_bot(self):
        print("Bot closing")
        self.driver.quit()
