from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

web = webdriver.Chrome()
web.get('https://astro.cafeastrology.com/natal.php')
print("Welcome to the birth chart report program!")
Name = input("What's your name? ")
Pronouns = input("Do you go by he, she, or they? ")
Birthday = int(input("What day were you born? (dd format) "))
Birthmonth = int(input("What month were you born? (mm format) "))
Birthyear = int(input("What year were you born? (yyyy format) "))
Birthhour = int(input("What hour were you born? (military time in form hr) "))
Birthminute = int(input("What minute were you born? (mn format). Enter -1 if unknown "))
Birthcity = input("What city were you born in? ")
Birthplace = input("What State and Country were you born in? (State, Country format) ")
NameElement = web.find_element(By.XPATH,
                               "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[1]/td/input[5]")
NameElement.send_keys(Name)
HeElement = web.find_element(By.XPATH,
                             "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[1]/td/input[6]")
SheElement = web.find_element(By.XPATH,
                              "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[1]/td/input[7]")
TheyElement = web.find_element(By.XPATH,
                               "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[1]/td/input[8]")
if Pronouns == "he":
    HeElement.click()
elif Pronouns == "she":
    SheElement.click()
elif Pronouns == "they":
    TheyElement.click()
BirthdayElement = web.find_element(By.XPATH,
                                   "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select[1]")
for x in range(Birthday - 1):
    BirthdayElement.send_keys(Keys.DOWN)
BirthmonthElement = web.find_element(By.XPATH,
                                     "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select[2]")
for x in range(Birthmonth - 1):
    BirthmonthElement.send_keys(Keys.DOWN)
BirthyearElement = web.find_element(By.XPATH,
                                    "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select[3]")
if Birthyear > 2000:
    for x in range(Birthyear - 2000):
        BirthyearElement.send_keys(Keys.DOWN)
elif Birthyear < 2000:
    for x in range(2000 - Birthyear):
        BirthyearElement.send_keys(Keys.UP)
elif Birthyear == 2000:
    BirthyearElement.send_keys(Birthyear)
BirthhourElement = web.find_element(By.XPATH,
                                    "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[3]/td/select[1]")
if Birthhour > 12:
    for x in range(Birthhour - 12):
        BirthhourElement.send_keys(Keys.DOWN)
elif Birthhour < 12:
    for x in range(12 - Birthhour):
        BirthhourElement.send_keys(Keys.UP)
elif Birthhour == 12:
    BirthhourElement.send_keys(Birthhour)
BirthminuteElement = web.find_element(By.XPATH,
                                      "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[3]/td/select[2]")
UnknownElement = web.find_element(By.XPATH,
                                  "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[3]/td/input")
if Birthminute == -1:
    UnknownElement.click()
else:
    for x in range(Birthminute):
        BirthminuteElement.send_keys(Keys.DOWN)
BirthcityElement = web.find_element(By.XPATH,
                                    "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[4]/td/table/tbody/tr/td/div/div[1]/input")
BirthcityElement.send_keys(Birthcity)
BirthplaceElement = web.find_element(By.XPATH,
                                     "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[4]/td/table/tbody/tr/td/div/div[1]/select")
web.implicitly_wait(20)
BirthplaceElement.send_keys(Birthcity + ", " + Birthplace)
Submit = web.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[5]/td/button")
Submit.click()
Chart = web.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/table")
print(Chart.text)
