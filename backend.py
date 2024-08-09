import requests
import urllib3

urllib3.disable_warnings()
OWM_API_KEY = '5c0be521628ced88241158b7b7122011'
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'


def get_data(city):
    params = {
        'q': city,
        'appid': OWM_API_KEY,
    }
    response = requests.get(url=OWM_ENDPOINT, params=params, verify=False)
    response.raise_for_status()
    return response.json()['list']


if __name__ == '__main__':
    d = get_data('London')
    print(d)
