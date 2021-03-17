from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from csv import writer



#path="/Users/gerd/Downloads/chromedriver"
#driver=webdriver.Chrome(path)

response=requests.get("https://www.klinikbewertungen.de/klinik-forum/erfahrung-mit-augenklinik-dr-hoffmann-braunschweig")

#driver.get("https://www.klinikbewertungen.de")
#search=driver.find_element_by_id("fwas")
#search.send_keys("Augenklinik Dr.Hoffmann")
#search.send_keys(Keys.RETURN)

soup=BeautifulSoup(response.text, "html.parser")

bewertungen=soup.find(class_="list ratinglist")
bewertung_title=soup.find(class_="list ratinglist").find_all(('h2').string)
bewertung_detail=bewertungen.find('p').string

print(bewertung_detail)

