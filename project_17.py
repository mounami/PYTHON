import requests

print("Currency converter\n")

def get_exchange_rate(from_currency, to_currency):
    """_summary_

    Args:
        from_currency (_type_): _description_
        to_currency (_type_): _description_
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            rates = data["rates"].get(to_currency)
            return rates
        else:
            return None
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    
def convert_currency(amount, rate):
    """_summary_

    Args:
        amount (_type_): _description_
        rate (_type_): _description_
    """
    if rate is None:
        print("❌ Error: Unable to get exchange rate.")
        return None
    
    return amount * rate

print("Supported currencies: USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, SEK, NZD")

from_currency = input("Enter the from currency (e.g., USD): ").upper()
to_currency = input("Enter the to currency (e.g., EUR): ").upper()

amount = float(input(f"Enter the amount in {from_currency}: "))
rate = get_exchange_rate(from_currency, to_currency)

if rate:
    converted_amount = convert_currency(amount, rate)
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
else:
    print("❌ Error: Invalid currency code or unable to fetch exchange rate.")