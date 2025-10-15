 # 1 ЗАДАНИЕ
def bgpu_image() -> None:
    url = f"http://static-maps.yandex.ru/1.x/"
    params = {"apikey": f"f3a0fe3a-b07e-4840-a1da-06f18b2ddf13",
              "ll": "127.540927,50.256563",
              "spn": "0.004457,0.00219",
              "l": "map"}

    response = requests.get(url, params)

    if response:
        with open("map.png", "wb") as p:
            p.write(response.content)
            print('Изображение успешно сохранено!')
    else:
        print(f"Ошибка запроса: {response.status_code}")


bgpu_image()


# 2 ЗАДАНИЕ
def find_index(address: str) -> str:
    url = f'http://geocode-maps.yandex.ru/1.x/'
    params = {"apikey": f"8013b162-6b42-4997-9691-77b7074026e0",
              "geocode": f"{address}",
              "format": "json"}

    response = requests.get(url, params)

    if response:
        data = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        try:
            return data["metaDataProperty"]["GeocoderMetaData"]["Address"]['postal_code']
        except KeyError:
            return 'Индекс не найден!'
    else:
        return f"Ошибка запроса: {response.status_code}"


print(find_index('Москва Петровки, 38'))


# 3 ЗАДАНИЕ
def country_in_different_languages(cioc_code: str) -> None:
    url = f"https://restcountries.com/v3.1/alpha/{cioc_code.lower()}"

    response = requests.get(url)
    data = response.json()

    if response:
        country = data[0]

        print(f"Страна: {country['name']['common']}")
        print("Названия на разных языках:")

        try:
            for lang_code, name_data in country['translations'].items():
                print(f"{lang_code}: {name_data['common']}")
        except KeyError:
            print("Нет данных о названиях на других языках.")
    else:
        print(f"Ошибка запроса: {response.status_code}")


country_in_different_languages('kaz')
