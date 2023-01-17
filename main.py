from fastapi import FastAPI, Header, HTTPException
from datetime import datetime
from functools import wraps
from currency_exchange_provider import XeCurrencyExchange

app = FastAPI()

# Default API Key
API_KEY = 'zaki@shake.io'

# list to store previous conversions as alternate of Database
conversions = []

# Specify currency exchange provider
CurrencyExchangeProvider = XeCurrencyExchange


# Custom decorator to check the api_key
def protected(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        api_key = kwargs.get('api_key')
        if api_key != API_KEY:
            raise HTTPException(
                status_code=401,
                detail='Unauthorized: Invalid API key provided. Please provide a valid API key to access this resource.'
            )
        return await func(*args, **kwargs)

    return wrapper


@app.get('/convert')
@protected
async def convert_currency(amount: float, from_currency: str, to_currency: str, api_key: str = Header(None)):
    '''
    This endpoint converts the amount from one currency to another using the mid-market rate
    based on conversion formula  converted_amount = amount * (to_currency_rate/from_currency_rate)
    '''

    # Get the latest updated rates
    rates = CurrencyExchangeProvider.get_rates()

    # Conversion formula
    converted_amount = amount * (rates[to_currency] / rates[from_currency])

    conversion_details = {
        'converted_amount': converted_amount,
        'rate': rates[to_currency] / rates[from_currency],
        'metadata': {
            'time_of_conversion': str(datetime.now()),
            'from_currency': from_currency,
            'to_currency': to_currency
        }
    }
    conversions.append(conversion_details)
    return conversion_details


@app.get('/currencies')
@protected
async def get_supported_currencies(api_key: str = Header(None)):
    '''
    This endpoint returns a dictionary containing all supported currencies
    '''
    supported_currencies = CurrencyExchangeProvider.get_supported_currencies()
    return supported_currencies


@app.get('/history')
@protected
async def get_conversion_history(api_key: str = Header(None)):
    '''
    This endpoint returns a list of all previous conversions
    '''
    return conversions
