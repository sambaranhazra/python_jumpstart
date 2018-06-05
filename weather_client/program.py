import bs4
import requests


def print_the_header():
    print('------------------')
    print('    WEATHER APP   ')
    print('------------------')


def get_html_from_web(zip_code):
    url = "http://www.wunderground.com/weather-forecast/{}".format(zip_code)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    soup.find()


def main():
    print_the_header()

    zip_code = input("What zip code do you want weather for?")
    print(zip_code)

    html = get_html_from_web(zip_code)

    get_weather_from_html(html)
    print('Hello from main')


if __name__ == '__main__':
    main()
