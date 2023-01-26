#!/usr/bin/env python
#

#import time
from typing import List
import wikipedia

requests_per_minute = 100
links_per_page = 200

class WikiRacer:
    def __init__(self, start, finish) -> None:
        self.start = start
        self.finish = finish

    def find_path(self, start: str, finish: str) -> List[str]:
        input_data = (start, finish)
        #requests_count = 0
        # Створюємо об'єкт сторiнки з потрiбною назвою
        try:
            start_link = wikipedia.search(start)
            current_page = wikipedia.page(start_link[0])
        except:
            current_page = None
        if current_page is not None:
            
            max_steps = 5
            steps = 0
            main_list_of_links = current_page.links[0:links_per_page]
            output_data = [start]

            while steps <= 200: # Прибрати хардкод
                # requests_count += 1
                # if requests_count > requests_per_minute:
                #     print("Too many requests, wait a minute")
                #     time.sleep(60)
                #     requests_count = 0

                # Перебираємо всi лiнки в основному масивi
                for main_link in range(len(main_list_of_links)):
                    if main_list_of_links[main_link].find(finish) == 0:
                        output_data.append(main_list_of_links[main_link])
                        result = ("%s->%s" % (input_data, output_data))
                        return result
                else:
                    cur_link = main_list_of_links[steps]
                    print('В основному масивi нема збiгiв, парсимо %s' % cur_link) # Декоративна строка, прибрати потiм
                    output_data.append(cur_link)                   
                    try:
                        cur = wikipedia.search(cur_link)
                        current_page = wikipedia.page(cur[0])
                    except:
                        print('Сторiнку %s не знайдено' % cur_link) # Декоратина, прибрати потiм
                        current_page = None
                    if current_page is not None:
                        current_list_of_links = current_page.links[0:links_per_page]

                    for link in range(len(current_list_of_links)):
                        if current_list_of_links[link].find(finish) == 0:
                            output_data.append(current_list_of_links[link])
                            result = ("%s->%s" % (input_data, output_data))
                            return result
                    else:
                        output_data.pop()
                        steps += 1
                        continue

                        # output_data.append(link)
                        # try:
                        #     cur = wikipedia.search(link)
                        #     current_page = wikipedia.page(cur[0])
                        # except:
                        #     current_page = None
                        # if current_page is not None:
                        #     current_list_of_links = current_page.links[0:links_per_page]
                        # for link1 in current_list_of_links:
                        #     if link1.find(finish) == 0:
                        #         output_data.append(link1)
                        #         result = ("%s->%s" % (input_data, output_data))
                        #         return result
                        #     else:
                        #         continue
                            
                
                #del output_data[-1]
                

### Зробити нормальний запуск

wikipedia.set_lang("uk") # Можливо прибрати хардкод
first_page_title = 'Фестиваль' # Прибрати хардкод
last_page_title = 'Пілястра' # Прибрати хардкод
start_app = WikiRacer.find_path(self = WikiRacer, start = first_page_title, finish = last_page_title)

if __name__ == "__main__":
    print(start_app)
