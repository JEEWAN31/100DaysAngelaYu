from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
chrome_driver = "/Users/jeewanchandrajoshi/Development/chromedriver"

# driver = webdriver.Chrome(executable_path=chrome_driver)


# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python

# driver.close() # only one tab
#
# driver.quit()   # Delete the whole chrome page completly

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path=chrome_driver)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.in/AmazonBasics-Inverter-Frost-Free-Refrigerator-Silver/dp/B09RJY6NYS?ref_=Oct_DLandingS_D_edae4833_62")

x = driver.find_element(by="x_path", value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
print(x)
print("Done")
print(x.text)


# <span class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay" data-a-size="xl" data-a-color="base"><span class="a-offscreen">₹51,490.00</span><span aria-hidden="true"><span class="a-price-symbol">₹</span><span class="a-price-whole">51,490<span class="a-price-decimal">.</span></span><span class="a-price-fraction">00</span></span></span>