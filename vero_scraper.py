from bs4 import BeautifulSoup
import requests
import json
import re


# url = "https://www.vero.fi/en/detailed-guidance/decisions/47405/tax-exempt-allowances-in-2023-for-business-travel/"
url = "https://www.vero.fi/en/detailed-guidance/decisions/47405/tax-exempt-allowances-in-2024-for-business-travel/"
soup = BeautifulSoup(requests.get(url).content, "html.parser")

match = re.match(r".*([1-3][0-9]{3})", url)
year = match.group(1) if match.group is not None else ""
print(year)

rows = []


tables = soup.findAll("table")
for table in tables:
    if table.findParent("table") is None:
        rows.append(table)

country_allowance_table = rows[2]
country_allowance_list = []
country_allowance_dict = {}

for row in country_allowance_table.findAll("tr"):
    cells = [td.getText(strip=True) for td in row.findAll("td")]
    country_allowance_list.append(cells)


for country_allowance in country_allowance_list:
    if len(country_allowance) > 0:
        country_allowance_dict[country_allowance[0]] = country_allowance[1]
# print(country_allowance_list)
print(country_allowance_dict)

with open(f"allowance_country_{year}.json", "w", encoding="utf-8") as f:
    json.dump(country_allowance_dict, f, ensure_ascii=False, indent=4)
