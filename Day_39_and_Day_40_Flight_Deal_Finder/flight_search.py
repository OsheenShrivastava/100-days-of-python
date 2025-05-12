import requests

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self, Api_Key, Api_Secret):
        self.api_key = Api_Key
        self.api_secret = Api_Secret
        self._token = self._get_new_token()
        print(self._token)


    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        token_response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        token_result = token_response.json()
        final_token = token_result["access_token"]
        return final_token


    def Add_data_to_iataCode_row(self, sheet_data):
        for place in sheet_data:
            # print(place)
            city = place["city"]
            # print(city)

            headers = {
                "Authorization": f"Bearer {self._token}"
            }

            params = {
                "keyword": city,
                "max": "2",
                "include": "AIRPORTS",
            }

            iataCode_response = requests.get(url=f"{AMADEUS_IATA_ENDPOINT}", headers=headers, params=params)
            # print(f"Status code {iataCode_response.status_code}. Airport IATA: {iataCode_response.text}")

            try:
                iataCode_result = iataCode_response.json()
                place["iataCode"] = iataCode_result["data"][0]["iataCode"]
            except IndexError:
                print(f"IndexError: No airport code found for {city}.")
                return "N/A"
            except KeyError:
                print(f"KeyError: No airport code found for {city}.")
                return "Not Found"


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }

        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": 10,
        }

        flight_data_response = requests.get(url=FLIGHT_OFFERS_ENDPOINT, params=params, headers=headers)

        if flight_data_response.status_code != 200:
            print(f"check_flights() response code: {flight_data_response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            # print("Response body:", flight_data_response.text)
            return None

        return flight_data_response.json()