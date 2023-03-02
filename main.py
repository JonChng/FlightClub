import requests

ok = True

starting = "Welcome to Jonathan's Flight Club.\nWe find the best flight deals and email you."
first_name = input("What is your first name?")
last_name = input("What is your last name?")
email = input("What is your email?")
confirm_mail = input("Type your mail again.")

if email != confirm_mail:
  ok = False
  print("The email entered was incorrect.")

if ok == True:
  url = "https://api.sheety.co/{YOUR API KEY}/flightDeals/users"
  data = {
    'user':{
      "firstName":first_name,
      "lastName":last_name,
      "email":email
    }
  }
  response = requests.post(url=url, json=data)
  response.raise_for_status()
  print(response.text)
