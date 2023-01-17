from fastapi import FastAPI, Header
from datetime import datetime

app = FastAPI()

# list to store previous conversions as alternate of Database
conversions = []

# list of all supported currencies
currencies = {
    'USD': {
        'name': 'United States Dollar',
        'rate': 1.0
    },
    'AED': {
            'name': 'Dirhams',
            'rate': 3.6725
    },
    'EGP': {
        'name': 'Egyption Pound',
        'rate': 29.6540453288
    },
}


@app.get("/convert")
def convert_currency(amount: float, from_currency: str, to_currency: str):
    """
    This endpoint converts the amount from one currency to another using the mid-market rate
    based on conversion formula  converted_amount = amount * (to_currency_rate/from_currency_rate)
    """

    # Conversion formula
    converted_amount = amount * (currencies[to_currency]['rate']/currencies[from_currency]['rate'])

    conversion_details = {
        "converted_amount": converted_amount,
        "rate": currencies[to_currency]['rate']/currencies[from_currency]['rate'],
        "metadata": {
            "time_of_conversion": str(datetime.now()),
            "from_currency": from_currency,
            "to_currency": to_currency
        }
    }
    conversions.append(conversion_details)
    return conversion_details


@app.get("/currencies")
def get_supported_currencies():
    """
    This endpoint returns a dictionary containing all supported currencies
    """
    supported_currencies = {currency: currencies[currency]['name'] for currency in currencies.keys()}
    return supported_currencies


@app.get("/history")
async def get_conversion_history():
    """
    This endpoint returns a list of all previous conversions
    """
    return conversions

