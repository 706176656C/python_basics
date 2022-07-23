import time
from pprint import pprint
import requests


class Stackoverflow:

    def get_python_pub(self, tag: str):
        question_list = []
        time_now = int(time.time())
        time_2day = time_now - 172800
        page = 1
        while True:
            url = f'https://api.stackexchange.com/2.3/questions?'
            params = {'page': str(page), 'pagesize': '100', 'order': 'desc', 'min': str(time_2day),
                      'max': str(time_now), 'sort': 'creation', 'tagged': str(tag), 'site': 'stackoverflow'}
            response = requests.get(url=url, params=params)
            answer = response.json()
            # pprint(response.json())
            for question in answer['items']:
                question_list.append(question['title'])
            if not answer['has_more']:
                break
            page += 1

        pprint(question_list)


if __name__ == '__main__':
    py = Stackoverflow()
    py.get_python_pub('Python')
