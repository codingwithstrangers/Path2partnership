from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import csv
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
duration = 380

#this wipes file
# with open ('lurker_points.csv', 'w') as file:
#     pass

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
    print('the total list',total_list)
    

    #make a func that opens csv and puts it in to a dict
    racer_csv = "the_strangest_racer.csv"
    all_viewers = [item.lower() for item in total_list]
    lurker_points_csv = 'lurker_points.csv'
   
    def open_csv ():
    # create first text file
        with open("All_viewers.txt", 'w') as file:
            lower_caseshit = '\n'.join(total_list).lower()
            file.write(lower_caseshit)

    
        racer_info = {}
        perfect_lurker = {}
        existing_lurker = {}
        with open (racer_csv,'r') as file:
            lines = csv.reader(file)
            racer_info ={l[0]: l[1] for l in lines}
            perfect_lurker.update(racer_info)
            # print('perfect_lurker')
            # print(perfect_lurker)
        
        existing_lurker = {key: value for key, value in perfect_lurker.items() if key.lower() in all_viewers}
        # print('the existing lurkers', existing_lurker) 

        lurker_points = 'lurker_points.csv'
        with open(lurker_points, 'r') as file:
            reader = csv.reader(file)
            existing_racers = {l[0]: {'score':l[1],'url':l[2]} for l in reader}

        #add score and combine dict for final 
        
        # for racer in existing_lurker:
        #     score = int(existing_racers[racer]['score'])+1 if racer in existing_racers else 0
        #     lurker_score[racer] = {'score': score, 'url': racer_info.get(racer, '')}
        lurker_score = {}
        for racer in existing_lurker:
            if racer in existing_racers:
                score = int(existing_racers[racer]['score']) + 1
            else:
                if racer in racer_info:
                    score = +0
            lurker_score[racer] = {'score': score, 'url': racer_info.get(racer, '')}

     
        with open("lurker_points.csv", "w") as file:
            for name in lurker_score.keys():
                final_output = f"{name},{lurker_score[name]['score']},{lurker_score[name]['url']}"
                print('final output:', final_output)
                file.write(final_output + '\n')
    
    open_csv()
    time.sleep(60)
driver.quit()