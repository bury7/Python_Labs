import datetime as dt

import matplotlib.pyplot as plt
import pytz
import requests


def main() -> None:
    tz = pytz.timezone("Europe/Kiev")
    now = dt.datetime.now(tz)
    start_date = (now - dt.timedelta(days=7)).strftime("%Y%m%d")
    end_date = now.strftime("%Y%m%d")

    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode=eur&json"
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return
    except ValueError as e:
        print("Error parsing JSON:", e)
        return

    if not data:
        print("No data available for the given date range.")
        return

    exchange_dates = [dt.datetime.strptime(entry["exchangedate"], "%d.%m.%Y").astimezone(tz) for entry in data]
    exchange_rates = [entry["rate"] for entry in data]

    plt.figure(figsize=(10, 6))
    plt.plot(exchange_dates, exchange_rates, marker="o", linestyle="-", color="purple")
    plt.title("Euro to UAH Exchange Rate - Last 7 Days")
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate (UAH)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
