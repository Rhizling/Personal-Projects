import scraper
import pandas as pd

scraper.battle_summary_1.update(scraper.battle_summary_2)
battle_data = []


def numbers_to_century(conversion):
    century = {-6: "Before 500 BC",
               -5: "5th Century BC",
               -4: "4th Century BC",
               -3: "3rd Century BC",
               -2: "2nd Century BC",
               -1: "1st Century BC",
               1: "1st Century",
               2: "2nd Century",
               3: "3rd Century",
               4: "4th Century",
               5: "5th Century",
               6: "6th Century",
               7: "7th Century",
               8: "8th Century",
               9: "9th Century",
               10: "10th Century",
               11: "11th Century",
               12: "12th Century",
               13: "13th Century"
               }
    return century.get(conversion)


for key, battles in scraper.battle_summary_1.items():
    for battle in battles:
        battle_row = [numbers_to_century(key), battle.title, battle.info, battle.image]
        battle_data.append(battle_row)

battle_frame = pd.DataFrame(battle_data, columns=['Century', 'Title', 'Info', 'Image'])
battles_csv = battle_frame.to_csv('battles_pre_1300.csv', encoding='utf-8', index=False)
