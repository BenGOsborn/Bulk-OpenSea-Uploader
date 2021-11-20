from selenium import webdriver
import os

class Uploader:
    def __init__(self):
        # Get the base directories
        bin_base = os.path.join(os.getcwd(), "bin")
        chromedriver_path = os.path.join(bin_base, "chromedriver");
        ext_path = os.path.join(bin_base, "metamask.crx");

        # Initialize the driver
        opt = webdriver.ChromeOptions()
        opt.add_extension(extension=ext_path)
        self.__driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opt)

    def connect(self):
        '''
        Connect to wallet. https://dev.to/ltmenezes/automated-dapps-scrapping-with-selenium-and-metamask-2ae9
        '''
        pass

    def __upload(self):
        '''
        Upload a single NFT to OpenSea.
        '''
        pass

    def close(self):
        self.__driver.close()

def main():
    pass

if __name__ == "__main__":
    main()