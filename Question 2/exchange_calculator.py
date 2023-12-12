import requests
import time

App_ID ="46d329fc45404fe4957500c747ec693b"
link = f"https://openexchangerates.org/api/latest.json?app_id={App_ID}"

def get_exchange_rate():
    try:
        response = requests.get(link)
        data = response.json()
        zar = data["rates"]["ZAR"]
        nok = data["rates"]["NOK"]
        rating = zar/nok
        return rating
    except Exception as e:
        print(f"Error no rates: {e}")
        return None

if __name__ == "__main__":
    while True:
        rating = get_exchange_rate()
        
        if rating is not None:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{current_time} ZAR/NOK : R {rating:.2f}")
            
            time.sleep(10)