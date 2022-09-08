import requests

def get_exchange_rates():
    """
    Get data from the API
    Arguments: None
    Returns:
        A json object containing the rates
    """

    return requests.get("https://api.coingecko.com/api/v3/exchange_rates").json()