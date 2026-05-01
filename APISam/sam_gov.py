import requests
import os

SAM_GOV_URL_BASE = "https://api.gsa.gov/analytics/dap/v2.0.0/agencies/"

class SamSearch:
    def __init__(self):
        self._api_key = os.environ.get("API_KEY")
        self.response_code = None

    def search_all_visits(self, date_after = "2025-12-31", agency_name=None):
        gov_header = {
            "x-api-key": self._api_key,
        }

        gov_params = {
            # "limit": 100,
            # "page": 3,
            "after": date_after,
            # "before": "2020-12-31",
        }

        url = SAM_GOV_URL_BASE + agency_name + "/reports/site/data"

        response = requests.get(url, params=gov_params, headers=gov_header)
        self.response_code = response.status_code
        return response.json()

    def search_most_visits(self, agency_name=None, **kwargs):
        #Which date had the most visits this year?
        all_records = self.search_all_visits(agency_name)
        visit = 0
        final_records = []
        for record in all_records:
            if record["visits"] > visit:
                visit = record["visits"]
        for record in all_records:
            if record["visits"] == visit:
                final_records.append(record)
        return final_records
