import requests
from pprint import pprint


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, Username, Password, Flight_Deals_Sheet_Price_Endpoint):
        self.response = requests.get(url=Flight_Deals_Sheet_Price_Endpoint, auth=(Username, Password))
        self.response.raise_for_status()
        self.data = self.response.json()
        pprint(self.data)

    def put_request(self, sheet_data, Username, Password, Flight_Deals_Sheet_Price_Endpoint):
        for ID in sheet_data:
            row_id = ID["id"]
            params = {
                "price": {
                    "iataCode": ID["iataCode"]
                }
            }
            requests.put(url=f"{Flight_Deals_Sheet_Price_Endpoint}/{row_id}", json=params, auth=(Username, Password))


    def get_customer_emails(self, Username, Password, Users_Data_Sheet_Endpoint):
        email_response = requests.get(url=Users_Data_Sheet_Endpoint, auth=(Username, Password))
        email_response.raise_for_status()
        email_data = email_response.json()
        pprint(email_data)
        Final_email_data = email_data["users"]
        return Final_email_data