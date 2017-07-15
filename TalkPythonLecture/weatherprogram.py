
def main()
    print_the_header()
    #get zipcode from user
    code = input('What zip code do you want the weather for? ')
    #get html from web
    get_html_from_web(code)
    #parse html
    #display forcast
    print('hello from main')


def print_the_header():
    print('---------------------------------')
    print('          Weather App')
    print('---------------------------------')

def get_html_from_web(code):
    url = 'https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}'.format(code)


if __name__ == '__main__':
    main()