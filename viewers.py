from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
duration = 500

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
    racer_csv = "the_strangest_racer.csv"
# create first text file
    with open("All_viewers.txt", 'w') as file:
        lower_caseshit = '\n'.join(total_list).lower()
        file.write(lower_caseshit)
   
#compare each file
    with open("All_viewers.txt", 'r') as file1:
        All_viewers = file1.read().splitlines()
    with open(racer_csv, 'r')as file2:
        the_strangest_racer= file2.read().splitlines()

    #check booth list for match
    matching_names = set(All_viewers) & set(the_strangest_racer)

      # Write the matching names to the "lurker_score.txt" file
    with open("lurker_score.txt", "w") as file:
        for name in matching_names:
            file.write(f"{name}\n")

#point for lurkers
    get_lurker = 'lurker_score.txt'
    lurker_points = 'lurker_points.csv'


        # Read the existing names from the CSV file
    existing_names = {}

    with open(lurker_points, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >=2:
                existing_names[row[0]] = int(row[1])

    # Read the new names from the text file
    new_names = set()

    with open(get_lurker, 'r') as file:
        new_names.update(file.read().splitlines())

    # # Determine the names that are not already in the CSV file
    # unique_names = new_names - existing_names

    # Append the unique names to the CSV file
    with open(lurker_points, 'w', newline='') as file:
        writer = csv.writer(file)
        for name in existing_names:
            if name in new_names:
                existing_names[name] += 1 
            writer.writerow([name, existing_names[name]])

    #add the names and points to the csv
    with open (lurker_points, 'a', newline='') as file:
        writer = csv.writer(file)
        for name in new_names - existing_names.keys():
            writer.writerow([name, 1])

    
    time.sleep(60)
driver.quit()