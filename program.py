import requests
import bs4
import collections

Weather = collections.namedtuple('Weather',
                                 'temp, scale, condition')


def header():
    print('---------------------------')
    print('----------weather----------')
    print('---------------------------')


def get_city_state():
    city = input('city: ').lower().split()
    state = input('state: ').lower()

    city = '-'.join(city)

    return city, state


def get_html(state, city):
    url = ('https://www.wunderground.com/weather/us/{}/{}'.format(state, city))

    response = requests.get(url)
    print(response.status_code)

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')

    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text().strip()
    condition = soup.find(class_='condition-icon').get_text().strip()

    return Weather(temp=temp, scale=scale, condition=condition)


def main():
    header()

    city, state = get_city_state()

    html = get_html(state, city)
    weather = get_weather_from_html(html)
    
    print('weather at {}, {} is {} {} and {}'.format(city, state, weather.temp, weather.scale, weather.condition))


if __name__ == '__main__':
    main()
