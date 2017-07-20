import requests, bs4, collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, units, loc')


def main():
    print_the_header()
    code = input('What zip code do you want the weather for? ')
    html = get_html_from_web(code)
    report = get_weather_from_html(html)
    display_weather_forecast(report)


def print_the_header():
    print('---------------------------------')
    print('          Weather App')
    print('---------------------------------')


def get_html_from_web(code):
    url = 'https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}'.format(code)
    response = requests.get(url)  # returns HTML to response variable. Can call response.text to see it
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # currenttemp = #curTemp span.wx-value
    # tempunit = #curTemp .wx-unit
    # currentcond = #curCond .wx-value
    # location = #location .city-nav-header
    location = soup.find(id='location').find(class_='city-nav-header').get_text().strip()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    units = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    location = cleanup_text(location)
    location = find_city_state_from_location(location)
    condition = cleanup_text(condition)
    units = cleanup_text(units)
    temp = cleanup_text(temp)
    report = WeatherReport(cond=condition, temp=temp, units=units, loc=location)
    return report


def find_city_state_from_location(location: str):  # :str is a type hint
    location = location.split('\n')[0]
    return location


def display_weather_forecast(report):
    print('The weather in {} is {} {} and {}'.format(report.loc, report.temp, report.units, report.cond))


def cleanup_text(text: str):
    if not text:
        return text
    text = text.strip()
    return text


if __name__ == '__main__':
    main()
