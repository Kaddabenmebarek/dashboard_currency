from datetime import date, datetime, timedelta
from pprint import pprint
import requests


def get_rates(currencies, since_days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=since_days)
    symbols = ','.join(currencies)
    req = f"https://www.docstring.fr/api/rates/history/?start_at={start_date}&end_at={end_date}&symbols={symbols}"
    r = requests.get(req)
    if not r and not r.json():
        return False, False

    all_rates = {currency: [] for currency in currencies}
    api_rates = r.json().get("rates")
    all_days = sorted(api_rates.keys())

    for each_day in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_day].items()]
        #print(api_rates[each_day].items())
        #print(api_rates.get(each_day))

    #pprint(all_rates)

    return all_days, all_rates


if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "CAD"])
    pprint(days)
    pprint(rates)
