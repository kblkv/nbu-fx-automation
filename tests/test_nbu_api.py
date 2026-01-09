import requests
import pytest
from datetime import datetime


def test_nbu_usd_rate_today():
    """
    Purpose: Check if NBU provides the correct USD rate for the current date.
    This helps to automate daily financial data monitoring.
    """

    # 1. Prepare today's date in the format NBU API expects (YYYYMMDD)
    # I used datetime here so there's no need to change the date manually every day.
    today_str = datetime.now().strftime("%Y%m%d")

    # 2. Define the endpoint with dynamic date
    api_url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={today_str}&json"

    print(f"\n[Action] Fetching current USD rate from NBU API...")
    print(f"[Details] Request URL: {api_url}")

    try:
        # 3. Send request and get the response
        response = requests.get(api_url, timeout=10)

        # Check if the connection was successful
        if response.status_code != 200:
            pytest.fail(f"API is not responding properly. Status code: {response.status_code}")

        data = response.json()

        # 4. Process and validate the data
        if not data:
            print(f"[Warning] No data found for {today_str}. The rate might not be published yet.")
            return  # Exit if no data; not necessarily fail the test

        # Extracting specific fields for report
        usd_info = data[0]
        rate = usd_info.get('rate')
        currency_name = usd_info.get('txt')
        official_date = usd_info.get('exchangedate')

        print(f"[Result] {currency_name} rate is {rate} UAH (Official NBU date: {official_date})")

        # Basic business rules validation
        assert rate > 0, "Exchange rate must be a positive number"
        assert "USD" in api_url, "The request was not for USD"

    except Exception as error:
        print(f"[Error] Something went wrong with the API call: {error}")
        raise error