import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


"""option = Options()
option.headless = True

profile = webdriver.FirefoxProfile()
user_agent = "Mozilla/5.0 (Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
profile.set_preference("general.useragent.override", user_agent)

driver = webdriver.Firefox(
    firefox_profile=profile,
    options=option,
    executable_path=GeckoDriverManager().install(),
)"""

url = 'https://fbref.com/pt/jogadores/72d0e1b6/gabriel-barbosa'

driver.get(url)
time.sleep(5)

element = driver.find_element(By.ID,'scout_summary_FW')
html_content = element.get_attribute("outerHTML")
soup = BeautifulSoup(html_content, "html.parser")

dtfs = pd.read_html(html_content)
df = pd.DataFrame(dtfs[0])
#pd.set_option("display.max_rows", df.shape[0] + 1)
print(df)

