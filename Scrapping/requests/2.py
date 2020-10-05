import requests
from requests.exceptions import HTTPError, Timeout, TooManyRedirects

urls = ['https://api.github.com/','https://api.github.com/invalid', 'https://abc.gerald.com/']

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status() # Raises a HTTPError if url is invalid
                                    # Raises a Timeout exception if request times out
                                    # Raises TooManyRedirects if so
                                    # All exceptions in requests inherits from
                                        # requests.exception.RequestException
    except HTTPError as http_err:
        print(f'HTTP Error occured: {http_err}')
    except Timeout as timeout:
        print(f'Timeout Error occured: {timeout}')
    except TooManyRedirects as toomanyredirects:
        print(f'Too Many Redirects: {toomanyredirects}')
    except Exception as err:
        print(f'Other errors occured: {err}')
    else:
        print('Success!')
    

