import requests

class Searching:
    def __init__(self):
        self.base_url = 'https://api.warframestat.us' # url of the api site

    def search(self):
        query = input('Enter the name of the drop that you want to search for')
        search_response = requests.get(self.base_url + '/drops/search/' + query + '\n')

        if not search_response.json():
            print('Please check the spelling of your item!')

        if search_response.status_code == 404:
            print('Make sure that your query is an item!')


        