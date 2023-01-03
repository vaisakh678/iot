from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from urlextract import URLExtract


links = open("links.txt", "r").read()
ext = URLExtract()
links = ext.find_urls(links)

link = "https://www.tinkercad.com/login"
driver = webdriver.Chrome()
driver.get(link)

def extract_circuit(link):
    driver.get(link)
    while not driver.execute_script("return !! document.querySelector('.sitemenu__title__span')"):
        sleep(2)
    title = driver.execute_script("return document.querySelector('.sitemenu__title__span').innerHTML")
    driver.execute_script("localStorage.clear()")
    action = ActionChains(driver)
    action.key_down(Keys.META).send_keys('a').key_up(Keys.META).perform() # select all -- cmt + a
    action.key_down(Keys.META).send_keys('c').key_up(Keys.META).perform() # copy selected -- cmt + c
    circuit = driver.execute_script("return localStorage.getItem('circuitClipboard')")
    driver.execute_script("localStorage.clear()")
    return {
        "circuit": circuit,
        "title": title
    }

path = "/Users/vaisakh/programs/iot/compailer/circuits"
for link in links:
    res = extract_circuit(link)
    circuit  = res["circuit"]
    title = res["title"].replace("/", "-")
    print(title)
    open(f"{path}/{title}.txt", "w").write(circuit)

driver.quit()




