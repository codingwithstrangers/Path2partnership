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
duration = 60

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

    #write to txt file (always write vs append)
    with open("All_viewers.txt",'w') as file:
        file.write('\n'.join(total_list))

    #read the files
    # def compare_files(file1, file2, output_file):
    #     with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as output:
    #         file1_names = set(f1.read().splitlines())
    #         file2_names = set(f2.read().splitlines())
        
    #     matching_names = file1_names.intersection(file2_names)
        
    #     for name in matching_names:
    #         output.write(name + '\n')

    # # Specify the file paths
    # file1_path = 'All_viewers.txt'
    # file2_path = 'the_strangest_racer.txt'
    # output_file_path = 'lurker_score.txt'

    # Compare the files and extract matching names
    # compare_files(file1_path, file2_path, output_file_path)

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
    with open("lurker_score.txt", "w") as file:
        for name in matching_names:
            file.write(f"{name}\n")

    #pause the loop 
    time.sleep(60)
    

driver.quit()