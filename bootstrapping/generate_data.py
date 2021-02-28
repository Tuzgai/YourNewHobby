import csv, json, re, requests
from bs4 import BeautifulSoup

def get_hobby_data(hobby):
    hobby = hobby.rstrip()
    title = hobby.replace(' ', '_').rstrip()
    params = {
        'action': 'query',
        'prop': 'extracts',
        'exintro': 'true',
        'titles': title,
        'format': 'json',
        'redirects': ''
    }
    response = requests.get(
	    url='https://en.wikipedia.org/w/api.php', params=params
    )

    parsed_json = json.loads(response.text)
    
    page_id = list(parsed_json.get('query').get('pages').keys())[0]

    if page_id == '-1':
        return [hobby, 'bad title', '']

    page_data = list(parsed_json.get('query').get('pages').values())[0]
    html = page_data.get('extract')
    url = f'https://en.wikipedia.org/wiki/{page_data.get('title')}'
    print(f'Processed: {url}')
    soup = BeautifulSoup(html, features='html.parser')

    paragraph = ' '.join(soup.findAll(text=True)).strip().strip('\'').replace('\n', ' ')

    if "may refer to:" in paragraph:
        return [hobby, 'bad title', '']
    
    return [hobby, paragraph, url]

hobby_data = []
hobby_list = open('hobby_list.txt', 'r')

for hobby in hobby_list:
    hobby_data.append(get_hobby_data(hobby))

with open('hobby_data.csv', mode='w') as output_target:
    writer = csv.writer(output_target, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerows(hobby_data)