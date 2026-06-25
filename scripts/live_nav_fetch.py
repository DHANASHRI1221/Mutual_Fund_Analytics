import requests
import pandas as pd
from pathlib import Path

schemes = {

    "HDFC_Top100_Direct":125497,
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841

}

output_folder = Path("../data/raw")

for name, code in schemes.items():

    print(f"Downloading {name}...")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        df.to_csv(output_folder/f"{name}.csv", index=False)

        print(f"{name} saved.")

    else:

        print("Failed:", name)