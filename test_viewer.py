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
driver_path = "F:\Coding with Strangers\Path2partnership\16chromedriver-win64\chromedriver-win64\chromedriver.exe"

#headless
options = Options()
options.add_argument("--headless")

#create driver instance
driver = webdriver.Chrome(options=options)

#stream you want to monitor
stream = "https://www.twitch.tv/codingwithstrangers/chat"



#loop my shit duration of bot 
duration = 580

#this wipes file
# with open ('lurker_points.csv', 'w') as file:
#     pass

exe_file_path = '"F:\Coding with Strangers\Path2partnership\minimap\The Perfect Lurker.exe"'
try:
    # Open the executable file
    os.startfile(exe_file_path)
except Exception as e:
    print(f"Error: {e}")

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
    

    #vatiables for code
    import csv



#Part two of Code used to set up CSV
    racer_csv = "the_strangest_racer.csv"
    all_viewers = [item.lower() for item in total_list]
    lurker_points_csv = 'lurker_points.csv'
    
    # Reads and puts the perfect lurker into dict.
    racer_info = {}
    perfect_lurker = {}
    with open(racer_csv, 'r') as file:
        lines = csv.reader(file)
        racer_info = {l[0]: {'score': l[1], 'url': l[2]} for l in lines}
        perfect_lurker.update(racer_info)

    # Reads csv with points and makes it into dict.
    lurker_points = 'lurker_points.csv'
    existing_racers = {}
    with open(lurker_points, 'r') as file:
        reader = csv.reader(file)
        existing_racers = {l[0]: {'score': l[1], 'url': l[2]} for l in reader}
    
    # Step 3: Update existing racers with perfect lurker info
    
    keys_to_remove = []
    for key in existing_racers:
        if key not in perfect_lurker:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        existing_racers.pop(key)

    # Update existing racers and perfect lurker
    for key in perfect_lurker:
        if key in existing_racers:
            if key.lower() in all_viewers:
                existing_racers[key]['score'] = str(int(existing_racers[key]['score']) + 1)
        else:
            if key.lower() in all_viewers:
                perfect_lurker[key]['score'] = str(int(perfect_lurker[key]['score']) + 1)
            existing_racers[key] = perfect_lurker[key]
  
    # Write the updated scores back to the CSV file
    with open("lurker_points.csv", "w") as file:
        for name in existing_racers.keys():
            final_output = f"{name},{existing_racers[name]['score']},{existing_racers[name]['url']}"
            file.write(final_output + '\n')

    print("Scores have been updated and written to the file.")



    time.sleep(60)
# let print text info

driver.quit()