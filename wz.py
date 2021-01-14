from selenium import webdriver
from time import sleep
import os
import pandas as pd 

class CodTracker():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/headless/webdriver/chromedriver')

    def get_basics(self):
        try:
            self.driver.get('https://cod.tracker.gg/warzone/profile/psn/'+os.getenv('USER')+'/matches')
        except:
            exit(1)

        sleep(3)
        cod_tracker_date_list            = []
        cod_tracker_games_per_day_list   = []
        cod_tracker_match_placement_list = []
        cod_tracker_mode_list            = []
        cod_tracker_time_list            = []
        cod_tracker_kills_list           = []
        cod_tracker_damage_list          = []
        cod_tracker_match_link_list      = []
        
        for i in range(1, 31):
            
            try:
                button = "//button[contains(., 'Load More Matches')]"
                login_btn = self.driver.find_element_by_xpath(button)
                login_btn.click()
                print('click ' + str(i))
                sleep (2)
            except:
                print("couldn't find ", i)
                sleep (1)
                pass
        
        for day in range(1,12):
            print(day)
            cod_tracker_date                = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/div/div[2]/div['+str(day)+']/div[1]/h3').text.split('\n')[0]
            cod_tracker_games_per_day       = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/div/div[2]/div['+str(day)+']/div[1]/h3').text.split('\n')[1]
            
            print(cod_tracker_games_per_day, cod_tracker_date)
            for match in range(1,int(cod_tracker_games_per_day)+1):
                cod_tracker_match_placement = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/div/div[2]/div['+str(day)+']/div[2]/div['+str(match)+']/div/div[1]').text
                cod_tracker_mode            = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/div/div[2]/div['+str(day)+']/div[2]/div['+str(match)+']/div/div[2]/div[1]/span[1]').text
                cod_tracker_time            = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/div/div[2]/div['+str(day)+']/div[2]/div['+str(match)+']/div/div[2]/div[1]/span[2]').text
                cod_tracker_kills           = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/div/div[2]/div['+str(day)+']/div[2]/div['+str(match)+']/div/div[3]/div[1]/div/div[1]/span[2]').text
                cod_tracker_damage          = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/div/div[2]/div['+str(day)+']/div[2]/div['+str(match)+']/div/div[3]/div[3]/div/div[1]/span[2]').text
                #https://cod.tracker.gg/warzone/match/<match ID>?handle=<username>
                cod_tracker_match_link      = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[2]/div/div[2]/div['+str(day)+']/div[2]/div['+str(match)+']/div/a').get_attribute("href").split('/')[-1].split('?')[0]    

                print(cod_tracker_mode, cod_tracker_match_placement, cod_tracker_time, cod_tracker_kills, cod_tracker_damage, cod_tracker_match_link)
                cod_tracker_date_list.append(cod_tracker_date)
                cod_tracker_games_per_day_list.append(cod_tracker_games_per_day)
                cod_tracker_match_placement_list.append(cod_tracker_match_placement)
                cod_tracker_mode_list.append(cod_tracker_mode)
                cod_tracker_time_list.append(cod_tracker_time)
                cod_tracker_kills_list.append(cod_tracker_kills)
                cod_tracker_damage_list.append(cod_tracker_damage)
                cod_tracker_match_link_list.append(cod_tracker_match_link)
        
        self.driver.quit()
        
        return cod_tracker_games_per_day_list, cod_tracker_date_list, cod_tracker_mode_list, cod_tracker_match_placement_list, cod_tracker_time_list, cod_tracker_kills_list, cod_tracker_damage_list, cod_tracker_match_link_list

class SbmmWz():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/headless/webdriver/chromedriver')

    def get_difficulty(self, lobbies):
        
        sbmm_match_difficulty_list = []
        sbmm_avg_kd_list = []
        sbmm_median_kd_list = []
        
        for lobby in lobbies:
            
            self.driver.get('https://sbmmwarzone.com/lobby/'+lobby)
            
            sleep(1.5)
            
            try:
                sbmm_match_difficulty = self.driver.find_element_by_xpath('/html/body/app-root/app-lobby/div/div/div/div/div/div[1]/div[1]/div/div[2]').text
            except:
                sbmm_match_difficulty = 'NOT RANKED'
            
            try:
                sbmm_avg_kd           = self.driver.find_element_by_xpath('/html/body/app-root/app-lobby/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]').text
                sbmm_median_kd        = self.driver.find_element_by_xpath('/html/body/app-root/app-lobby/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div[2]').text
            except:
                sbmm_avg_kd           = '0'
                sbmm_median_kd        = '0'
            
            sbmm_match_difficulty_list.append(sbmm_match_difficulty)
            sbmm_avg_kd_list.append(sbmm_avg_kd)
            sbmm_median_kd_list.append(sbmm_median_kd)
            
            print(lobby, sbmm_match_difficulty, sbmm_median_kd, sbmm_avg_kd)
            
        return sbmm_match_difficulty_list, sbmm_avg_kd_list, sbmm_median_kd_list
            
            

ct = CodTracker()
cod_tracker_games_per_day_list, cod_tracker_date_list, cod_tracker_mode_list, cod_tracker_match_placement_list, cod_tracker_time_list, cod_tracker_kills_list, cod_tracker_damage_list, cod_tracker_match_link_list = ct.get_basics()

sbmm = SbmmWz()
sbmm_match_difficulty_list, sbmm_avg_kd_list, sbmm_median_kd_list = sbmm.get_difficulty(cod_tracker_match_link_list)

df = pd.DataFrame(list(zip(cod_tracker_games_per_day_list, cod_tracker_date_list, cod_tracker_mode_list, cod_tracker_match_placement_list, cod_tracker_time_list, cod_tracker_kills_list, cod_tracker_damage_list, cod_tracker_match_link_list, sbmm_match_difficulty_list, sbmm_avg_kd_list, sbmm_median_kd_list)), 
               columns =['cod_tracker_games_per_day', 'cod_tracker_date', 'cod_tracker_mode', 'cod_tracker_match_placement', 'cod_tracker_time', 'cod_tracker_kills', 'cod_tracker_damage', 'cod_tracker_match_link', 'sbmm_match_difficulty', 'sbmm_avg_kd', 'sbmm_median_kd'])

print(df)

df.to_csv('/app/summary.csv', index=False)