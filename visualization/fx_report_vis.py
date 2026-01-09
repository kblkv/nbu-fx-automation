import matplotlib.pyplot as plt
import csv

def build_chart():
    dates = []
    rates = []

    # Read data from report
    with open('../reports/fx_report.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(row['Date'])
            rates.append(row['Rate'])

    # Set up graph
    plt.figure(figsize=(10, 5))
    plt.plot(dates, rates, marker='o', linestyle='-', color='b', label='USD')

    # Figure caption
    plt.title('Official NBU USD Exchange Rate')
    plt.xlabel('Date and Time')
    plt.ylabel('Rate (UAH)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Save graph
    plt.tight_layout()
    plt.savefig('../reports/rate_chart.png')
    print("Chart has been saved to reports/rate_chart.png")
    plt.show()

if __name__ == "__main__":
    build_chart()