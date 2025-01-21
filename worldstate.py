import requests # import the requests

class WorldState:
    def __init__(self):
        self.base_url = 'https://api.warframestat.us' # url of the api site

    def archon(self):
        archon_response = requests.get(self.base_url + '/pc/en/archonHunt')
        nodeList = []
        for i in range(3):
            nodeList.append(archon_response.json()['missions'][i]['nodeKey'] + ' - ' + archon_response.json()['missions'][i]['typeKey'])

        print('Archon: ' + archon_response.json()['boss'])
        for i in nodeList:
            print(i)

        print('Expires: ' + archon_response.json()['expiry'].replace('T', ' ').replace('.000Z', ' ') + '\n')

    def cambion(self):
        cambion_response = requests.get(self.base_url + '/pc/en/cambionCycle')
        print('Current Cambion Cycle: ' + cambion_response.json()['state'].upper() + '\nTime Left in Current Cycle: ' + cambion_response.json()['timeLeft'] + '\n')

    def cetus(self):
        cetus_response = requests.get(self.base_url + '/pc/en/cetusCycle')
        print('Current Cetus Cycle: ' + cetus_response.json()['state'].upper() + '\nTime Left in Current Cycle: ' + cetus_response.json()['timeLeft'] + '\n')
            
    def orb_vallis(self):
        vallis_response = requests.get(self.base_url + '/pc/en/vallisCycle')
        if vallis_response.json()['isWarm']:
            print('Current Vallis Temperature: Warm' + '\nTime Left: ' + vallis_response.json()['timeLeft'])
        else:
            print('Current Vallis Temperature: Cold' + '\nTime Left: ' + vallis_response.json()['timeLeft'])

    def lith(self):
        lith = requests.get(self.base_url + '/pc/en/fissures')
        lithList = []

        for i in range(9):
            lithList.append(lith.json()[i]['node'] + ' - ' + lith.json()[i]['missionType'] + ' - ' + lith.json()[i]['tier'] + ' - ' + lith.json()[i]['eta'])
        print(lithList)
