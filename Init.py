import time
from selenium import webdriver
from xml.dom import minidom
import xml.etree.cElementTree as ET
from datetime import datetime

def Translate(words, start, isIncreaseTimeout):
    obj = words
    start = start
    initIndex = start
    stop = len(words)
    currentIndex = 0
    try:
        for index, word in enumerate(obj[start:stop], start=start):            
            datetime_object = datetime.now()
            currentIndex = index
            print(str(currentIndex) + " - " + str(datetime_object))            
            elements3 = driver.find_elements_by_class_name('goog-textarea')
            elements3[0].click()    
            elements3[0].send_keys(word)            
            timeoutSec = 2                        
            time.sleep(timeoutSec)
            elements5 = driver.find_elements_by_id('kAz1tf')
            element6 = elements5[0].find_element_by_tag_name('span').get_attribute("innerHTML")
            translatedWords.append(element6)
            time.sleep(2)
            elements4 = driver.find_elements_by_class_name('wuXmqc')
            elements4[0].click()        
            time.sleep(1)
        root = ET.Element("languages")
        doc = ET.SubElement(root, "language")
        for index, word in enumerate(translatedWords, start=initIndex):
            ET.SubElement(doc, "languageT", id=str(index)).text = word
        tree = ET.ElementTree(root)
        tree.write("filename.xml", encoding="utf-8")
    except:
        print("ERROR "+ str(currentIndex))
        root = ET.Element("languages")
        doc = ET.SubElement(root, "language")
        for index, word in enumerate(translatedWords, start=initIndex):
            ET.SubElement(doc, "languageT", id=str(index)).text = word
        tree = ET.ElementTree(root)
        tree.write("filename.xml", encoding="utf-8")

words = []
translatedWords = []

mydoc = minidom.parse('language.xml')
items = mydoc.getElementsByTagName('english')

for elem in items:
    words.append(elem.firstChild.data.replace('\n', ' '))

driver = webdriver.Chrome()
driver.get('https://www.google.com/search?q=tradutor&oq=tradutor&aqs=chrome.0.69i59j0j0i433l2j0j0i433l2j0l3.1600j0j7&sourceid=chrome&ie=UTF-8')

time.sleep(1)
elements = driver.find_elements_by_class_name('DQEUec')
elements[1].click()

time.sleep(1)
elements2 = driver.find_elements_by_class_name('language_list_item')

for elem in elements2:
    nameLang = elem.get_attribute("innerHTML")
    if nameLang == "Vietnamita":
        elem.click()
        break
time.sleep(2)

Translate(words, 0, False)