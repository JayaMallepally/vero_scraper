from bs4 import BeautifulSoup
import requests


url = "https://www.vero.fi/en/detailed-guidance/decisions/47405/tax-exempt-allowances-in-2023-for-business-travel/"
soup = BeautifulSoup(requests.get(url).content, "html.parser")

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
