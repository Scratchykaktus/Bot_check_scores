import requests


def req():
    data = {
        'Login': 'un6jpr8a',
        'Password': '8pgdVY3a',
    }

    session = requests.Session()
    login = session.post('https://de.ncfu.ru/Account/Login', data=data)

    r = session.get('https://de.ncfu.ru/api/user/GetUserTests?Localization=Ru')

    items = r.json()
    result = []
    for i in items:
        i_status = i.get('Status').strip()
        i_discipline = i.get('Discipline').strip()
        i_score = i.get('Score')
        result.append(
            [i_status, i_discipline, i_score]
        )

    return result

