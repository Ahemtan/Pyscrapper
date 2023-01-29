from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image

PATH = 'PATH TO YOUR WEB DRIVER'

#init Your web driver
wd = webdriver.Chrome(PATH)


#function to scrape image
def scrape(wd, max_img, Weburls):
    url = Weburls
    wd.get(url)

    image_urls = set()

    while len(image_urls) < max_img:
        #                                  change class name here \/          
        images = wd.find_elements(By.CLASS_NAME, "attachment-shop_catalog")
        for image in images:
            if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                image_urls.add(image.get_attribute('src'))
                print(f"collected {len(image_urls)}" )
    return image_urls

#function to download images
def download(down_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = down_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")
        print("suceess")
    except Exception as e:
        print('Opps someting went wrong', e)



# to scrape use scrape(ws, 1, url to your web)

#run code
urls = scrape(wd, 1)
print(urls)


#download images
for i, url in enumerate(urls):
    download("uploads/", url, str(i) + ".jpg")

wd.quit()