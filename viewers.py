from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import chromedriver_autoinstaller

#path to webdriver
driver_path = "F:\Coding with Strangers\Path2partnership\chromedriver_win32\chromedriver.exe"

#headless
options = Options()
options.add_argument("--headless")

#create driver instance
driver = webdriver.Chrome(executable_path=driver_path,options=options)

#stream you want to monitor
stream = "https://www.twitch.tv/codingwithstrangers/chat"

#loop my shit duration of bot 
duration = 180

#the loop
for i in range(duration):
    #go to site using driver
    driver.get(stream)

    #dict
    total_list = []
    

    #selenium code starts
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div[2]/div[2]/button'))
    )

    button.click()
    users = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/section/div/div[6]/section/div/div[2]/div[2]/div[3]/div/div/div[4]/div[2]'))
    )
    #sets up list to get and store vip viewers and mods
    total_list.extend(users[0].text.split('\n'))
    
    #this adds mods to viewer list
    moderators = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/section/div/div[6]/section/div/div[2]/div[2]/div[3]/div/div/div[2]/div[2]')
    
    total_list.extend(moderators.text.split('\n'))
    
    #this adds vips to viewer list 
    vips = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/section/div/div[6]/section/div/div[2]/div[2]/div[3]/div/div/div[3]/div[2]')
    
    total_list.extend(vips.text.split('\n'))

    #prints List of total viewers 
    print(total_list)

    # Convert elements of total_list to lowercase
    lowercase_list = [item.lower() for item in total_list]

    # Write lowercase_list to a text file
    with open("All_viewers.txt", 'w') as file:
        file.write('\n'.join(lowercase_list))
   
#cmpare each file
    with open("All_viewers.txt", 'r') as file:
        All_viewers = file.read().splitlines()
    with open("the_strangest_racer.txt", 'r')as file:
        the_strangest_racer= file.read().splitlines()

    #check booth list for match
    lurker_score = {}

    matching_names = []

    #check if names are matching 
    for viewer in All_viewers:
        if viewer in the_strangest_racer:
            matching_names.append(viewer)


    # Write the matching names to the "lurker_score.txt" file
    with open("lurker_score.csv", "w") as file:
        for name in matching_names:
            file.write(f"{name.lower()}\n")

    #pause the loop 
    time.sleep(60)
    

driver.quit()