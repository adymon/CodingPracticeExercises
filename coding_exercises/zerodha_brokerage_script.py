from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


option = Options()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))

driver.get("https://zerodha.com/brokerage-calculator#tab-equities")

buy_price = driver.find_element(By.CSS_SELECTOR, 'input[class="opt_bp options"]')
sell_price = driver.find_element(By.CSS_SELECTOR, 'input[class="opt_sp options"]')
qty = driver.find_element(By.CSS_SELECTOR, 'input[class="opt_qty options"]')
btn = driver.find_element(By.CSS_SELECTOR, 'button[id="opt_ecn"]')

buy = [
       ]

sell = [


        ]

qt = [


       ]

for i in range(0, len(buy)):
    buy_price.clear()
    buy_price.send_keys(buy[i])
    sell_price.clear()
    sell_price.send_keys(sell[i])
    qty.clear()
    qty.send_keys(qt[i])

    btn.click()


