from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import dotenv

class Uploader:
    def __init__(self):
        # Get the base directories
        bin_base = os.path.join(os.getcwd(), "bin")
        chromedriver_path = os.path.join(bin_base, "chromedriver")
        ext_path = os.path.join(bin_base, "metamask.crx")
        self.__METAMASK_URL = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"

        # Initialize the driver
        opt = webdriver.ChromeOptions()
        opt.add_extension(extension=ext_path)
        self.__driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opt)

        # Close the metamask popup and navigate back to the correct window
        sleep(2)
        self.__driver.switch_to.window(self.__driver.window_handles[0])
        self.__driver.close()
        self.__driver.switch_to.window(self.__driver.window_handles[0])


    def connect_metamask(self, seed_phrase: str, password: str):
        '''
        Connect to Metamask
        '''

        # Navigate to metamask screen
        self.__driver.get(f"{self.__METAMASK_URL}#initialize/welcome")
        sleep(1)

        # Skip through wallet setup screen
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]').click()
        sleep(0.5)

        # Enter wallet seed phrase and password
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input').send_keys(seed_phrase)
        self.__driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        self.__driver.find_element_by_xpath('//*[@id="confirm-password"]').send_keys(password)
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div').click()
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/button').click()
        sleep(2)

    def add_network(self, rpc_url: str, chain_id: int, preconfigured_network: int = None):
        '''
        Adds the specified network to Metamask and selects it
        '''

        # Go to the networks tab
        self.__driver.get(f"{self.__METAMASK_URL}#settings/networks")
        sleep(1)

        # Choose one of the preconfigured networks if specified
        if preconfigured_network == None:
            self.__driver.find_element_by_xpath('//*[@id="network-name"]').send_keys("Network")
            self.__driver.find_element_by_xpath('//*[@id="rpc-url"]').send_keys(rpc_url)
            self.__driver.find_element_by_xpath('//*[@id="chainId"]').send_keys(chain_id)
            self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div[7]/button[2]').click()
            preconfigured_network = 7

        # Select the network
        self.__driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div').click()
        self.__driver.find_element_by_xpath(f'//*[@id="app-content"]/div/div[2]/div/li[{preconfigured_network}]').click()
        sleep(2)

    def __upload(self):
        '''
        Upload a single NFT to OpenSea.
        '''
        pass

    def close(self):
        for window_handle in self.__driver.window_handles:
            self.__driver.switch_to.window(window_handle)
            self.__driver.close()

def main():
    # Initialize env variables
    dotenv.load_dotenv()
    seed_phrase = os.getenv("SEED_PHRASE")
    password = os.getenv("PASSWORD")

    uploader = Uploader()
    sleep(50)
    uploader.connect_metamask(seed_phrase, password)
    uploader.close()

if __name__ == "__main__":
    main()