from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os

class Uploader:
    def __init__(self, seed_phrase: str, passphrase: str):
        # Get the base directories
        bin_base = os.path.join(os.getcwd(), "bin")
        chromedriver_path = os.path.join(bin_base, "chromedriver")
        ext_path = os.path.join(bin_base, "metamask.crx")

        # Initialize the driver
        opt = webdriver.ChromeOptions()
        opt.add_extension(extension=ext_path)
        self.__driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opt)

        # Connect to metamask
        sleep(2)
        self.__driver.switch_to.window(self.__driver.window_handles[0])
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]').click()

        sleep(0.5)
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input').send_keys(seed_phrase)
        self.__driver.find_element_by_xpath('//*[@id="password"]').send_keys(passphrase)
        self.__driver.find_element_by_xpath('//*[@id="confirm-password"]').send_keys(passphrase)
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div').click()
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/button').click()

    def __upload(self):
        '''
        Upload a single NFT to OpenSea.
        '''
        pass

    def close(self):
        self.__driver.close()

def main():
    uploader = Uploader("Hello world", "helloworld")
    sleep(50)
    uploader.close()

if __name__ == "__main__":
    main()