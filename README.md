# Mid-Market Currency Converter API


A simple API to convert currency using mid-market rate with the help of external currency exchange provider (xe.com)

## Requirements

-   Python 3.10+
-   Docker & Docker Compose

## Getting Started

1.  Clone the repository
> git clone https://github.com/AlienZaki/MidMarketCurrencyConverterAPI.git

2. Navigate to the project directory
> cd MidMarketCurrencyConverterAPI

3. Build the Docker image and start the container
> docker-compose up --build

- Visit the API documentation at <http://localhost:8000/docs>

- The API is now running on [http://localhost:8000](http://localhost:8000/)

### API Key

Api key is `zaki@shake.io`, you can change it in `docker-compose.yml` file.

### Endpoints

-   `/convert` - This endpoint converts the amount from one currency to another using the mid-market rate
-   `/currencies` - This endpoint returns a dictionary containing all supported currencies
-   `/history` - This endpoint returns a list of all previously made conversions

### Note

-   You need to provide a valid api key to access the endpoints.
-   You can access the endpoint documentation by visiting `/docs` after running the application
-   The `conversions` history is stored in memory, so it will not persist after the application is closed.

Built With
----------

-   [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
-   [xe.com](https://www.xe.com/) - Currency Exchange Provider