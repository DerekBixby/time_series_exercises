import os
import math
from pprint import pprint

base_url = "https://swapi.dev/api/"

def get_people():

    ppl_url = base_url + "people/"

    page_results = []

    data1 = requests.get(ppl_url + "?page=1").json()

    number_of_people = data1['count']
    number_of_results = len(data1['results'])

    max_page = math.ceil(number_of_people / number_of_results)
    print(max_page)

    for i in range(max_page):
        ppl_pg = ppl_url + f"?page={i+1}"
        #print(ppl_pg)
        data = requests.get(ppl_pg).json()
        #print(data['results'])
        for r in range(len(data['results'])):
            person = data['results'][r]
            page_results.append(person)
    #pprint(page_results)

    ppl_df = pd.DataFrame(page_results)

def get_planets(): 
    planet_url = base_url + "planets/"

    while data['next'] != None:
        print(data['next'])
        response = requests.get(data['next'])
        data = response.json()
        planet_df = pd.concat([planet_df, pd.DataFrame(data['results'])], ignore_index=True)


def get_ships():
    ships_url = base_url + "starships/"

    while data['next'] != None:
    print(data['next'])
    response = requests.get(data['next'])
    data = response.json()
    starships_df = pd.concat([starships_df, pd.DataFrame(data['results'])], ignore_index=True)


def get_swapi_data(endpoint):
    """ 
    - creates a csv of input variable (endpoint) if one does not exist
        - if one already exists, it uses the existing csv 
        - outputs data as a dataframe.
    
    endpoint formatting: "planets"
    
    """
    
    base_url = "https://swapi.dev/api/"
    
    if os.path.isfile(f"{endpoint}.csv"):
        df = pd.read_csv(f"{endpoint}.csv", index_col=0)
        
    else:
        response = requests.get(base_url + endpoint + "/")
        data = response.json()
        df = pd.DataFrame(data['results'])
        
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv(f"{endpoint}.csv")
        
    return df

def swapi_merge(): 
    ppl_planet_ship_df = pd.merge(left=ppl_planet_df.explode('starships'),
        right=starship,
        left_on='starships',
        right_on='url',
        how='left', suffixes=['_ppl_plnt', '_ships'])
    return ppl_planet_ship_df

def get_germant(): 
    germany = pd.read_csv("https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv")

    return germany