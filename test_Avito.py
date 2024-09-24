from AdApi import AdApi


api = AdApi("https://qa-internship.avito.com")


def test_get_one_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)

    # Сохраняем новое объявление продавца

    name = "Торшер"
    price = 42401
    contacts = 46
    likes = 4839
    viewCount = 74696
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    status = result["status"]
    ad_id = status[23:]

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление сохранилось(+1)

    assert len_after - len_before == 1

    # Обращаемся к сохраненному объявлению продавца по id объявления

    ad_id = api.get_ad(ad_id)
    assert ad_id[0]["name"] == name
    assert ad_id[0]["price"] == price
    assert ad_id[0]["sellerId"] == sellerId
    assert ad_id[0]["statistics"]["contacts"] == contacts
    assert ad_id[0]["statistics"]["likes"] == likes
    assert ad_id[0]["statistics"]["viewCount"] == viewCount


def test_get_two_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "lavalamp"
    price = 335392
    contacts = 312
    likes = 5
    viewCount = 0
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    status = result["status"]
    ad_id = status[23:]

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление сохранилось(+1)

    assert len_after - len_before == 1

    # Обращаемся к сохраненному объявлению продавца по id объявления

    ad_id = api.get_ad(ad_id)
    assert ad_id[0]["name"] == name
    assert ad_id[0]["price"] == price
    assert ad_id[0]["sellerId"] == sellerId
    assert ad_id[0]["statistics"]["contacts"] == contacts
    assert ad_id[0]["statistics"]["likes"] == likes
    assert ad_id[0]["statistics"]["viewCount"] == viewCount


def test_get_three_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "наушники"
    price = 528359964
    contacts = 192109
    likes = 542820
    viewCount = 6
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    status = result["status"]
    ad_id = status[23:]

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление сохранилось(+1)

    assert len_after - len_before == 1

    # Обращаемся к сохраненному объявлению продавца по id объявления

    ad_id = api.get_ad(ad_id)
    assert ad_id[0]["name"] == name
    assert ad_id[0]["price"] == price
    assert ad_id[0]["sellerId"] == sellerId
    assert ad_id[0]["statistics"]["contacts"] == contacts
    assert ad_id[0]["statistics"]["likes"] == likes
    assert ad_id[0]["statistics"]["viewCount"] == viewCount


def test_get_four_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "КАМЕРА"
    price = 70991249656
    contacts = 0
    likes = 648295481
    viewCount = 268537
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    status = result["status"]
    ad_id = status[23:]

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление сохранилось(+1)

    assert len_after - len_before == 1

    # Обращаемся к сохраненному объявлению продавца по id объявления

    ad_id = api.get_ad(ad_id)
    assert ad_id[0]["name"] == name
    assert ad_id[0]["price"] == price
    assert ad_id[0]["sellerId"] == sellerId
    assert ad_id[0]["statistics"]["contacts"] == contacts
    assert ad_id[0]["statistics"]["likes"] == likes
    assert ad_id[0]["statistics"]["viewCount"] == viewCount


def test_get_five_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "плащ-палатка"
    price = 84
    contacts = 8
    likes = 37
    viewCount = 75
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    status = result["status"]
    ad_id = status[23:]

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление сохранилось(+1)

    assert len_after - len_before == 1

    # Обращаемся к сохраненному объявлению продавца по id объявления

    ad_id = api.get_ad(ad_id)
    assert ad_id[0]["name"] == name
    assert ad_id[0]["price"] == price
    assert ad_id[0]["sellerId"] == sellerId
    assert ad_id[0]["statistics"]["contacts"] == contacts
    assert ad_id[0]["statistics"]["likes"] == likes
    assert ad_id[0]["statistics"]["viewCount"] == viewCount


def test_get_six_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "Ни одного штриха не мог бы я сделать, а никогда не был таким большим художником, как в эти минуты."
    price = 3
    contacts = 2483
    likes = 0
    viewCount = 0
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    status = result["status"]
    ad_id = status[23:]

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление сохранилось(+1)

    assert len_after - len_before == 1

    # Обращаемся к сохраненному объявлению продавца по id объявления

    ad_id = api.get_ad(ad_id)
    assert ad_id[0]["name"] == name
    assert ad_id[0]["price"] == price
    assert ad_id[0]["sellerId"] == sellerId
    assert ad_id[0]["statistics"]["contacts"] == contacts
    assert ad_id[0]["statistics"]["likes"] == likes
    assert ad_id[0]["statistics"]["viewCount"] == viewCount


def test_get_seven_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "lava лампа"
    price = 7902.61
    contacts = 0
    likes = 0
    viewCount = 0
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500
    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0


def test_get_eight_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "Торшер"
    price = 0
    contacts = 46
    likes = 4839
    viewCount = 74696
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    status = result["status"]
    ad_id = status[23:]

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление сохранилось(+1)

    assert len_after - len_before == 1

    # Обращаемся к сохраненному объявлению продавца по id объявления

    ad_id = api.get_ad(ad_id)
    assert ad_id[0]["name"] == name
    assert ad_id[0]["price"] == price
    assert ad_id[0]["sellerId"] == sellerId
    assert ad_id[0]["statistics"]["contacts"] == contacts
    assert ad_id[0]["statistics"]["likes"] == likes
    assert ad_id[0]["statistics"]["viewCount"] == viewCount


def test_get_nine_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "КАМЕРА"
    price = 70991249656
    contacts = 0
    likes = 648295481
    viewCount = 268537.51
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0


def test_get_ten_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "lava лампа"
    price = 335392
    contacts = 312
    likes = 5.21
    viewCount = 0
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0


def test_get_eleven_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "lavaлампа"
    price = 335392
    contacts = 312
    likes = "5"
    viewCount = 0
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0


def test_get_twelve_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "✧✧✧✧✧✧"
    price = 5508
    contacts = 121498439
    likes = 819
    viewCount = 0
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0


def test_get_thirteen_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = ""
    price = 335392
    contacts = 312
    likes = 5
    viewCount = 0
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0


def test_get_fourteen_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "наушники"
    price = -528359964
    contacts = 192109
    likes = 542820
    viewCount = 6
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0


def test_get_fiveteen_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "КАМЕРА"
    price = 84
    contacts = -8
    likes = 37
    viewCount = 75
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500
    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0


def test_get_sixteen_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "плащ-палатка"
    price = 70991249656
    contacts = 0
    likes = -648295481
    viewCount = 268537
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0


def test_get_seventeen_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "Торшер"
    price = 3
    contacts = 2483
    likes = 0
    viewCount = -74696
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0


def test_get_eighteen_ad():

    # Обращаемся ко всем объявлениям продавца

    sellerId = 326460
    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_before = len(all_ad_sellerId)
    assert all_ad_sellerId

    # Сохраняем новое объявление продавца

    name = "Противоположная точка зрения подразумевает, что стремящиеся вытеснить традиционное производство, нанотехнологии, которые представляют собой яркий пример континентально-европейского типа политической культуры, будут призваны к ответу. В целом, конечно, перспективное планирование требует от нас анализа дальнейших направлений развития. Наше дело не так однозначно, как может показаться: повышение уровня гражданского сознания выявляет срочную потребность первоочередных требований."
    price = 21060
    contacts = 0
    likes = 4839
    viewCount = 43968
    result = api.save_ad(name, price, sellerId, contacts, likes, viewCount)
    assert result["message"] == "internal error"
    assert result["code"] == 500

    # Обращаемся ко всем объявлениям продавца повторно

    all_ad_sellerId = api.get_ad_sellerId(sellerId)
    len_after = len(all_ad_sellerId)

    # Провереям, что новое объявление не сохранилось(0)

    assert len_after - len_before == 0
