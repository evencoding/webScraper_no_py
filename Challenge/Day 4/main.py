import os
import requests

def start_over():
    answer = input("Do you want start over? y/n ")
    if(answer == "y"):
        check_online()
    elif(answer == "n"):
        print("k, Bye")
    else:
        print("That's not a vaild answer")
        start_over()

def check_online():
    os.system('cls')
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (separated by comma")
    url_arr = []
    url_arr = input().split(',')
    for i in range(0, len(url_arr)):
            if(".com" in url_arr[i]):
                url_arr[i] = url_arr[i].replace(" ", "")
                url_arr[i] = url_arr[i].lower()
            if("http://" not in url_arr[i] and ".com" in url_arr[i]):
                url_arr[i] = url_arr[i].replace(f"{url_arr[i]}", f"http://{url_arr[i]}")
    for i in range(0, len(url_arr)):
        if(".com" not in url_arr[i]):
            print(f"{url_arr[i]} is not a valid URL")
            break
        try:
            url = requests.get(url_arr[i])
        except:
            print(f"{url_arr[i]} is down!")
        else:
            if(url.status_code == 200):
                print(f"{url_arr[i]} is up!")
    start_over()

check_online()