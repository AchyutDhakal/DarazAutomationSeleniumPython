from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    # BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    options = Options()
    # options.binary_location = BRAVE_PATH
    options.add_argument("--start-maximized")
    # options.add_argument("--incognito")
    options.page_load_strategy = "eager"


    driver = webdriver.Chrome(options=options)
    return driver