import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apitask.settings')

django.setup()

from announcement_api.models import Announcement

# HEADERS = {'Accept-Encoding': 'identity'}


DATA = {
    'header':[
        'Установка Видеонаблюдение шлагбаум сигнализация обслуживание домофон',
        'Установка видеонаблюдения. Домофонов. СКУД, монтаж, обслуживание',
        'Монтаж, настройка видеонаблюдения под ключ, обслуживание',
        'Монтаж, Установка, Обслуживание СКС, СКУД, Видеонаблюдения, АТС во Владивостоке',
        'Видеонаблюдение, домофоны, ОПС, СКУД, установка, монтаж, обслуживание',
        'Установка видеонаблюдения для дома/ дачи/ офиса (монтаж, обслуживание)',
        'Установка видеонаблюдения. (Проектирование, монтаж. обслуживание)',
        'Ремонт/Настройка видеонаблюдения: камер, регистраторов, домофонов. И т. д',
        'Монтаж видеонаблюдения Hikvision HiWatch Trassir, СКУД, домофонов',
        'Видеонаблюдение Установка Продажа Настройка Видеокамер IP'
    ],
    'author':[
        '100 камер',
        'SmartVision',
        'AtlantisGroup',
        'SmartVision',
        'AtlantisGroup',
        'ООО А Сервис',
        'primssm',
        'GM1022',
        'doneit',
        'TVi MART',
    ],
    'views_count':[
        7753, 1866, 369, 211, 6034, 268, 369, 330, 536, 1485
    ],
}


def load_project_database(announcements_count: int) -> None:
    '''Скрипт для загрузки данных для теста'''
    for i in range(10):
        Announcement.objects.create(
            header=DATA['header'][i],
            author=DATA['author'][i],
            views_count=DATA['views_count'][i],
            position=i+1,
        )


# url = 'https://www.farpost.ru/vladivostok/service/construction/guard/+/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F/#center=43.17296717586861%2C131.96034531052948&zoom=11.60415718364368'
    # response = requests.get(url, headers=HEADERS)
    #
    # soup = BeautifulSoup(response.content, parser='lxml')
    # all_announcements = soup.find_all(_class='descriptionCell')
    # for i in range(announcements_count):
    #     load_announcement(
    #         url=all_announcements[i].find(class_='bulletinLink bull-item__self-link auto-shy').href,
    #         views=all_announcements[i].find(class_='views'),
    #         index=i
    #     )


# def load_announcement(url: str, views: int, index: int) -> None:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, parser='lxml')
#     print(f"header={soup.find(class_='subject viewbull-field__container')}, \
#         author={soup.find(class_='userNick')}, \
#         views_count={views},\
#         position={index},")


if __name__ == '__main__':
    load_project_database(announcements_count=10)