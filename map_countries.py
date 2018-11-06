import re
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


rankings = pd.read_csv('data/fifa_ranking.csv')
rankings['rank_date'] = pd.to_datetime(rankings['rank_date'])
ranking_earliest_date = '2009-01-01'
rankings_after = rankings[rankings['rank_date'] > pd.to_datetime(ranking_earliest_date)]
fifa_teams = rankings_after.country_full.str.lower()
fifa_teams = fifa_teams.str.replace(r'[,.]','')
fifa_teams = set(fifa_teams)

country_mapping = {
'burma': 'myanmar',
'congo dem rep': 'congo dr',
'congo rep': 'congo',
'democratic republic of the congo': 'congo dr',
'kyrgyzstan': 'kyrgyz republic',
'ivory coast': "côte d'ivoire",
'north korea': 'korea dpr',
'são tomé and príncipe': 'são tomé e príncipe',
'sao tome and principe': 'são tomé e príncipe',
'south korea': 'korea republic',
'taiwan': 'chinese taipei',
'united kingdom': 'england',
'united koreans in japan': None,
'united states': 'usa',
}

def map_country(country_string):
    if country_string == None:
        return None
    country_string = country_string.lower()
    #get rid of punctuation
    country_string = re.sub(r'[,.]','', country_string.lower())
    if country_string in country_mapping.keys():
        return country_mapping[country_string]
    elif country_string in fifa_teams:
        return country_string
    else:
        match = process.extractOne(country_string, fifa_teams,  scorer=fuzz.token_set_ratio)
        if match[1] >= 80:
            return match[0]
        else: 
            print("Cannot map {}".format(country_string))
            return None

