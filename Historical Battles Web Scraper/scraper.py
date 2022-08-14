from bs4 import BeautifulSoup
import requests

from battle import Battle

wiki_url = 'https://en.wikipedia.org'
battles_1_url = 'https://en.wikipedia.org/wiki/List_of_battles_before_301'
battles_2_url = 'https://en.wikipedia.org/wiki/List_of_battles_301–1300'
battle_summary_1 = {-6: [], -5: [], -4: [], -3: [], -2: [], -1: [], 1: [], 2: [], 3: []}
battle_summary_2 = {4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: []}
century_tracker = []
for key in battle_summary_1.keys():
    century_tracker.append(key)
for key in battle_summary_2.keys():
    century_tracker.append(key)
print(century_tracker)


def get_battle_data(url, data_dict, counter):
    battles_page = requests.get(url)
    battles_soup = BeautifulSoup(battles_page.content, 'html.parser')
    tables = battles_soup.findAll("table", {'class': ['wikitable', 'sortable', 'jquery-tablesorter']})
    for table in tables:
        for row in table.findAll('tr')[1:]:
            if len(row.findAll('td')) >= 3:
                battle_cell = row.findAll('td')[1].find('a')
            else:
                battle_cell = row.findAll('td')[0].find('a')
            if battle_cell is None or battle_cell.text == '':
                battle_cell = row.findAll('td')[0].find('a')
            if battle_cell is None:
                continue
            if battle_cell.has_attr('class') and battle_cell['class'][0] == 'new':
                continue
            battle_title = battle_cell.text
            battle_url = wiki_url + battle_cell['href']
            battle_page = requests.get(battle_url)
            battle_soup = BeautifulSoup(battle_page.content, 'html.parser')
            battle_soup_body = battle_soup.find('div', 'mw-parser-output')
            for nav in battle_soup_body.findAll("div", {'class': ['navbox', 'toc', 'reflist']}):
                nav.decompose()
            battle_soup_body_tags = battle_soup_body.findAll(['p', 'ul'])
            battle_info = ''
            for tag in battle_soup_body_tags:
                battle_info += tag.text
            try:
                battle_image = wiki_url + battle_soup_body.find('a', 'image')['href']
            except TypeError:
                battle_image = None
            print(battle_title)
            battle = Battle(title=battle_title, info=battle_info, image=battle_image)
            data_dict.get(century_tracker[counter]).append(battle)
        counter += 1


get_battle_data(battles_1_url, battle_summary_1, 0)
get_battle_data(battles_2_url, battle_summary_2, 9)

print('done')
