import requests


def req_runner(list_of_urls, number_of_requests):
    for i in range(len(list_of_urls)):
        print("Request to " + list_urls[i])
        for j in range(number_of_requests):
            response = requests.get(list_of_urls[i])
            print(response.status_code)
            print(response.text)
            print()
        print("End of requesting to " + list_urls[i])


list_urls = [
    "https://www.avito.ru/",
    "https://www.w3schools.com/",
    "https://www.datacamp.com/",
    "https://skillbox.ru/",
    "https://yandex.ru/",
    "https://mipt.ru/",
    "https://mephi.ru/",
    "https://tproger.ru/",
    "http://spec-zone.ru/"
]
req_number = int(input())
req_runner(list_urls, req_number)
