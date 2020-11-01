import random
import requests
from bs4 import BeautifulSoup
import os

#   Clear the terminal
os.system('cls')


class Series:
    def __init__(self, name, seasons, episodes, page,
                s1_episode_summaries, s2_episode_summaries, s3_episode_summaries,
                s4_episode_summaries, s5_episode_summaries, s6_episode_summaries,
                s7_episode_summaries):
        self.name = name
        self.seasons = seasons
        self.episodes = episodes
        self.page = page
        self.s1_episode_summaries = s1_episode_summaries
        self.s2_episode_summaries = s2_episode_summaries
        self.s3_episode_summaries = s3_episode_summaries
        self.s4_episode_summaries = s4_episode_summaries
        self.s5_episode_summaries = s5_episode_summaries
        self.s6_episode_summaries = s6_episode_summaries
        self.s7_episode_summaries = s7_episode_summaries


def site_scraper():
    page = requests.get(active_series.page[Season])
    soup = BeautifulSoup(page.content, 'html.parser')
    p = soup.find_all('p')[Episode_Location - 1]
    print(p.text)


def runnit():
    global st
    global tng
    global ds9
    global voy
    global ent
    global active_series
    global Episode_Location

    st = Series('Star Trek', 3, {1:29, 2:26, 3:24},
        {1:"https://startrekguide.com/2019/05/06/the-original-series-episode-guide-season-1/",
        2:"https://startrekguide.com/2019/05/06/the-original-series-episode-guide-season-2/",
        3:"https://startrekguide.com/2019/05/06/the-original-series-episode-guide-season-3/"},
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
        'No 4th season', 'No 5th season', 'No 6th Season', 'No 7th Season')

    tng = Series('The Next Generation', 7, {1:26, 2:22, 3:26, 4:26, 5:26, 6:26, 7:26},
        {1:"https://startrekguide.com/2019/05/02/tng-episode-guide-season-1/",
        2:"https://startrekguide.com/2019/05/02/tng-episode-guide-season-2/",
        3:"https://startrekguide.com/2019/05/02/tng-episode-guide-season-3/",
        4:"https://startrekguide.com/2019/05/02/tng-episode-guide-season-4/",
        5:"https://startrekguide.com/2019/05/02/tng-episode-guide-season-5/",
        6:"https://startrekguide.com/2019/05/02/tng-episode-guide-season-6/",
        7:"https://startrekguide.com/2019/05/02/tng-episode-guide-season-7/"},
        [0, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], 
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28],
        [0, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    ds9 = Series('Deep Space Nine', 7, {1:20, 2:26, 3:26, 4:26, 5:26, 6:26, 7:26},
        {1:"https://startrekguide.com/2019/05/06/deep-space-nine-episode-guide-season-1",
        2:"https://startrekguide.com/2019/05/06/deep-space-nine-episode-guide-season-2",
        3:"https://startrekguide.com/2019/05/06/deep-space-nine-episode-guide-season-3",
        4:"https://startrekguide.com/2019/05/06/deep-space-nine-episode-guide-season-4",
        5:"https://startrekguide.com/2019/05/06/deep-space-nine-episode-guide-season-5",
        6:"https://startrekguide.com/2019/05/06/deep-space-nine-episode-guide-season-6",
        7:"https://startrekguide.com/2019/05/06/deep-space-nine-episode-guide-season-7"},
        [0, 3, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 22, 23, 24, 25, 26, 27, 28],
        [0, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
        [0, 3, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 28])

    voy = Series('Voyager', 7, {1:16, 2:26, 3:26, 4:26, 5:26, 6:26, 7:26},
        {1:"https://startrekguide.com/2019/05/06/voyager-episode-guide-season-1",
        2:"https://startrekguide.com/2019/05/06/voyager-episode-guide-season-2",
        3:"https://startrekguide.com/2019/05/06/voyager-episode-guide-season-3",
        4:"https://startrekguide.com/2019/05/06/voyager-episode-guide-season-4",
        5:"https://startrekguide.com/2019/05/06/voyager-episode-guide-season-5",
        6:"https://startrekguide.com/2019/05/06/voyager-episode-guide-season-6",
        7:"https://startrekguide.com/2019/05/06/voyager-episode-guide-season-7"},
        [0, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21, 22, 23, 24, 25, 26, 27, 28],
        [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 26])

    ent = Series('Enterprise', 4, {1:26, 2:26, 3:24, 4:22},
        {1:"https://startrekguide.com/2019/05/03/enterprise-episode-guide-season-1",
        2:"https://startrekguide.com/2019/05/03/enterprise-episode-guide-season-2",
        3:"https://startrekguide.com/2019/05/03/enterprise-episode-guide-season-3",
        4:"https://startrekguide.com/2019/05/03/enterprise-episode-guide-season-4"},
        [0, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
        [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [0, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,],
        'No 5th season', 'No 6th Season', 'No 7th Season')
    
    show_library = {1:'Star Trek', 2:'TNG', 3:'DS9', 4:'Voyager', 5:'Enterprise', 6:'Random'}
    print()
    print(' 1-Star Trek\n 2-The Next Generations\n 3-Deep Space 9\n 4-Voyager\n 5-Enterprise\n 6-Random')
    
    try:
        choice = int(input('Select series from the above list: '))
        if choice not in(show_library.keys()):
            runnit()
    except ValueError:
        runnit()
    else:
        if choice == 6:
            choice = random.randint(1, 5)   
        if choice == 1:
            active_series = st
        elif choice == 2:
            active_series = tng
        elif choice == 3:
            active_series = ds9
        elif choice == 4:
            active_series = voy
        elif choice == 5:
            active_series = ent


#   Season and Episode selection
    global Season
    global Episode
    global Episode_Location


    Season = random.randint(1, (active_series.seasons))
    #Season = int(input('MANUAL SEASON SELECTION: '))   #Use this to manually select

    Episode = random.randint(1, (active_series.episodes[Season]))
    #Episode = int(input('MANUAL EPISODE SELECTION: '))   #Use this to manually select
    #print(f'randomly generated episode= {Episode}')


    if Season == 1:
        Episode_Location = active_series.s1_episode_summaries[Episode]
    elif Season == 2:
        Episode_Location = active_series.s2_episode_summaries[Episode]
    elif Season == 3:
        Episode_Location = active_series.s3_episode_summaries[Episode]
    elif Season == 4:
        Episode_Location = active_series.s4_episode_summaries[Episode]
    elif Season == 5:
        Episode_Location = active_series.s5_episode_summaries[Episode]
    elif Season == 6:
        Episode_Location = active_series.s6_episode_summaries[Episode]
    elif Season == 7:
        Episode_Location = active_series.s7_episode_summaries[Episode]

#Output
    print(f'Watch season {Season} episode {Episode} of {active_series.name}')
    print()
    print('Show episode summary?')
    summary = ''
    while summary != ('y' or 'n'):
        summary = input('y = Yes   n = No: ')
        if summary == ('n'):
            startup()
        elif summary == ('y'):
            site_scraper()


def done():
    print()
    print ('Beaming out!!')
    print()
    quit()


def startup():
    print()
    print()
    print('Run the Episoder?')
    ready = ''
    while ready != ('q' or 'y'):
        ready = input('y = Yes   q = QUIT: ')
        if ready == ('y'):
            runnit()
        elif ready == ('q'):
            done()
startup()



