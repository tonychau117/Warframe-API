import requests # allows us to get the information from the json file from the website
import keyboard as kb # key listener
from worldstate import *
from search import *
import time # allows us to use a counter to refresh the api

wf_key = '' # api key that we use
base_url = 'https://api.warframestat.us' # url of the api site
response = requests.get(base_url) # grabs the json code for us to see if it works or not

ws = WorldState() # allows us to access the worldstate menu/info

'''
while True:
    if kb.is_pressed('Esc'):
        print('Goodbye!')
        break
    else:
    
    # constant refreshing of the api to get the most accurate data

'''        # introduction when loading the program
print('Welcome to the Warframe API, choose a number to access the menu below or hit ESC to end')


'''
if kb.is_pressed('1'): 
    continue
elif kb.is_pressed('2'):
    continue
else:
    continue
'''

# world state retrieval [1.0 - 1.9]
    # archon hunt ✅
    # cambion drift ✅
    # orb vallis ✅
    # cetus  cycle ✅
    # deep archimedia X
    # fissures ✅
    # steel path datas
    # void trader

ws = WorldState()
ws.lith()

sh = Searching()
sh.search()
# WorldState.archon(base_url)


        

