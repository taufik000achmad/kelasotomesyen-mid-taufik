from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

url1 = "https://www.tiket.com"
driver.get(url1)
title1 = driver.title

url2 = "https://www.tokopedia.com"
driver.get(url2)
title2 = driver.title

url3 = "https://www.orangsiber.com"
driver.get(url3)
title3 = driver.title

url4 = "https://demoqa.com/"
driver.get(url4)
title4 = driver.title

url5 = "https://automatetheboringstuff.com"
driver.get(url5)
title5 = driver.title

#loop
alltitle = [title1 , title2 , title3 , title4 , title5]
for title in alltitle:
    print(title)

driver.quit()


