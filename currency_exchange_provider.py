from abc import ABC, abstractmethod
import requests


class CurrencyExchangeProvider(ABC):
    """
    Abstract class for Currency Converter Website, it defines the method of getting currency conversion rates
    """

    @staticmethod
    @abstractmethod
    def get_supported_currencies() -> dict:
        """
        Returns the all supported currencies.
        """
        pass

    @staticmethod
    @abstractmethod
    def get_rates() -> dict:
        """
        Returns the conversion rate for all supported currencies.
        """

        pass


class XeCurrencyExchange(CurrencyExchangeProvider):

    @staticmethod
    def get_supported_currencies() -> dict:
        r = requests.get('https://www.xe.com/_next/data/5Ut5PpnbbM4siii4BIOC2/en/currency.json')
        currencies = r.json()['pageProps']['commonI18nResources']['currencies']['en']
        currencies = {currencies[currency]['name']: currency for currency in currencies}
        return currencies

    @staticmethod
    def get_rates() -> dict:
        headers = {'authorization': 'Basic bG9kZXN0YXI6akZiaFcyQWJvMU13VFQ0T2hDSDR1TUttT3pCUnY0ZmI='}
        r = requests.get('https://www.xe.com/api/protected/midmarket-converter/', headers=headers)
        rates = r.json()['rates']
        return rates


# if __name__ == '__main__':
#     xe = XeCurrencyExchange()
#     print(xe.get_supported_currencies())
#     print(xe.get_rates())
