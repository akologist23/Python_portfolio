from bs4 import BeautifulSoup
import requests
from pprint import pprint

class AgencyEndpoints:
    def __init__(self):
        self.base_url = "https://open.gsa.gov/api/dap/#response-structure"

    def get_agency_endpoints(self):
        response = requests.get(self.base_url)
        web_page = response.text #returns html code
        soup = BeautifulSoup(web_page, "html.parser")
        #pprint(soup)

        location_marker = soup.find("h3", attrs={"id": "available-agencies"})
        table_cells = location_marker.find_all_next("td")
        agency_list = []
        for number in range(1, len(table_cells)+1, 3):
            try:
                agency_list.append(table_cells[number].text)
            except IndexError:
                pass
        return agency_list