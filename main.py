from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import requests


baseURL = 'https://liptur.ru'
d = {
        'Хлевенский район': 'hlevray',
        'Задонский район': 'zadray',
        'Липецк': 'lipetsk',
        'Становлянский район': 'stanray',
        'Чаплыгинский район': 'chapray',
        'Тербунский район': 'terbray',
        'Лев-Толстовский район': 'levray',
        'Данковский район': 'dankray',
        'Елецкий район': 'elray',
        'Добринский район': 'dobray',
        'Липецкий район': 'lipray',
        'Елец': 'elets',
        'Краснинский район': 'krasray',
        'Лебедянский район': 'lebray',
        'Усманский район': 'usmray',
        'Добровский район': 'dobrovray'
    }


def parse_estates(dop=''):
    answ = []
    url = 'https://liptur.ru/ru/attractions/estates/' + dop
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allEst = soup.findAll('div', 'place-item-small')
    for i in allEst:
        s = BeautifulSoup(str(i), 'html.parser')
        l = s.find('a', 'd-block')
        link = baseURL + l['href']
        page = BeautifulSoup(requests.get(link).text, "html.parser")
        img = baseURL + page.find('a', 'carousel-backgr')['href']
        region = page.find('div', 'region').text
        name = page.find('div', 'head-itinerary').text
        description = page.find('div', 'object-desc').text

        btn = page.find('div', 'btn-box')
        btnSoup = BeautifulSoup(str(btn), 'html.parser')
        yalink = btnSoup.findAll('a')
        for i in yalink:
            try:
                parsed = urlparse(i['href'])
                degrees = parse_qs(parsed.query)['ll']
            except:
                pass
        tmp = ''
        for i in str(degrees):
            if i not in ['[', ']', "'"]:
                tmp += i
        tmp2 = tmp.split(',')
        model = {'name': name,
                 'place': d[region],
                 'text': description,
                 'image': img,
                 'category': 'usadbi',
                 'degrees': [str(tmp2[1]), str(tmp2[0])]
                 }
        answ.append(model)
    return answ


def parse_museums(dop=''):
    answ = []
    url = 'https://liptur.ru/ru/attractions/museums/' + dop
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allEst = soup.findAll('div', 'place-item-small')
    for i in allEst:
        s = BeautifulSoup(str(i), 'html.parser')
        l = s.find('a', 'd-block')
        link = baseURL + l['href']
        page = BeautifulSoup(requests.get(link).text, "html.parser")
        img = baseURL + page.find('a', 'carousel-backgr')['href']
        region = page.find('div', 'region').text
        name = page.find('div', 'head-itinerary').text
        description = page.find('div', 'object-desc').text

        btn = page.find('div', 'btn-box')
        btnSoup = BeautifulSoup(str(btn), 'html.parser')
        yalink = btnSoup.findAll('a')
        for i in yalink:
            try:
                parsed = urlparse(i['href'])
                degrees = parse_qs(parsed.query)['ll']
            except:
                pass
        tmp = ''
        for i in str(degrees):
            if i not in ['[', ']', "'"]:
                tmp += i
        tmp2 = tmp.split(',')
        model = {'name': name,
                 'place': d[region],
                 'text': description,
                 'image': img,
                 'category': 'museums',
                 'degrees': [str(tmp2[1]), str(tmp2[0])]
                 }
        answ.append(model)
    return answ


def parse_parks(dop=''):
    answ = []
    url = 'https://liptur.ru/ru/attractions/parks/' + dop
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allEst = soup.findAll('div', 'place-item-small')
    for i in allEst:
        s = BeautifulSoup(str(i), 'html.parser')
        l = s.find('a', 'd-block')
        link = baseURL + l['href']
        page = BeautifulSoup(requests.get(link).text, "html.parser")
        img = baseURL + page.find('a', 'carousel-backgr')['href']
        region = page.find('div', 'region').text
        name = page.find('div', 'head-itinerary').text
        description = page.find('div', 'object-desc').text

        btn = page.find('div', 'btn-box')
        btnSoup = BeautifulSoup(str(btn), 'html.parser')
        yalink = btnSoup.findAll('a')
        for i in yalink:
            try:
                parsed = urlparse(i['href'])
                degrees = parse_qs(parsed.query)['ll']
            except:
                pass
        tmp = ''
        for i in str(degrees):
            if i not in ['[', ']', "'"]:
                tmp += i
        tmp2 = tmp.split(',')
        model = {'name': name,
                 'place': d[region],
                 'text': description,
                 'image': img,
                 'category': 'parks',
                 'degrees': [str(tmp2[1]), str(tmp2[0])]
                 }
        answ.append(model)
    return answ


def parse_church(dop=''):
    answ = []
    url = 'https://liptur.ru/ru/attractions/temples/' + dop
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allEst = soup.findAll('div', 'place-item-small')
    for i in allEst:
        s = BeautifulSoup(str(i), 'html.parser')
        l = s.find('a', 'd-block')
        link = baseURL + l['href']
        page = BeautifulSoup(requests.get(link).text, "html.parser")
        img = baseURL + page.find('a', 'carousel-backgr')['href']
        region = page.find('div', 'region').text
        name = page.find('div', 'head-itinerary').text
        description = page.find('div', 'object-desc').text

        btn = page.find('div', 'btn-box')
        btnSoup = BeautifulSoup(str(btn), 'html.parser')
        yalink = btnSoup.findAll('a')
        for i in yalink:
            try:
                parsed = urlparse(i['href'])
                degrees = parse_qs(parsed.query)['ll']
            except:
                pass
        tmp = ''
        for i in str(degrees):
            if i not in ['[', ']', "'"]:
                tmp += i
        tmp2 = tmp.split(',')
        model = {'name': name,
                 'place': d[region],
                 'text': description,
                 'image': img,
                 'category': 'church',
                 'degrees': [str(tmp2[1]), str(tmp2[0])]
                 }
        answ.append(model)
    return answ


def parse_sport(dop=''):
    answ = []
    url = 'https://liptur.ru/ru/attractions/sport/' + dop
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allEst = soup.findAll('div', 'place-item-small')
    for i in allEst:
        s = BeautifulSoup(str(i), 'html.parser')
        l = s.find('a', 'd-block')
        link = baseURL + l['href']
        page = BeautifulSoup(requests.get(link).text, "html.parser")
        img = baseURL + page.find('a', 'carousel-backgr')['href']
        region = page.find('div', 'region').text
        name = page.find('div', 'head-itinerary').text
        description = page.find('div', 'object-desc').text

        btn = page.find('div', 'btn-box')
        btnSoup = BeautifulSoup(str(btn), 'html.parser')
        yalink = btnSoup.findAll('a')
        for i in yalink:
            try:
                parsed = urlparse(i['href'])
                degrees = parse_qs(parsed.query)['ll']
            except:
                pass
        tmp = ''
        for i in str(degrees):
            if i not in ['[', ']', "'"]:
                tmp += i
        tmp2 = tmp.split(',')
        model = {'name': name,
                 'place': d[region],
                 'text': description,
                 'image': img,
                 'category': 'sport',
                 'degrees': [str(tmp2[1]), str(tmp2[0])]
                 }
        answ.append(model)
    return answ


def parse_water(dop=''):
    answ = []
    url = 'https://liptur.ru/ru/attractions/rest_on_water/' + dop
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allEst = soup.findAll('div', 'place-item-small')
    for i in allEst:
        s = BeautifulSoup(str(i), 'html.parser')
        l = s.find('a', 'd-block')
        link = baseURL + l['href']
        page = BeautifulSoup(requests.get(link).text, "html.parser")
        img = baseURL + page.find('a', 'carousel-backgr')['href']
        region = page.find('div', 'region').text
        name = page.find('div', 'head-itinerary').text
        description = page.find('div', 'object-desc').text

        btn = page.find('div', 'btn-box')
        btnSoup = BeautifulSoup(str(btn), 'html.parser')
        yalink = btnSoup.findAll('a')
        for i in yalink:
            try:
                parsed = urlparse(i['href'])
                degrees = parse_qs(parsed.query)['ll']
            except:
                pass
        tmp = ''
        for i in str(degrees):
            if i not in ['[', ']', "'"]:
                tmp += i
        tmp2 = tmp.split(',')
        model = {'name': name,
                 'place': d[region],
                 'text': description,
                 'image': img,
                 'category': 'water',
                 'degrees': [str(tmp2[1]), str(tmp2[0])]
                 }
        answ.append(model)
    return answ


def parse_cities(dop=''):
    answ = []
    url = 'https://liptur.ru/ru/attractions/cities/' + dop
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allEst = soup.findAll('div', 'place-item-small')
    for i in allEst:
        s = BeautifulSoup(str(i), 'html.parser')
        l = s.find('a', 'd-block')
        link = baseURL + l['href']
        page = BeautifulSoup(requests.get(link).text, "html.parser")
        img = baseURL + page.find('a', 'carousel-backgr')['href']
        region = page.find('div', 'region').text
        name = page.find('div', 'head-itinerary').text
        description = page.find('div', 'object-desc').text

        btn = page.find('div', 'btn-box')
        btnSoup = BeautifulSoup(str(btn), 'html.parser')
        yalink = btnSoup.findAll('a')
        for i in yalink:
            try:
                parsed = urlparse(i['href'])
                degrees = parse_qs(parsed.query)['ll']
            except:
                pass
        tmp = ''
        for i in str(degrees):
            if i not in ['[', ']', "'"]:
                tmp += i
        tmp2 = tmp.split(',')
        model = {'name': name,
                 'place': region,
                 'text': description,
                 'image': img,
                 'category': 'cities',
                 'degrees': [str(tmp2[1]), str(tmp2[0])]
                 }
        answ.append(model)
    return answ


def parse_all():
    resp = []
    i = 0
    while i < 2:
        i = i + 1
        try:
            t = f'?PAGEN_1={i}'
            a = parse_estates(t)
            resp = resp + a
        except:
            break
    i = 0
    while i < 4:
        i = i + 1
        try:
            t = f'?PAGEN_1={i}'
            a = parse_museums(t)
            resp = resp + a
        except:
            break
    i = 0
    while i < 2:
        i = i + 1
        try:
            t = f'?PAGEN_1={i}'
            a = parse_parks(t)
            resp = resp + a
        except:
            break
    i = 0
    while i < 1:
        i = i + 1
        try:
            t = f'?PAGEN_1={i}'
            a = parse_church(t)
            resp = resp + a
        except:
            break
    i = 0
    while i < 1:
        i = i + 1
        try:
            t = f'?PAGEN_1={i}'
            a = parse_sport(t)
            resp = resp + a
        except:
            break
    i = 0
    while i < 2:
        i = i + 1
        try:
            t = f'?PAGEN_1={i}'
            a = parse_water(t)
            resp = resp + a
        except:
            break
    i = 0
    while i < 1:
        i = i + 1
        try:
            t = f'?PAGEN_1={i}'
            a = parse_cities(t)
            resp = resp + a
        except:
            break
    return resp


# k = {'new': parse_all()}

# print(requests.post('https://liptur.octateam.ru/sights/add', json=k).text)


def parse_trips():
    answ = []
    url = 'https://liptur.ru/ru/routes/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allEst = soup.findAll('div', 'place-item-small')
    for i in allEst:
        s = BeautifulSoup(str(i), 'html.parser')
        l = s.find('a', 'd-block')
        link = baseURL + l['href']
        page = BeautifulSoup(requests.get(link).text, "html.parser")
        imgt = page.find('div', 'main-img')['style']
        img = baseURL
        for i in range(35, len(imgt) - 15):
            img += imgt[i]
        region = page.find('div', 'region').text
        name = page.find('div', 'head-itinerary').text
        description = page.find('div', 'plan-details').text
        times = page.find('div', 'time').text
        length = page.find('div', 'length').text

        model = {'name': name,
                 'text': description,
                 'image': img,
                 'time': times,
                 'length': length,
                 'categories': ['1000', '100', 'many']
                 }
        answ.append(model)
    return answ


kk = {'new': parse_trips()}
print(requests.post('https://liptur.octateam.ru/trips/add', json=kk).text)
