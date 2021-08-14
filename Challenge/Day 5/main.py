import os
import requests
from bs4 import BeautifulSoup

def start():
  print("Hello! Please choose select a country by number:")
  for i in range(len(country_name)):
    print(f"# {i} {country_name[i]}")

def re_input():
  try:
    answer = int(input("#: "))
    if(0 <= answer < len(country_name)):
      print(f"You chose {country_name[answer]}")
      print(f"The currency code is {country_code[answer]}")
    else:
      print("Choose a number from the list.")
      re_input()
  except:
    print("That wasn't a number.")
    re_input()

os.system("clear")
url = "https://www.iban.com/currency-codes"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
country = soup.find_all("td")

country_name = []
country_code = []

index = 2
while(index <= len(country)):
  if(country[index].string != None):
    country_code.append(country[index].string)
  index += 4

for i in range(len(country)):
  if(i % 4 == 0):
    if(country[i+2].string != None):
      country_name.append(country[i].string)

start()
re_input()