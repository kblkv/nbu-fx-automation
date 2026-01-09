import requests
import csv
import os
from datetime import datetime


def test_nbu_export():
    # Retrieve date
    today = datetime.now().strftime("%Y%m%d")
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={today}&json"

    # Retrieve data
    response = requests.get(url)
    data = response.json()

    # Specify fields
    rate = data[0]['rate']
    currency = data[0]['txt']
    date_for_report = datetime.now().strftime("%d.%m.%Y %H:%M")

    # Prepare report
    report_file = "reports/fx_report.csv"

    # Check existing file
    file_exists = os.path.isfile(report_file)

    with open(report_file, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)

        # If not exist, add column names
        if not file_exists:
            writer.writerow(["Date", "Currency", "Rate"])

        # Add row with data
        writer.writerow([date_for_report, currency, rate])

    # Validation
    assert rate > 0
    print(f"Success. Saved rate: {rate}")