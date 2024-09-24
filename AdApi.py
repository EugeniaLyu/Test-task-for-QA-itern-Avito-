import requests


class AdApi:
    #  Инициализация

    def __init__(self, url):
        self.url = url

    # Сохранить объявление:

    def save_ad(self, name, price, sellerId, contacts, likes, viewCount):
        sale = {
            "name": name,
            "price": price,
            "sellerId": sellerId,
            "statistics": {
                "contacts": contacts,
                "likes": likes,
                "viewCount": viewCount,
            },
        }
        my_headers = {}
        resp = requests.post(self.url + "/api/1/item", json=sale, headers=my_headers)
        return resp.json()

    # Получить объявление

    def get_ad(self, id):
        resp = requests.get(self.url + "/api/1/item/" + str(id))
        return resp.json()

    # Получить все объявления по продавцам:

    def get_ad_sellerId(self, sellerId):
        resp = requests.get(self.url + "/api/1/" + str(sellerId) + "/item")
        return resp.json()
