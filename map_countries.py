init_country_mapping = {
'Bahamas, The': 'Bahamas',
'Bosnia and Herzegovina': 'Bosnia-Herzegovina',
'Cape Verde Islands': 'Cape Verde',
#We have no political intentions with this assignment. Also Taiwan is not included in wikipedia data we scrapped
'China PR': 'China',
'Chinese Taipei': 'Taiwan',
'Congo, Dem. Rep.': 'Congo DR',
'Congo, Rep.': 'Congo',
#Apparently the two cote de ivoire use different characters. 
"Côte d'Ivoire": 'Ivory Coast',
"Côte d'Ivoire": 'Ivory Coast',
'Democratic Republic of the Congo': 'Congo DR',
'FYR Macedonia': 'Macedonia',
'Gambia, The': 'Gambia',
'IR Iran' : 'Iran',
'Kyrgyz Republic' : 'Kyrgyzstan',
'Myanmar': 'Burma',
'North Korea': 'Korea DPR',
'Republic of Ireland': 'Ireland',
'Republic of the Congo': 'Congo',
'Republic of Macedonia': 'Macedonia',
'St Kitts and Nevis': 'St. Kitts and Nevis',
'Saint Kitts and Nevis': 'St. Kitts and Nevis',
'Saint Lucia': 'St. Lucia',
'St Lucia': 'St. Lucia',
'Saint Vincent and the Grenadines': 'St. Vincent and the Grenadines',
'St Vincent and the Grenadines': 'St. Vincent and the Grenadines',
'São Tomé e Príncipe': 'Sao Tome and Principe',
'São Tomé and Príncipe': 'Sao Tome and Principe',
'São Tomé and Príncipe': 'Sao Tome and Principe',
'South Korea': 'Korea Republic',
'Timor-Leste': 'East Timor',
'The Gambia': 'Gambia',
#Scotland is not that good. Just map to England for now. 
'United Kingdom': 'England',
'United States': 'USA'

#no clue which virgin islands
#'US Virgin Islands': 'Virgin Islands'
}

country_mapping = {}
#lower case everything
for key,value in init_country_mapping.items():
    country_mapping[key.lower()] = value.lower()

def map_countries(rankings_country):
    rankings_country = rankings_country.lower()
    if rankings_country in country_mapping.keys():
        return country_mapping[rankings_country]
    return rankings_country