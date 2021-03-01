import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from match import match
import numpy as np
import json

class LeagueStats:

    """
        This class is used to select a soccer league and generate the url list of its next matches.
    """

    sourceURL = "https://www.soccerstats.com/"
    league_id   = ""                                                # Contains the league initials       
    league_url  = "https://www.soccerstats.com/latest.asp?league="  # Contains the specific league URL, initialize with an URL that will be concatenate
    next_matches_urls = []                                          # List with the URL of the next matches of the league
    num_matches = 0                                                 # Contain the number of matches that will be analyzed
    match_list = []

    # ================= Methods =================

    def gen_next_matches(self):
        # Method that generates the list of next matches URLs

        option = Options()
        option.headless = True
        driver = webdriver.Firefox(options = option)

        driver.get(self.league_url)
        

        # Interpreting HTML data
        element = driver.find_element_by_css_selector(
                ".eight > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1)") # Select matches table
        html_content = element.get_attribute('outerHTML')                                                                   
        soup = BeautifulSoup(html_content,'html.parser')

        # Getting href table
        href_table_matches = []
        for a in  soup.find_all("a", class_="vsmall", text="stats"):
            href_table_matches.insert(self.num_matches, a['href'])
            self.num_matches = self.num_matches + 1

        # Generating URL table
        for i in range(0, self.num_matches):
            self.next_matches_urls.insert(i, self.sourceURL + href_table_matches[i])

        driver.quit()

    def percent_to_float(self, s):
        s = s[:-1]
        s = float(s)
        s = s/100

        return s

    def gen_stats(self):
        # Get game stats
        
        for i in range(0, self.num_matches):
            # Debug
            tmp_match = match()

            driver = webdriver.Firefox()
            driver.get(self.next_matches_urls[i])
            time.sleep(4)
            
            # Accepting Cookies
            driver.find_element_by_css_selector(".css-flk0bs").click()
            time.sleep(1)

        #== Getting Team Names
            
          
            

        #== Getting Games Played

            element = driver.find_element_by_css_selector(".five > table:nth-child(3)")
            html_content = element.get_attribute("outerHTML")
            soup = BeautifulSoup(html_content, "html.parser")
            table = soup.find(name="table")

            df = pd.read_html(str(table))[0]
            df = df.to_dict()

            aux_a = list( df[1].items() )
            np.delete(aux_a, 0, 1)
            aux_b = list( df[6].items() )
            np.delete(aux_b, 0, 1)

            tmp_match.games_played_a = []
            tmp_match.games_played_a.insert(0, int(aux_a[2][1]))
            tmp_match.games_played_a.insert(0, int(aux_a[1][1]))

            tmp_match.games_played_b = []
            tmp_match.games_played_b.insert(0, int(aux_b[2][1]))
            tmp_match.games_played_b.insert(0, int(aux_b[1][1]))
            
        #==

        #== Getting Goals Table

            # Accessing table
            element = driver.find_element_by_css_selector(".five > table:nth-child(17)")
            html_content = element.get_attribute("outerHTML")
            
            # Interpreting table
            soup = BeautifulSoup(html_content, "html.parser")
            table = soup.find(name="table")

            # Estruturando o Data Frame
            df = pd.read_html(str(table))[0]
            titles = list(df)
            titles.remove(2)
            df = df[titles]

            # Tratamento de dados
            tmp = df.to_numpy()

            tmp_a = np.delete(tmp, 2, 1)
            tmp_a = np.delete(tmp_a, 2, 1)

            tmp_b = np.delete(tmp, 0, 1)
            tmp_b = np.delete(tmp_b, 0, 1)

            # Swap Columns
            tmp_b[:,[0, 1]] = tmp_b[:,[1, 0]]

            tmp_match.goals_table_a = tmp_a
            tmp_match.goals_table_b = tmp_b

            #Convert str to float
            for j in range(1, 6):
                tmp_match.goals_table_a[j][0] = float(tmp_match.goals_table_a[j][0])
                tmp_match.goals_table_a[j][1] = float(tmp_match.goals_table_a[j][1])


                tmp_match.goals_table_b[j][0] = float(tmp_match.goals_table_b[j][0])
                tmp_match.goals_table_b[j][1] = float(tmp_match.goals_table_b[j][1])

            for j in range(6, 14):
                tmp_match.goals_table_a[j][0] = self.percent_to_float(tmp_match.goals_table_a[j][0])
                tmp_match.goals_table_a[j][1] = self.percent_to_float(tmp_match.goals_table_a[j][1])


                tmp_match.goals_table_b[j][0] = self.percent_to_float(tmp_match.goals_table_b[j][0])
                tmp_match.goals_table_b[j][1] = self.percent_to_float(tmp_match.goals_table_b[j][1])
            
        #====
            driver.quit()
            self.match_list.append(tmp_match)
            del tmp_match

    def __init__(self, id):
        # Inicializer

        self.league_id = id
        self.league_url = self.league_url + id
        self.gen_next_matches()
        self.gen_stats()