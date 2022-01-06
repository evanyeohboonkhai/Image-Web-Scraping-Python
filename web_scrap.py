import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome import options 
import time
import bs4
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.headless = True


# What you enter here will be searched for in
# Google Images
query = input("Keyword that want to search: ")


folder_name = "scrapped_img"
  
# Creating a webdriver instance
driver = webdriver.Chrome(chrome_options=options)
  
# Open Google Images in the browser
driver.get('https://images.google.com/')
  
# Finding the search box
# box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
box = driver.find_element(By.XPATH,'//*[@id="sbtc"]/div/div[2]/input')
  
# Type the search query in the search box
box.send_keys(query)
  
# Pressing enter
box.send_keys(Keys.ENTER)
  




def download_image(url, folder_name, num):

    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join(folder_name, query+"_"+str(num)+".jpg"), 'wb') as file:
            file.write(reponse.content)


# #Scrolling all the way up
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class':"isv-r PNCib MSM1fd BUooTd"} )

# print(len(containers))

len_containers = len(containers)

for i in range(1, len_containers+1):
    if i % 25 == 0:
        continue

    xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)

    previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
    previewImageElement = driver.find_element_by_xpath(previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")

    driver.find_element_by_xpath(xPath).click()

    #It's all about the wait

    timeStarted = time.time()
    while True:

        imageElement = driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img""")
        imageURL= imageElement.get_attribute('src')

        if imageURL != previewImageURL:
            #print("actual URL", imageURL)
            break

        else:
            #making a timeout if the full res image can't be loaded
            currentTime = time.time()

            if currentTime - timeStarted > 10:
                print("Timeout! Will download a lower resolution image and move onto the next one")
                break


    #Downloading image
    try:
        download_image(imageURL, folder_name, i)
        print("Downloaded element %s out of %s total. URL: %s" % (i, len_containers + 1, imageURL))
    except:
        print("Couldn't download an image %s, continuing downloading the next one"%(i))
