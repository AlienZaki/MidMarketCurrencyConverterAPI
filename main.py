from fastapi import FastAPI, Header
from datetime import datetime
from currency_exchange_provider import XeCurrencyExchange

app = FastAPI()

# list to store previous conversions as alternate of Database
conversions = []

# list of all supported currencies
CurrencyExchangeProvider = XeCurrencyExchange


@app.get("/convert")
def convert_currency(amount: float, from_currency: str, to_currency: str):
    """
    This endpoint converts the amount from one currency to another using the mid-market rate
    based on conversion formula  converted_amount = amount * (to_currency_rate/from_currency_rate)
    """

    # Get the latest updated rates
    rates = CurrencyExchangeProvider.get_rates()
    print(rates)

    # Conversion formula
    converted_amount = amount * (rates[to_currency]/rates[from_currency])

    conversion_details = {
        "converted_amount": converted_amount,
        "rate": rates[to_currency]/rates[from_currency],
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
    supported_currencies = CurrencyExchangeProvider.get_supported_currencies()
    return supported_currencies


@app.get("/history")
async def get_conversion_history():
    """
    This endpoint returns a list of all previous conversions
    """
    return conversions

