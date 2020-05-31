{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import os\n",
    "from collections import Counter\n",
    "#print(os.listdir(\"../input\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>tt0369610</td>\n",
       "      <td>32.985763</td>\n",
       "      <td>150000000</td>\n",
       "      <td>1513528810</td>\n",
       "      <td>Jurassic World</td>\n",
       "      <td>Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...</td>\n",
       "      <td>Colin Trevorrow</td>\n",
       "      <td>The park is open.</td>\n",
       "      <td>Twenty-two years after the events of Jurassic ...</td>\n",
       "      <td>124</td>\n",
       "      <td>Action|Adventure|Science Fiction|Thriller</td>\n",
       "      <td>Universal Studios|Amblin Entertainment|Legenda...</td>\n",
       "      <td>6/9/2015</td>\n",
       "      <td>5562</td>\n",
       "      <td>6.5</td>\n",
       "      <td>2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>tt1392190</td>\n",
       "      <td>28.419936</td>\n",
       "      <td>150000000</td>\n",
       "      <td>378436354</td>\n",
       "      <td>Mad Max: Fury Road</td>\n",
       "      <td>Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...</td>\n",
       "      <td>George Miller</td>\n",
       "      <td>What a Lovely Day.</td>\n",
       "      <td>An apocalyptic story set in the furthest reach...</td>\n",
       "      <td>120</td>\n",
       "      <td>Action|Adventure|Science Fiction|Thriller</td>\n",
       "      <td>Village Roadshow Pictures|Kennedy Miller Produ...</td>\n",
       "      <td>5/13/2015</td>\n",
       "      <td>6185</td>\n",
       "      <td>7.1</td>\n",
       "      <td>2015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>tt2908446</td>\n",
       "      <td>13.112507</td>\n",
       "      <td>110000000</td>\n",
       "      <td>295238201</td>\n",
       "      <td>Insurgent</td>\n",
       "      <td>Shailene Woodley|Theo James|Kate Winslet|Ansel...</td>\n",
       "      <td>Robert Schwentke</td>\n",
       "      <td>One Choice Can Destroy You</td>\n",
       "      <td>Beatrice Prior must confront her inner demons ...</td>\n",
       "      <td>119</td>\n",
       "      <td>Adventure|Science Fiction|Thriller</td>\n",
       "      <td>Summit Entertainment|Mandeville Films|Red Wago...</td>\n",
       "      <td>3/18/2015</td>\n",
       "      <td>2480</td>\n",
       "      <td>6.3</td>\n",
       "      <td>2015</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     imdb_id  popularity     budget     revenue      original_title  \\\n",
       "0  tt0369610   32.985763  150000000  1513528810      Jurassic World   \n",
       "1  tt1392190   28.419936  150000000   378436354  Mad Max: Fury Road   \n",
       "2  tt2908446   13.112507  110000000   295238201           Insurgent   \n",
       "\n",
       "                                                cast          director  \\\n",
       "0  Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...   Colin Trevorrow   \n",
       "1  Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...     George Miller   \n",
       "2  Shailene Woodley|Theo James|Kate Winslet|Ansel...  Robert Schwentke   \n",
       "\n",
       "                      tagline  \\\n",
       "0           The park is open.   \n",
       "1          What a Lovely Day.   \n",
       "2  One Choice Can Destroy You   \n",
       "\n",
       "                                            overview  runtime  \\\n",
       "0  Twenty-two years after the events of Jurassic ...      124   \n",
       "1  An apocalyptic story set in the furthest reach...      120   \n",
       "2  Beatrice Prior must confront her inner demons ...      119   \n",
       "\n",
       "                                      genres  \\\n",
       "0  Action|Adventure|Science Fiction|Thriller   \n",
       "1  Action|Adventure|Science Fiction|Thriller   \n",
       "2         Adventure|Science Fiction|Thriller   \n",
       "\n",
       "                                production_companies release_date  vote_count  \\\n",
       "0  Universal Studios|Amblin Entertainment|Legenda...     6/9/2015        5562   \n",
       "1  Village Roadshow Pictures|Kennedy Miller Produ...    5/13/2015        6185   \n",
       "2  Summit Entertainment|Mandeville Films|Red Wago...    3/18/2015        2480   \n",
       "\n",
       "   vote_average  release_year  \n",
       "0           6.5          2015  \n",
       "1           7.1          2015  \n",
       "2           6.3          2015  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv('data.csv')\n",
    "data.head(3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1890"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Предобработка датасета"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста\n",
    "# сюда можем вписать создание новых колонок в датасете\n",
    "data['profit'] = data['revenue'] - data['budget']\n",
    "data['release_month'] = data.release_date.apply(lambda x:x.split('/')[0])\n",
    "data['original_title_len'] = data.original_title.apply(lambda x: len(x))\n",
    "data['word_len'] = data.original_title.apply(lambda x: len(x.split(' ')))\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1. У какого фильма из списка самый большой бюджет?\n",
    "Варианты ответов:\n",
    "1. The Dark Knight Rises (tt1345836)\n",
    "2. Spider-Man 3 (tt0413300)\n",
    "3. Avengers: Age of Ultron (tt2395427)\n",
    "4. The Warrior's Way\t(tt1032751)\n",
    "5. Pirates of the Caribbean: On Stranger Tides (tt1298650)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>profit</th>\n",
       "      <th>release_month</th>\n",
       "      <th>original_title_len</th>\n",
       "      <th>word_len</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>491</th>\n",
       "      <td>tt1032751</td>\n",
       "      <td>0.25054</td>\n",
       "      <td>425000000</td>\n",
       "      <td>11087569</td>\n",
       "      <td>The Warrior's Way</td>\n",
       "      <td>Kate Bosworth|Jang Dong-gun|Geoffrey Rush|Dann...</td>\n",
       "      <td>Sngmoo Lee</td>\n",
       "      <td>Assassin. Hero. Legend.</td>\n",
       "      <td>An Asian assassin (Dong-gun Jang) is forced to...</td>\n",
       "      <td>100</td>\n",
       "      <td>Adventure|Fantasy|Action|Western|Thriller</td>\n",
       "      <td>Boram Entertainment Inc.</td>\n",
       "      <td>12/2/2010</td>\n",
       "      <td>74</td>\n",
       "      <td>6.4</td>\n",
       "      <td>2010</td>\n",
       "      <td>-413912431</td>\n",
       "      <td>12</td>\n",
       "      <td>17</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       imdb_id  popularity     budget   revenue     original_title  \\\n",
       "491  tt1032751     0.25054  425000000  11087569  The Warrior's Way   \n",
       "\n",
       "                                                  cast    director  \\\n",
       "491  Kate Bosworth|Jang Dong-gun|Geoffrey Rush|Dann...  Sngmoo Lee   \n",
       "\n",
       "                     tagline  \\\n",
       "491  Assassin. Hero. Legend.   \n",
       "\n",
       "                                              overview  runtime  \\\n",
       "491  An Asian assassin (Dong-gun Jang) is forced to...      100   \n",
       "\n",
       "                                        genres      production_companies  \\\n",
       "491  Adventure|Fantasy|Action|Western|Thriller  Boram Entertainment Inc.   \n",
       "\n",
       "    release_date  vote_count  vote_average  release_year     profit  \\\n",
       "491    12/2/2010          74           6.4          2010 -413912431   \n",
       "\n",
       "    release_month  original_title_len  word_len  \n",
       "491            12                  17         3  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# тут вводим ваш ответ и добавлем в его список ответов (сейчас для примера стоит \"1\")\n",
    "display(data[data.budget == data.budget.max()])\n",
    "\n",
    "answer_ls.append(4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2. Какой из фильмов самый длительный (в минутах)\n",
    "1. The Lord of the Rings: The Return of the King\t(tt0167260)\n",
    "2. Gods and Generals\t(tt0279111)\n",
    "3. King Kong\t(tt0360717)\n",
    "4. Pearl Harbor\t(tt0213149)\n",
    "5. Alexander\t(tt0346491)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>profit</th>\n",
       "      <th>release_month</th>\n",
       "      <th>original_title_len</th>\n",
       "      <th>word_len</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1158</th>\n",
       "      <td>tt0279111</td>\n",
       "      <td>0.469518</td>\n",
       "      <td>56000000</td>\n",
       "      <td>12923936</td>\n",
       "      <td>Gods and Generals</td>\n",
       "      <td>Stephen Lang|Jeff Daniels|Robert Duvall|Kevin ...</td>\n",
       "      <td>Ronald F. Maxwell</td>\n",
       "      <td>The nations heart was touched by...</td>\n",
       "      <td>The film centers mostly around the personal an...</td>\n",
       "      <td>214</td>\n",
       "      <td>Drama|History|War</td>\n",
       "      <td>Turner Pictures|Antietam Filmworks</td>\n",
       "      <td>2/21/2003</td>\n",
       "      <td>23</td>\n",
       "      <td>5.8</td>\n",
       "      <td>2003</td>\n",
       "      <td>-43076064</td>\n",
       "      <td>2</td>\n",
       "      <td>17</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        imdb_id  popularity    budget   revenue     original_title  \\\n",
       "1158  tt0279111    0.469518  56000000  12923936  Gods and Generals   \n",
       "\n",
       "                                                   cast           director  \\\n",
       "1158  Stephen Lang|Jeff Daniels|Robert Duvall|Kevin ...  Ronald F. Maxwell   \n",
       "\n",
       "                                  tagline  \\\n",
       "1158  The nations heart was touched by...   \n",
       "\n",
       "                                               overview  runtime  \\\n",
       "1158  The film centers mostly around the personal an...      214   \n",
       "\n",
       "                 genres                production_companies release_date  \\\n",
       "1158  Drama|History|War  Turner Pictures|Antietam Filmworks    2/21/2003   \n",
       "\n",
       "      vote_count  vote_average  release_year    profit release_month  \\\n",
       "1158          23           5.8          2003 -43076064             2   \n",
       "\n",
       "      original_title_len  word_len  \n",
       "1158                  17         3  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data[data.runtime == data.runtime.max()])\n",
    "\n",
    "answer_ls.append(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3. Какой из фильмов самый короткий (в минутах)\n",
    "Варианты ответов:\n",
    "\n",
    "1. Home on the Range\ttt0299172\n",
    "2. The Jungle Book 2\ttt0283426\n",
    "3. Winnie the Pooh\ttt1449283\n",
    "4. Corpse Bride\ttt0121164\n",
    "5. Hoodwinked!\ttt0443536"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>profit</th>\n",
       "      <th>release_month</th>\n",
       "      <th>original_title_len</th>\n",
       "      <th>word_len</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>769</th>\n",
       "      <td>tt1449283</td>\n",
       "      <td>1.425344</td>\n",
       "      <td>30000000</td>\n",
       "      <td>14460000</td>\n",
       "      <td>Winnie the Pooh</td>\n",
       "      <td>Jim Cummings|Travis Oates|Jim Cummings|Bud Luc...</td>\n",
       "      <td>Stephen Anderson|Don Hall</td>\n",
       "      <td>Oh Pooh.</td>\n",
       "      <td>During an ordinary day in Hundred Acre Wood, W...</td>\n",
       "      <td>63</td>\n",
       "      <td>Animation|Family</td>\n",
       "      <td>Walt Disney Pictures|Walt Disney Animation Stu...</td>\n",
       "      <td>4/13/2011</td>\n",
       "      <td>174</td>\n",
       "      <td>6.8</td>\n",
       "      <td>2011</td>\n",
       "      <td>-15540000</td>\n",
       "      <td>4</td>\n",
       "      <td>15</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       imdb_id  popularity    budget   revenue   original_title  \\\n",
       "769  tt1449283    1.425344  30000000  14460000  Winnie the Pooh   \n",
       "\n",
       "                                                  cast  \\\n",
       "769  Jim Cummings|Travis Oates|Jim Cummings|Bud Luc...   \n",
       "\n",
       "                      director   tagline  \\\n",
       "769  Stephen Anderson|Don Hall  Oh Pooh.   \n",
       "\n",
       "                                              overview  runtime  \\\n",
       "769  During an ordinary day in Hundred Acre Wood, W...       63   \n",
       "\n",
       "               genres                               production_companies  \\\n",
       "769  Animation|Family  Walt Disney Pictures|Walt Disney Animation Stu...   \n",
       "\n",
       "    release_date  vote_count  vote_average  release_year    profit  \\\n",
       "769    4/13/2011         174           6.8          2011 -15540000   \n",
       "\n",
       "    release_month  original_title_len  word_len  \n",
       "769             4                  15         3  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data[data.runtime == data.runtime.min()])\n",
    "\n",
    "answer_ls.append(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 4. Средняя длительность фильма?\n",
    "\n",
    "Варианты ответов:\n",
    "1. 115\n",
    "2. 110\n",
    "3. 105\n",
    "4. 120\n",
    "5. 100\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "109.65343915343915"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data.runtime.mean())\n",
    "\n",
    "answer_ls.append(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 5. Средняя длительность фильма по медиане?\n",
    "Варианты ответов:\n",
    "1. 106\n",
    "2. 112\n",
    "3. 101\n",
    "4. 120\n",
    "5. 115\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "106.5"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data.runtime.median())\n",
    "\n",
    "answer_ls.append(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 6. Какой самый прибыльный фильм?\n",
    "Варианты ответов:\n",
    "1. The Avengers\ttt0848228\n",
    "2. Minions\ttt2293640\n",
    "3. Star Wars: The Force Awakens\ttt2488496\n",
    "4. Furious 7\ttt2820852\n",
    "5. Avatar\ttt0499549"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>profit</th>\n",
       "      <th>release_month</th>\n",
       "      <th>original_title_len</th>\n",
       "      <th>word_len</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>239</th>\n",
       "      <td>tt0499549</td>\n",
       "      <td>9.432768</td>\n",
       "      <td>237000000</td>\n",
       "      <td>2781505847</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>Sam Worthington|Zoe Saldana|Sigourney Weaver|S...</td>\n",
       "      <td>James Cameron</td>\n",
       "      <td>Enter the World of Pandora.</td>\n",
       "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
       "      <td>162</td>\n",
       "      <td>Action|Adventure|Fantasy|Science Fiction</td>\n",
       "      <td>Ingenious Film Partners|Twentieth Century Fox ...</td>\n",
       "      <td>12/10/2009</td>\n",
       "      <td>8458</td>\n",
       "      <td>7.1</td>\n",
       "      <td>2009</td>\n",
       "      <td>2544505847</td>\n",
       "      <td>12</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       imdb_id  popularity     budget     revenue original_title  \\\n",
       "239  tt0499549    9.432768  237000000  2781505847         Avatar   \n",
       "\n",
       "                                                  cast       director  \\\n",
       "239  Sam Worthington|Zoe Saldana|Sigourney Weaver|S...  James Cameron   \n",
       "\n",
       "                         tagline  \\\n",
       "239  Enter the World of Pandora.   \n",
       "\n",
       "                                              overview  runtime  \\\n",
       "239  In the 22nd century, a paraplegic Marine is di...      162   \n",
       "\n",
       "                                       genres  \\\n",
       "239  Action|Adventure|Fantasy|Science Fiction   \n",
       "\n",
       "                                  production_companies release_date  \\\n",
       "239  Ingenious Film Partners|Twentieth Century Fox ...   12/10/2009   \n",
       "\n",
       "     vote_count  vote_average  release_year      profit release_month  \\\n",
       "239        8458           7.1          2009  2544505847            12   \n",
       "\n",
       "     original_title_len  word_len  \n",
       "239                   6         1  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data[data.profit == data.profit.max()])\n",
    "\n",
    "answer_ls.append(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 7. Какой фильм самый убыточный?\n",
    "Варианты ответов:\n",
    "1. Supernova tt0134983\n",
    "2. The Warrior's Way tt1032751\n",
    "3. Flushed Away\ttt0424095\n",
    "4. The Adventures of Pluto Nash\ttt0180052\n",
    "5. The Lone Ranger\ttt1210819"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>profit</th>\n",
       "      <th>release_month</th>\n",
       "      <th>original_title_len</th>\n",
       "      <th>word_len</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>491</th>\n",
       "      <td>tt1032751</td>\n",
       "      <td>0.25054</td>\n",
       "      <td>425000000</td>\n",
       "      <td>11087569</td>\n",
       "      <td>The Warrior's Way</td>\n",
       "      <td>Kate Bosworth|Jang Dong-gun|Geoffrey Rush|Dann...</td>\n",
       "      <td>Sngmoo Lee</td>\n",
       "      <td>Assassin. Hero. Legend.</td>\n",
       "      <td>An Asian assassin (Dong-gun Jang) is forced to...</td>\n",
       "      <td>100</td>\n",
       "      <td>Adventure|Fantasy|Action|Western|Thriller</td>\n",
       "      <td>Boram Entertainment Inc.</td>\n",
       "      <td>12/2/2010</td>\n",
       "      <td>74</td>\n",
       "      <td>6.4</td>\n",
       "      <td>2010</td>\n",
       "      <td>-413912431</td>\n",
       "      <td>12</td>\n",
       "      <td>17</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       imdb_id  popularity     budget   revenue     original_title  \\\n",
       "491  tt1032751     0.25054  425000000  11087569  The Warrior's Way   \n",
       "\n",
       "                                                  cast    director  \\\n",
       "491  Kate Bosworth|Jang Dong-gun|Geoffrey Rush|Dann...  Sngmoo Lee   \n",
       "\n",
       "                     tagline  \\\n",
       "491  Assassin. Hero. Legend.   \n",
       "\n",
       "                                              overview  runtime  \\\n",
       "491  An Asian assassin (Dong-gun Jang) is forced to...      100   \n",
       "\n",
       "                                        genres      production_companies  \\\n",
       "491  Adventure|Fantasy|Action|Western|Thriller  Boram Entertainment Inc.   \n",
       "\n",
       "    release_date  vote_count  vote_average  release_year     profit  \\\n",
       "491    12/2/2010          74           6.4          2010 -413912431   \n",
       "\n",
       "    release_month  original_title_len  word_len  \n",
       "491            12                  17         3  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data[data.profit == data.profit.min()])\n",
    "\n",
    "answer_ls.append(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 8. Сколько всего фильмов в прибыли?\n",
    "Варианты ответов:\n",
    "1. 1478\n",
    "2. 1520\n",
    "3. 1241\n",
    "4. 1135\n",
    "5. 1398\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1478"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(len(data[data.profit > 0]))\n",
    "\n",
    "answer_ls.append(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 9. Самый прибыльный фильм в 2008 году?\n",
    "Варианты ответов:\n",
    "1. Madagascar: Escape 2 Africa\ttt0479952\n",
    "2. Iron Man\ttt0371746\n",
    "3. Kung Fu Panda\ttt0441773\n",
    "4. The Dark Knight\ttt0468569\n",
    "5. Mamma Mia!\ttt0795421"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>profit</th>\n",
       "      <th>release_month</th>\n",
       "      <th>original_title_len</th>\n",
       "      <th>word_len</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>600</th>\n",
       "      <td>tt0468569</td>\n",
       "      <td>8.466668</td>\n",
       "      <td>185000000</td>\n",
       "      <td>1001921825</td>\n",
       "      <td>The Dark Knight</td>\n",
       "      <td>Christian Bale|Michael Caine|Heath Ledger|Aaro...</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Why So Serious?</td>\n",
       "      <td>Batman raises the stakes in his war on crime. ...</td>\n",
       "      <td>152</td>\n",
       "      <td>Drama|Action|Crime|Thriller</td>\n",
       "      <td>DC Comics|Legendary Pictures|Warner Bros.|Syncopy</td>\n",
       "      <td>7/16/2008</td>\n",
       "      <td>8432</td>\n",
       "      <td>8.1</td>\n",
       "      <td>2008</td>\n",
       "      <td>816921825</td>\n",
       "      <td>7</td>\n",
       "      <td>15</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       imdb_id  popularity     budget     revenue   original_title  \\\n",
       "600  tt0468569    8.466668  185000000  1001921825  The Dark Knight   \n",
       "\n",
       "                                                  cast           director  \\\n",
       "600  Christian Bale|Michael Caine|Heath Ledger|Aaro...  Christopher Nolan   \n",
       "\n",
       "             tagline                                           overview  \\\n",
       "600  Why So Serious?  Batman raises the stakes in his war on crime. ...   \n",
       "\n",
       "     runtime                       genres  \\\n",
       "600      152  Drama|Action|Crime|Thriller   \n",
       "\n",
       "                                  production_companies release_date  \\\n",
       "600  DC Comics|Legendary Pictures|Warner Bros.|Syncopy    7/16/2008   \n",
       "\n",
       "     vote_count  vote_average  release_year     profit release_month  \\\n",
       "600        8432           8.1          2008  816921825             7   \n",
       "\n",
       "     original_title_len  word_len  \n",
       "600                  15         3  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_2008 = data.query('release_year == 2008')\n",
    "display(data_2008[data_2008.profit == data_2008.profit.max()])\n",
    "\n",
    "answer_ls.append(4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?\n",
    "Варианты ответов:\n",
    "1. Winter's Tale\ttt1837709\n",
    "2. Stolen\ttt1656186\n",
    "3. Broken City\ttt1235522\n",
    "4. Upside Down\ttt1374992\n",
    "5. The Lone Ranger\ttt1210819\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>profit</th>\n",
       "      <th>release_month</th>\n",
       "      <th>original_title_len</th>\n",
       "      <th>word_len</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1246</th>\n",
       "      <td>tt1210819</td>\n",
       "      <td>1.21451</td>\n",
       "      <td>255000000</td>\n",
       "      <td>89289910</td>\n",
       "      <td>The Lone Ranger</td>\n",
       "      <td>Johnny Depp|Armie Hammer|William Fichtner|Hele...</td>\n",
       "      <td>Gore Verbinski</td>\n",
       "      <td>Never Take Off the Mask</td>\n",
       "      <td>The Texas Rangers chase down a gang of outlaws...</td>\n",
       "      <td>149</td>\n",
       "      <td>Action|Adventure|Western</td>\n",
       "      <td>Walt Disney Pictures|Jerry Bruckheimer Films|I...</td>\n",
       "      <td>7/3/2013</td>\n",
       "      <td>1607</td>\n",
       "      <td>6.0</td>\n",
       "      <td>2013</td>\n",
       "      <td>-165710090</td>\n",
       "      <td>7</td>\n",
       "      <td>15</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        imdb_id  popularity     budget   revenue   original_title  \\\n",
       "1246  tt1210819     1.21451  255000000  89289910  The Lone Ranger   \n",
       "\n",
       "                                                   cast        director  \\\n",
       "1246  Johnny Depp|Armie Hammer|William Fichtner|Hele...  Gore Verbinski   \n",
       "\n",
       "                      tagline  \\\n",
       "1246  Never Take Off the Mask   \n",
       "\n",
       "                                               overview  runtime  \\\n",
       "1246  The Texas Rangers chase down a gang of outlaws...      149   \n",
       "\n",
       "                        genres  \\\n",
       "1246  Action|Adventure|Western   \n",
       "\n",
       "                                   production_companies release_date  \\\n",
       "1246  Walt Disney Pictures|Jerry Bruckheimer Films|I...     7/3/2013   \n",
       "\n",
       "      vote_count  vote_average  release_year     profit release_month  \\\n",
       "1246        1607           6.0          2013 -165710090             7   \n",
       "\n",
       "      original_title_len  word_len  \n",
       "1246                  15         3  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_12_14 = data.query('2011 < release_year < 2015')\n",
    "display(data_12_14[data_12_14.profit == data_12_14.profit.min()])\n",
    "\n",
    "answer_ls.append(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 11. Какого жанра фильмов больше всего?\n",
    "Варианты ответов:\n",
    "1. Action\n",
    "2. Adventure\n",
    "3. Drama\n",
    "4. Comedy\n",
    "5. Thriller"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'x' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-16-6c580546bd91>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mgenre_counter\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mCounter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mgenre\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mdata\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgenres\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'|'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m     \u001b[0mgenre_counter\u001b[0m \u001b[1;33m+=\u001b[0m \u001b[0mCounter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;31m# Ошибку увидел!!! Выдавал Thriller; 1890\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[0mgenre_counter\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmost_common\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'x' is not defined"
     ]
    }
   ],
   "source": [
    "answer_ls.append(5)\n",
    "\n",
    "genre_counter = Counter()\n",
    "for genre in data.genres.str.split('|'):\n",
    "    genre_counter += Counter(x) # Ошибку увидел!!! Выдавал Thriller; 1890\n",
    "genre_counter.most_common()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 12. Какого жанра среди прибыльных фильмов больше всего?\n",
    "Варианты ответов:\n",
    "1. Drama\n",
    "2. Comedy\n",
    "3. Action\n",
    "4. Thriller\n",
    "5. Adventure"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Drama', 560),\n",
       " ('Comedy', 551),\n",
       " ('Thriller', 446),\n",
       " ('Action', 444),\n",
       " ('Adventure', 337),\n",
       " ('Romance', 242),\n",
       " ('Crime', 231),\n",
       " ('Family', 226),\n",
       " ('Science Fiction', 195),\n",
       " ('Fantasy', 188),\n",
       " ('Horror', 150),\n",
       " ('Animation', 120),\n",
       " ('Mystery', 119),\n",
       " ('Music', 47),\n",
       " ('History', 46),\n",
       " ('War', 41),\n",
       " ('Western', 12),\n",
       " ('Documentary', 7)]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "answer_ls.append(1)\n",
    "\n",
    "data_profit = data.query('profit > 0')\n",
    "counter_profit = Counter()\n",
    "for i in data_profit.genres.str.split('|'):\n",
    "    counter_profit += Counter(i) \n",
    "counter_profit.most_common()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 13. Кто из режиссеров снял больше всего фильмов?\n",
    "Варианты ответов:\n",
    "1. Steven Spielberg\n",
    "2. Ridley Scott \n",
    "3. Steven Soderbergh\n",
    "4. Christopher Nolan\n",
    "5. Clint Eastwood"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Steven Soderbergh', 13), ('Ridley Scott', 12), ('Clint Eastwood', 12)]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "answer_ls.append(3)\n",
    "\n",
    "counter_director = Counter()\n",
    "for x in data.director.str.split('|'):\n",
    "    counter_director += Counter(x) \n",
    "counter_director.most_common(3)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 14. Кто из режиссеров снял больше всего Прибыльных фильмов?\n",
    "Варианты ответов:\n",
    "1. Steven Soderbergh\n",
    "2. Clint Eastwood\n",
    "3. Steven Spielberg\n",
    "4. Ridley Scott\n",
    "5. Christopher Nolan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Ridley Scott', 12), ('Steven Spielberg', 10), ('Clint Eastwood', 10)]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "answer_ls.append(4)\n",
    "\n",
    "data_profit = data.query('profit > 0')\n",
    "counter_director = Counter()\n",
    "for i in data_profit.director.str.split('|'):\n",
    "    counter_director += Counter(i) \n",
    "counter_director.most_common(3)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 15. Кто из режиссеров принес больше всего прибыли?\n",
    "Варианты ответов:\n",
    "1. Steven Spielberg\n",
    "2. Christopher Nolan\n",
    "3. David Yates\n",
    "4. James Cameron\n",
    "5. Peter Jackson\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "director\n",
       "Peter Jackson            5202593685\n",
       "David Yates              3379295625\n",
       "Christopher Nolan        3162548502\n",
       "J.J. Abrams              2839169916\n",
       "Michael Bay              2760938960\n",
       "                            ...    \n",
       "David Bowers|Sam Fell     -84540684\n",
       "Peter Hyams               -86956545\n",
       "Ron Underwood             -92896027\n",
       "James L. Brooks           -96289726\n",
       "Sngmoo Lee               -413912431\n",
       "Name: profit, Length: 958, dtype: int64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[('Peter Jackson', 5202593685),\n",
       " ('David Yates', 3379295625),\n",
       " ('Christopher Nolan', 3162548502)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(data.groupby(['director'])['profit'].sum().sort_values(ascending=False))\n",
    "director_profit = Counter()\n",
    "for i in range(len(data)):\n",
    "    for name in data.iloc[i].director.split('|'):\n",
    "        director_profit[name] += data.iloc[i].profit\n",
    "display(director_profit.most_common(3))       \n",
    "\n",
    "    \n",
    "answer_ls.append(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 16. Какой актер принес больше всего прибыли?\n",
    "Варианты ответов:\n",
    "1. Emma Watson\n",
    "2. Johnny Depp\n",
    "3. Michelle Rodriguez\n",
    "4. Orlando Bloom\n",
    "5. Rupert Grint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Emma Watson', 6666245597),\n",
       " ('Daniel Radcliffe', 6514990281),\n",
       " ('Rupert Grint', 6408638290)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(1)\n",
    "\n",
    "actor_profit = Counter()\n",
    "for i in range(len(data)):\n",
    "    for name in data.iloc[i].cast.split('|'):\n",
    "        actor_profit[name] += data.iloc[i].profit\n",
    "display(actor_profit.most_common(3))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 17. Какой актер принес меньше всего прибыли в 2012 году?\n",
    "Варианты ответов:\n",
    "1. Nicolas Cage\n",
    "2. Danny Huston\n",
    "3. Kirsten Dunst\n",
    "4. Jim Sturgess\n",
    "5. Sami Gayle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Kirsten Dunst', -68109207), ('Heidi Hawkins', -51893525)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(3)\n",
    "data_2012 = data.query('release_year == 2012')\n",
    "actor_profit_2012 = Counter()\n",
    "for i in range(len(data_2012)):\n",
    "    for name in data_2012.iloc[i].cast.split('|'):\n",
    "        actor_profit_2012[name] += data_2012.iloc[i].profit\n",
    "display(actor_profit_2012.most_common()[:-3:-1])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)\n",
    "Варианты ответов:\n",
    "1. Tom Cruise\n",
    "2. Mark Wahlberg \n",
    "3. Matt Damon\n",
    "4. Angelina Jolie\n",
    "5. Adam Sandler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Matt Damon', 18), ('Adam Sandler', 17), ('Angelina Jolie', 16)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(3)\n",
    "\n",
    "data_budget = data[data['budget'] > data.budget.mean()]\n",
    "counter_actor = Counter()\n",
    "for name in data_budget.cast.str.split('|'):\n",
    "        counter_actor += Counter(name)\n",
    "display(counter_actor.most_common(3))\n",
    "        \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  \n",
    "Варианты ответа:\n",
    "1. Drama\n",
    "2. Action\n",
    "3. Thriller\n",
    "4. Adventure\n",
    "5. Crime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Action', 17), ('Thriller', 15), ('Drama', 12)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(2)\n",
    "\n",
    "data_cage = data[data.cast.str.contains(\"Nicolas Cage\", na=False)]\n",
    "counter_genre = Counter()\n",
    "for genre in data_cage.genres.str.split('|'):\n",
    "        counter_genre += Counter(genre)\n",
    "display(counter_genre.most_common(3))\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 20. Какая студия сняла больше всего фильмов?\n",
    "Варианты ответа:\n",
    "1. Universal Pictures (Universal)\n",
    "2. Paramount Pictures\n",
    "3. Columbia Pictures\n",
    "4. Warner Bros\n",
    "5. Twentieth Century Fox Film Corporation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Universal Pictures', 173),\n",
       " ('Warner Bros.', 168),\n",
       " ('Paramount Pictures', 122)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(1)\n",
    "\n",
    "counter_company = Counter()\n",
    "for company in data.production_companies.str.split('|'):\n",
    "    counter_company += Counter(company)\n",
    "display(counter_company.most_common(3))\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 21. Какая студия сняла больше всего фильмов в 2015 году?\n",
    "Варианты ответа:\n",
    "1. Universal Pictures\n",
    "2. Paramount Pictures\n",
    "3. Columbia Pictures\n",
    "4. Warner Bros\n",
    "5. Twentieth Century Fox Film Corporation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Warner Bros.', 12),\n",
       " ('Universal Pictures', 10),\n",
       " ('Twentieth Century Fox Film Corporation', 8)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(4)\n",
    "\n",
    "data_2015 = data.query('release_year == 2015')\n",
    "counter_company_2015 = Counter()\n",
    "for company in data_2015.production_companies.str.split('|'):\n",
    "    counter_company_2015 += Counter(company)\n",
    "display(counter_company_2015.most_common(3))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 22. Какая студия заработала больше всего денег в жанре комедий за все время?\n",
    "Варианты ответа:\n",
    "1. Warner Bros\n",
    "2. Universal Pictures (Universal)\n",
    "3. Columbia Pictures\n",
    "4. Paramount Pictures\n",
    "5. Walt Disney"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Universal Pictures', 8961545581),\n",
       " ('Walt Disney Pictures', 7669710326),\n",
       " ('Twentieth Century Fox Film Corporation', 5686960294)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(2)\n",
    "\n",
    "data_comedy = data[data.genres.str.contains(\"Comedy\", na=False)]\n",
    "profit_company = Counter()\n",
    "for i in  range(len(data_comedy)):\n",
    "    for company in data_comedy.iloc[i].production_companies.split('|'):           \n",
    "        profit_company[company] += data_comedy.iloc[i].profit    \n",
    "display(profit_company.most_common(3))\n",
    "        \n",
    "\n",
    "        \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 23. Какая студия заработала больше всего денег в 2012 году?\n",
    "Варианты ответа:\n",
    "1. Universal Pictures (Universal)\n",
    "2. Warner Bros\n",
    "3. Columbia Pictures\n",
    "4. Paramount Pictures\n",
    "5. Lucasfilm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Columbia Pictures', 2501406608),\n",
       " ('Universal Pictures', 1981011579),\n",
       " ('Marvel Studios', 1299557910)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(3)\n",
    "\n",
    "profit_2012 = Counter()\n",
    "data_12 = data.query('release_year == 2012')\n",
    "for i in range(len(data_12)): \n",
    "    for company in data_12.iloc[i].production_companies.split('|'):\n",
    "        profit_2012[company] += data_2012.iloc[i].profit\n",
    "display(profit_2012.most_common(3))\n",
    "\n",
    "      \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 24. Самый убыточный фильм от Paramount Pictures\n",
    "Варианты ответа:\n",
    "\n",
    "1. K-19: The Widowmaker tt0267626\n",
    "2. Next tt0435705\n",
    "3. Twisted tt0315297\n",
    "4. The Love Guru tt0811138\n",
    "5. The Fighter tt0964517"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>profit</th>\n",
       "      <th>release_month</th>\n",
       "      <th>original_title_len</th>\n",
       "      <th>word_len</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>926</th>\n",
       "      <td>tt0267626</td>\n",
       "      <td>0.72233</td>\n",
       "      <td>100000000</td>\n",
       "      <td>35168966</td>\n",
       "      <td>K-19: The Widowmaker</td>\n",
       "      <td>Harrison Ford|Liam Neeson|Peter Sarsgaard|Joss...</td>\n",
       "      <td>Kathryn Bigelow</td>\n",
       "      <td>Fate has found its hero.</td>\n",
       "      <td>When Russia's first nuclear submarine malfunct...</td>\n",
       "      <td>138</td>\n",
       "      <td>Thriller|Drama|History</td>\n",
       "      <td>Paramount Pictures|Intermedia Films|National G...</td>\n",
       "      <td>7/19/2002</td>\n",
       "      <td>146</td>\n",
       "      <td>6.0</td>\n",
       "      <td>2002</td>\n",
       "      <td>-64831034</td>\n",
       "      <td>7</td>\n",
       "      <td>20</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       imdb_id  popularity     budget   revenue        original_title  \\\n",
       "926  tt0267626     0.72233  100000000  35168966  K-19: The Widowmaker   \n",
       "\n",
       "                                                  cast         director  \\\n",
       "926  Harrison Ford|Liam Neeson|Peter Sarsgaard|Joss...  Kathryn Bigelow   \n",
       "\n",
       "                      tagline  \\\n",
       "926  Fate has found its hero.   \n",
       "\n",
       "                                              overview  runtime  \\\n",
       "926  When Russia's first nuclear submarine malfunct...      138   \n",
       "\n",
       "                     genres  \\\n",
       "926  Thriller|Drama|History   \n",
       "\n",
       "                                  production_companies release_date  \\\n",
       "926  Paramount Pictures|Intermedia Films|National G...    7/19/2002   \n",
       "\n",
       "     vote_count  vote_average  release_year    profit release_month  \\\n",
       "926         146           6.0          2002 -64831034             7   \n",
       "\n",
       "     original_title_len  word_len  \n",
       "926                  20         3  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(1)\n",
    "\n",
    "data_paramount = data[data.production_companies.str.contains(\"Paramount Pictures\", na=False)]\n",
    "display(data_paramount[(data_paramount.profit == data_paramount.profit.min())])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 25. Какой Самый прибыльный год (заработали больше всего)?\n",
    "Варианты ответа:\n",
    "1. 2014\n",
    "2. 2008\n",
    "3. 2012\n",
    "4. 2002\n",
    "5. 2015"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "release_year\n",
       "2015    18668572378\n",
       "2014    16397812953\n",
       "2012    16077001687\n",
       "2013    15243179791\n",
       "2011    14730241341\n",
       "2009    13423744372\n",
       "2010    13117292530\n",
       "2008    11663881990\n",
       "2007    11565911801\n",
       "2004     9634180720\n",
       "2003     9228823312\n",
       "2002     9002361487\n",
       "2005     8981925558\n",
       "2006     8691077320\n",
       "2001     7950614865\n",
       "2000     6101399805\n",
       "Name: profit, dtype: int64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(5)\n",
    "\n",
    "display(data.groupby(['release_year'])['profit'].sum().sort_values(ascending=False))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 26. Какой Самый прибыльный год для студии Warner Bros?\n",
    "Варианты ответа:\n",
    "1. 2014\n",
    "2. 2008\n",
    "3. 2012\n",
    "4. 2010\n",
    "5. 2015"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "release_year\n",
       "2014    2295464519\n",
       "2007    2201675217\n",
       "2008    2134595031\n",
       "2010    1974712985\n",
       "2011    1871393682\n",
       "2003    1855493377\n",
       "2009    1822454136\n",
       "2013    1636453400\n",
       "2004    1631933725\n",
       "2005    1551980298\n",
       "2001    1343545668\n",
       "2012    1258020056\n",
       "2002    1022709901\n",
       "2015     870368348\n",
       "2006     620170743\n",
       "2000     452631386\n",
       "Name: profit, dtype: int64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(1)\n",
    "\n",
    "data_warner = data[data.production_companies.str.contains(\"Warner Bros\", na=False)]\n",
    "display(data_warner.groupby(['release_year'])['profit'].sum().sort_values(ascending=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 27. В каком месяце за все годы суммарно вышло больше всего фильмов?\n",
    "Варианты ответа:\n",
    "1. Январь\n",
    "2. Июнь\n",
    "3. Декабрь\n",
    "4. Сентябрь\n",
    "5. Май"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "release_month\n",
       "9     227\n",
       "12    191\n",
       "10    186\n",
       "8     161\n",
       "3     156\n",
       "4     149\n",
       "6     147\n",
       "11    146\n",
       "7     142\n",
       "5     140\n",
       "2     135\n",
       "1     110\n",
       "Name: imdb_id, dtype: int64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(4)\n",
    "\n",
    "display(data.groupby(['release_month'])['imdb_id'].count().sort_values(ascending=False))# в imbd_id все значения уникальные! \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)\n",
    "Варианты ответа:\n",
    "1. 345\n",
    "2. 450\n",
    "3. 478\n",
    "4. 523\n",
    "5. 381"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "450"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(2)\n",
    "\n",
    "data_summer = data.query('release_month in [\"6\",\"7\",\"8\"]')\n",
    "display(data_summer.imdb_id.count())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?\n",
    "Варианты ответов:\n",
    "1. Steven Soderbergh\n",
    "2. Christopher Nolan\n",
    "3. Clint Eastwood\n",
    "4. Ridley Scott\n",
    "5. Peter Jackson"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Peter Jackson', 7), ('Clint Eastwood', 6), ('Steven Soderbergh', 6)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(5)\n",
    "\n",
    "data_winter = data.query('release_month in [\"12\",\"1\",\"2\"]')\n",
    "director_count = Counter()\n",
    "for name in data_winter.director.str.split('|'):\n",
    "        director_count += Counter(name)\n",
    "display(director_count.most_common(3))\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 30. Какой месяц чаще всего по годам самый прибыльный?\n",
    "Варианты ответа:\n",
    "1. Январь\n",
    "2. Июнь\n",
    "3. Декабрь\n",
    "4. Сентябрь\n",
    "5. Май"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "release_month\n",
       "6     27551262500\n",
       "12    26563071474\n",
       "5     25039516141\n",
       "11    18654155473\n",
       "7     18307895020\n",
       "3     13720216540\n",
       "10    12994907859\n",
       "4     12876005537\n",
       "9     10878921041\n",
       "8      9640610446\n",
       "2      8854574425\n",
       "1      5396885454\n",
       "Name: profit, dtype: int64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(2)\n",
    "\n",
    "display(data.groupby(['release_month'])['profit'].sum().sort_values(ascending=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?\n",
    "Варианты ответа:\n",
    "1. Universal Pictures (Universal)\n",
    "2. Warner Bros\n",
    "3. Jim Henson Company, The\n",
    "4. Paramount Pictures\n",
    "5. Four By Two Productions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Python\\lib\\site-packages\\pandas\\core\\strings.py:1952: UserWarning: This pattern has match groups. To actually get the groups, use str.extract.\n",
      "  return func(self, *args, **kwargs)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[('Four By Two Productions', 83.0),\n",
       " ('Jim Henson Company, The', 59.0),\n",
       " ('Dos Corazones', 47.0)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(5)\n",
    "\n",
    "company_counter = Counter()\n",
    "for company in data.production_companies.str.split('|'):\n",
    "    company_counter += Counter(company)\n",
    "company_name = sorted(company_counter)\n",
    "\n",
    "len_counter = Counter()\n",
    "for name in company_name:\n",
    "    len_counter[name] += data[data.production_companies.str.contains(name, na=False)].original_title_len.mean()\n",
    "display(len_counter.most_common(3))\n",
    "# Выдает предупреждение UserWarning!!! Что это значит?\n",
    "\n",
    "            \n",
    "            \n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?\n",
    "Варианты ответа:\n",
    "1. Universal Pictures (Universal)\n",
    "2. Warner Bros\n",
    "3. Jim Henson Company, The\n",
    "4. Paramount Pictures\n",
    "5. Four By Two Productions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('Four By Two Productions', 12.0),\n",
       " ('Jim Henson Company, The', 10.0),\n",
       " ('Dos Corazones', 9.0)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(5)\n",
    "\n",
    "len_counter = Counter()\n",
    "for name in company_name:\n",
    "    len_counter[name] += data[data.production_companies.str.contains(name, na=False)].word_len.mean()\n",
    "display(len_counter.most_common(3))\n",
    "## Не понятно как считать названия с цифрами и символами! \"Пила - 5\" сколько слов?\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)\n",
    "Варианты ответа:\n",
    "1. 6540\n",
    "2. 1002\n",
    "3. 2461\n",
    "4. 28304\n",
    "5. 3432"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2461"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(3)\n",
    "\n",
    "title_list = data.original_title.str.lower().str.split().sum()\n",
    "display(len(set(title_list)))\n",
    "\n",
    "\n",
    " \n",
    "    \n",
    "\n",
    "                       \n",
    "                       \n",
    "                       \n",
    "                       \n",
    "                       \n",
    "                       \n",
    "                       \n",
    "                      \n",
    "\n",
    "\n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 34. Какие фильмы входят в 1 процент лучших по рейтингу?\n",
    "Варианты ответа:\n",
    "1. Inside Out, Gone Girl, 12 Years a Slave\n",
    "2. BloodRayne, The Adventures of Rocky & Bullwinkle\n",
    "3. The Lord of the Rings: The Return of the King\n",
    "4. 300, Lucky Number Slevin"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>imdb_id</th>\n",
       "      <th>popularity</th>\n",
       "      <th>budget</th>\n",
       "      <th>revenue</th>\n",
       "      <th>original_title</th>\n",
       "      <th>cast</th>\n",
       "      <th>director</th>\n",
       "      <th>tagline</th>\n",
       "      <th>overview</th>\n",
       "      <th>runtime</th>\n",
       "      <th>genres</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>release_date</th>\n",
       "      <th>vote_count</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>release_year</th>\n",
       "      <th>profit</th>\n",
       "      <th>release_month</th>\n",
       "      <th>original_title_len</th>\n",
       "      <th>word_len</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>tt2096673</td>\n",
       "      <td>6.326804</td>\n",
       "      <td>175000000</td>\n",
       "      <td>853708609</td>\n",
       "      <td>Inside Out</td>\n",
       "      <td>Amy Poehler|Phyllis Smith|Richard Kind|Bill Ha...</td>\n",
       "      <td>Pete Docter</td>\n",
       "      <td>Meet the little voices inside your head.</td>\n",
       "      <td>Growing up can be a bumpy road, and it's no ex...</td>\n",
       "      <td>94</td>\n",
       "      <td>Comedy|Animation|Family</td>\n",
       "      <td>Walt Disney Pictures|Pixar Animation Studios|W...</td>\n",
       "      <td>6/9/2015</td>\n",
       "      <td>3935</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2015</td>\n",
       "      <td>678708609</td>\n",
       "      <td>6</td>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>tt3170832</td>\n",
       "      <td>3.557846</td>\n",
       "      <td>6000000</td>\n",
       "      <td>35401758</td>\n",
       "      <td>Room</td>\n",
       "      <td>Brie Larson|Jacob Tremblay|Joan Allen|Sean Bri...</td>\n",
       "      <td>Lenny Abrahamson</td>\n",
       "      <td>Love knows no boundaries</td>\n",
       "      <td>Jack is a young boy of 5 years old who has liv...</td>\n",
       "      <td>117</td>\n",
       "      <td>Drama|Thriller</td>\n",
       "      <td>Element Pictures|No Trace Camping|A24|Duperele...</td>\n",
       "      <td>10/16/2015</td>\n",
       "      <td>1520</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2015</td>\n",
       "      <td>29401758</td>\n",
       "      <td>10</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>118</th>\n",
       "      <td>tt0816692</td>\n",
       "      <td>24.949134</td>\n",
       "      <td>165000000</td>\n",
       "      <td>621752480</td>\n",
       "      <td>Interstellar</td>\n",
       "      <td>Matthew McConaughey|Jessica Chastain|Anne Hath...</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Mankind was born on Earth. It was never meant ...</td>\n",
       "      <td>Interstellar chronicles the adventures of a gr...</td>\n",
       "      <td>169</td>\n",
       "      <td>Adventure|Drama|Science Fiction</td>\n",
       "      <td>Paramount Pictures|Legendary Pictures|Warner B...</td>\n",
       "      <td>11/5/2014</td>\n",
       "      <td>6498</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2014</td>\n",
       "      <td>456752480</td>\n",
       "      <td>11</td>\n",
       "      <td>12</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>119</th>\n",
       "      <td>tt2015381</td>\n",
       "      <td>14.311205</td>\n",
       "      <td>170000000</td>\n",
       "      <td>773312399</td>\n",
       "      <td>Guardians of the Galaxy</td>\n",
       "      <td>Chris Pratt|Zoe Saldana|Dave Bautista|Vin Dies...</td>\n",
       "      <td>James Gunn</td>\n",
       "      <td>All heroes start somewhere.</td>\n",
       "      <td>Light years from Earth, 26 years after being a...</td>\n",
       "      <td>121</td>\n",
       "      <td>Action|Science Fiction|Adventure</td>\n",
       "      <td>Marvel Studios|Moving Picture Company (MPC)|Bu...</td>\n",
       "      <td>7/30/2014</td>\n",
       "      <td>5612</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2014</td>\n",
       "      <td>603312399</td>\n",
       "      <td>7</td>\n",
       "      <td>23</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>125</th>\n",
       "      <td>tt2084970</td>\n",
       "      <td>8.110711</td>\n",
       "      <td>14000000</td>\n",
       "      <td>233555708</td>\n",
       "      <td>The Imitation Game</td>\n",
       "      <td>Benedict Cumberbatch|Keira Knightley|Matthew G...</td>\n",
       "      <td>Morten Tyldum</td>\n",
       "      <td>The true enigma was the man who cracked the code.</td>\n",
       "      <td>Based on the real life story of legendary cryp...</td>\n",
       "      <td>113</td>\n",
       "      <td>History|Drama|Thriller|War</td>\n",
       "      <td>Black Bear Pictures|Bristol Automotive</td>\n",
       "      <td>11/14/2014</td>\n",
       "      <td>3478</td>\n",
       "      <td>8.0</td>\n",
       "      <td>2014</td>\n",
       "      <td>219555708</td>\n",
       "      <td>11</td>\n",
       "      <td>18</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>128</th>\n",
       "      <td>tt2267998</td>\n",
       "      <td>6.438727</td>\n",
       "      <td>61000000</td>\n",
       "      <td>369330363</td>\n",
       "      <td>Gone Girl</td>\n",
       "      <td>Ben Affleck|Rosamund Pike|Carrie Coon|Neil Pat...</td>\n",
       "      <td>David Fincher</td>\n",
       "      <td>You don't know what you've got 'til it's...</td>\n",
       "      <td>With his wife's disappearance having become th...</td>\n",
       "      <td>145</td>\n",
       "      <td>Mystery|Thriller|Drama</td>\n",
       "      <td>Twentieth Century Fox Film Corporation|Regency...</td>\n",
       "      <td>10/1/2014</td>\n",
       "      <td>3720</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2014</td>\n",
       "      <td>308330363</td>\n",
       "      <td>10</td>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>138</th>\n",
       "      <td>tt2278388</td>\n",
       "      <td>4.930820</td>\n",
       "      <td>30000000</td>\n",
       "      <td>174600318</td>\n",
       "      <td>The Grand Budapest Hotel</td>\n",
       "      <td>Ralph Fiennes|Tony Revolori|F. Murray Abraham|...</td>\n",
       "      <td>Wes Anderson</td>\n",
       "      <td>A perfect holiday without leaving home.</td>\n",
       "      <td>The Grand Budapest Hotel tells of a legendary ...</td>\n",
       "      <td>99</td>\n",
       "      <td>Comedy|Drama</td>\n",
       "      <td>Fox Searchlight Pictures|Scott Rudin Productio...</td>\n",
       "      <td>2/26/2014</td>\n",
       "      <td>2802</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2014</td>\n",
       "      <td>144600318</td>\n",
       "      <td>2</td>\n",
       "      <td>24</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>370</th>\n",
       "      <td>tt1375666</td>\n",
       "      <td>9.363643</td>\n",
       "      <td>160000000</td>\n",
       "      <td>825500000</td>\n",
       "      <td>Inception</td>\n",
       "      <td>Leonardo DiCaprio|Joseph Gordon-Levitt|Ellen P...</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Your mind is the scene of the crime.</td>\n",
       "      <td>Cobb, a skilled thief who commits corporate es...</td>\n",
       "      <td>148</td>\n",
       "      <td>Action|Thriller|Science Fiction|Mystery|Adventure</td>\n",
       "      <td>Legendary Pictures|Warner Bros.|Syncopy</td>\n",
       "      <td>7/14/2010</td>\n",
       "      <td>9767</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2010</td>\n",
       "      <td>665500000</td>\n",
       "      <td>7</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>600</th>\n",
       "      <td>tt0468569</td>\n",
       "      <td>8.466668</td>\n",
       "      <td>185000000</td>\n",
       "      <td>1001921825</td>\n",
       "      <td>The Dark Knight</td>\n",
       "      <td>Christian Bale|Michael Caine|Heath Ledger|Aaro...</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Why So Serious?</td>\n",
       "      <td>Batman raises the stakes in his war on crime. ...</td>\n",
       "      <td>152</td>\n",
       "      <td>Drama|Action|Crime|Thriller</td>\n",
       "      <td>DC Comics|Legendary Pictures|Warner Bros.|Syncopy</td>\n",
       "      <td>7/16/2008</td>\n",
       "      <td>8432</td>\n",
       "      <td>8.1</td>\n",
       "      <td>2008</td>\n",
       "      <td>816921825</td>\n",
       "      <td>7</td>\n",
       "      <td>15</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>873</th>\n",
       "      <td>tt0253474</td>\n",
       "      <td>2.364204</td>\n",
       "      <td>35000000</td>\n",
       "      <td>120072577</td>\n",
       "      <td>The Pianist</td>\n",
       "      <td>Adrien Brody|Thomas Kretschmann|Frank Finlay|M...</td>\n",
       "      <td>Roman Polanski</td>\n",
       "      <td>Music was his passion. Survival was his master...</td>\n",
       "      <td>The Pianist is a film adapted from the biograp...</td>\n",
       "      <td>150</td>\n",
       "      <td>Drama|War</td>\n",
       "      <td>Bac Films|Canal+Polska|Heritage Films|Studio B...</td>\n",
       "      <td>9/24/2002</td>\n",
       "      <td>938</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2002</td>\n",
       "      <td>85072577</td>\n",
       "      <td>9</td>\n",
       "      <td>11</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1082</th>\n",
       "      <td>tt0167260</td>\n",
       "      <td>7.122455</td>\n",
       "      <td>94000000</td>\n",
       "      <td>1118888979</td>\n",
       "      <td>The Lord of the Rings: The Return of the King</td>\n",
       "      <td>Elijah Wood|Ian McKellen|Viggo Mortensen|Liv T...</td>\n",
       "      <td>Peter Jackson</td>\n",
       "      <td>The eye of the enemy is moving.</td>\n",
       "      <td>Aragorn is revealed as the heir to the ancient...</td>\n",
       "      <td>201</td>\n",
       "      <td>Adventure|Fantasy|Action</td>\n",
       "      <td>WingNut Films|New Line Cinema</td>\n",
       "      <td>12/1/2003</td>\n",
       "      <td>5636</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2003</td>\n",
       "      <td>1024888979</td>\n",
       "      <td>12</td>\n",
       "      <td>45</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1184</th>\n",
       "      <td>tt0993846</td>\n",
       "      <td>4.877927</td>\n",
       "      <td>100000000</td>\n",
       "      <td>392000694</td>\n",
       "      <td>The Wolf of Wall Street</td>\n",
       "      <td>Leonardo DiCaprio|Jonah Hill|Margot Robbie|Kyl...</td>\n",
       "      <td>Martin Scorsese</td>\n",
       "      <td>EARN. SPEND. PARTY.</td>\n",
       "      <td>A New York stockbroker refuses to cooperate in...</td>\n",
       "      <td>180</td>\n",
       "      <td>Crime|Drama|Comedy</td>\n",
       "      <td>Paramount Pictures|Appian Way|EMJAG Production...</td>\n",
       "      <td>12/25/2013</td>\n",
       "      <td>4027</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2013</td>\n",
       "      <td>292000694</td>\n",
       "      <td>12</td>\n",
       "      <td>23</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1192</th>\n",
       "      <td>tt2024544</td>\n",
       "      <td>3.625529</td>\n",
       "      <td>20000000</td>\n",
       "      <td>187000000</td>\n",
       "      <td>12 Years a Slave</td>\n",
       "      <td>Chiwetel Ejiofor|Michael Fassbender|Lupita Nyo...</td>\n",
       "      <td>Steve McQueen</td>\n",
       "      <td>The extraordinary true story of Solomon Northup</td>\n",
       "      <td>In the pre-Civil War United States, Solomon No...</td>\n",
       "      <td>134</td>\n",
       "      <td>Drama|History</td>\n",
       "      <td>Plan B Entertainment|Regency Enterprises|River...</td>\n",
       "      <td>10/18/2013</td>\n",
       "      <td>2241</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2013</td>\n",
       "      <td>167000000</td>\n",
       "      <td>10</td>\n",
       "      <td>16</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1801</th>\n",
       "      <td>tt0209144</td>\n",
       "      <td>3.095625</td>\n",
       "      <td>9000000</td>\n",
       "      <td>39723096</td>\n",
       "      <td>Memento</td>\n",
       "      <td>Guy Pearce|Carrie-Anne Moss|Joe Pantoliano|Mar...</td>\n",
       "      <td>Christopher Nolan</td>\n",
       "      <td>Some memories are best forgotten.</td>\n",
       "      <td>Suffering short-term memory loss after a head ...</td>\n",
       "      <td>113</td>\n",
       "      <td>Mystery|Thriller</td>\n",
       "      <td>Summit Entertainment|Newmarket Capital Group|T...</td>\n",
       "      <td>10/11/2000</td>\n",
       "      <td>2144</td>\n",
       "      <td>7.9</td>\n",
       "      <td>2000</td>\n",
       "      <td>30723096</td>\n",
       "      <td>10</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        imdb_id  popularity     budget     revenue  \\\n",
       "9     tt2096673    6.326804  175000000   853708609   \n",
       "34    tt3170832    3.557846    6000000    35401758   \n",
       "118   tt0816692   24.949134  165000000   621752480   \n",
       "119   tt2015381   14.311205  170000000   773312399   \n",
       "125   tt2084970    8.110711   14000000   233555708   \n",
       "128   tt2267998    6.438727   61000000   369330363   \n",
       "138   tt2278388    4.930820   30000000   174600318   \n",
       "370   tt1375666    9.363643  160000000   825500000   \n",
       "600   tt0468569    8.466668  185000000  1001921825   \n",
       "873   tt0253474    2.364204   35000000   120072577   \n",
       "1082  tt0167260    7.122455   94000000  1118888979   \n",
       "1184  tt0993846    4.877927  100000000   392000694   \n",
       "1192  tt2024544    3.625529   20000000   187000000   \n",
       "1801  tt0209144    3.095625    9000000    39723096   \n",
       "\n",
       "                                     original_title  \\\n",
       "9                                        Inside Out   \n",
       "34                                             Room   \n",
       "118                                    Interstellar   \n",
       "119                         Guardians of the Galaxy   \n",
       "125                              The Imitation Game   \n",
       "128                                       Gone Girl   \n",
       "138                        The Grand Budapest Hotel   \n",
       "370                                       Inception   \n",
       "600                                 The Dark Knight   \n",
       "873                                     The Pianist   \n",
       "1082  The Lord of the Rings: The Return of the King   \n",
       "1184                        The Wolf of Wall Street   \n",
       "1192                               12 Years a Slave   \n",
       "1801                                        Memento   \n",
       "\n",
       "                                                   cast           director  \\\n",
       "9     Amy Poehler|Phyllis Smith|Richard Kind|Bill Ha...        Pete Docter   \n",
       "34    Brie Larson|Jacob Tremblay|Joan Allen|Sean Bri...   Lenny Abrahamson   \n",
       "118   Matthew McConaughey|Jessica Chastain|Anne Hath...  Christopher Nolan   \n",
       "119   Chris Pratt|Zoe Saldana|Dave Bautista|Vin Dies...         James Gunn   \n",
       "125   Benedict Cumberbatch|Keira Knightley|Matthew G...      Morten Tyldum   \n",
       "128   Ben Affleck|Rosamund Pike|Carrie Coon|Neil Pat...      David Fincher   \n",
       "138   Ralph Fiennes|Tony Revolori|F. Murray Abraham|...       Wes Anderson   \n",
       "370   Leonardo DiCaprio|Joseph Gordon-Levitt|Ellen P...  Christopher Nolan   \n",
       "600   Christian Bale|Michael Caine|Heath Ledger|Aaro...  Christopher Nolan   \n",
       "873   Adrien Brody|Thomas Kretschmann|Frank Finlay|M...     Roman Polanski   \n",
       "1082  Elijah Wood|Ian McKellen|Viggo Mortensen|Liv T...      Peter Jackson   \n",
       "1184  Leonardo DiCaprio|Jonah Hill|Margot Robbie|Kyl...    Martin Scorsese   \n",
       "1192  Chiwetel Ejiofor|Michael Fassbender|Lupita Nyo...      Steve McQueen   \n",
       "1801  Guy Pearce|Carrie-Anne Moss|Joe Pantoliano|Mar...  Christopher Nolan   \n",
       "\n",
       "                                                tagline  \\\n",
       "9              Meet the little voices inside your head.   \n",
       "34                             Love knows no boundaries   \n",
       "118   Mankind was born on Earth. It was never meant ...   \n",
       "119                         All heroes start somewhere.   \n",
       "125   The true enigma was the man who cracked the code.   \n",
       "128         You don't know what you've got 'til it's...   \n",
       "138             A perfect holiday without leaving home.   \n",
       "370                Your mind is the scene of the crime.   \n",
       "600                                     Why So Serious?   \n",
       "873   Music was his passion. Survival was his master...   \n",
       "1082                    The eye of the enemy is moving.   \n",
       "1184                                EARN. SPEND. PARTY.   \n",
       "1192    The extraordinary true story of Solomon Northup   \n",
       "1801                  Some memories are best forgotten.   \n",
       "\n",
       "                                               overview  runtime  \\\n",
       "9     Growing up can be a bumpy road, and it's no ex...       94   \n",
       "34    Jack is a young boy of 5 years old who has liv...      117   \n",
       "118   Interstellar chronicles the adventures of a gr...      169   \n",
       "119   Light years from Earth, 26 years after being a...      121   \n",
       "125   Based on the real life story of legendary cryp...      113   \n",
       "128   With his wife's disappearance having become th...      145   \n",
       "138   The Grand Budapest Hotel tells of a legendary ...       99   \n",
       "370   Cobb, a skilled thief who commits corporate es...      148   \n",
       "600   Batman raises the stakes in his war on crime. ...      152   \n",
       "873   The Pianist is a film adapted from the biograp...      150   \n",
       "1082  Aragorn is revealed as the heir to the ancient...      201   \n",
       "1184  A New York stockbroker refuses to cooperate in...      180   \n",
       "1192  In the pre-Civil War United States, Solomon No...      134   \n",
       "1801  Suffering short-term memory loss after a head ...      113   \n",
       "\n",
       "                                                 genres  \\\n",
       "9                               Comedy|Animation|Family   \n",
       "34                                       Drama|Thriller   \n",
       "118                     Adventure|Drama|Science Fiction   \n",
       "119                    Action|Science Fiction|Adventure   \n",
       "125                          History|Drama|Thriller|War   \n",
       "128                              Mystery|Thriller|Drama   \n",
       "138                                        Comedy|Drama   \n",
       "370   Action|Thriller|Science Fiction|Mystery|Adventure   \n",
       "600                         Drama|Action|Crime|Thriller   \n",
       "873                                           Drama|War   \n",
       "1082                           Adventure|Fantasy|Action   \n",
       "1184                                 Crime|Drama|Comedy   \n",
       "1192                                      Drama|History   \n",
       "1801                                   Mystery|Thriller   \n",
       "\n",
       "                                   production_companies release_date  \\\n",
       "9     Walt Disney Pictures|Pixar Animation Studios|W...     6/9/2015   \n",
       "34    Element Pictures|No Trace Camping|A24|Duperele...   10/16/2015   \n",
       "118   Paramount Pictures|Legendary Pictures|Warner B...    11/5/2014   \n",
       "119   Marvel Studios|Moving Picture Company (MPC)|Bu...    7/30/2014   \n",
       "125              Black Bear Pictures|Bristol Automotive   11/14/2014   \n",
       "128   Twentieth Century Fox Film Corporation|Regency...    10/1/2014   \n",
       "138   Fox Searchlight Pictures|Scott Rudin Productio...    2/26/2014   \n",
       "370             Legendary Pictures|Warner Bros.|Syncopy    7/14/2010   \n",
       "600   DC Comics|Legendary Pictures|Warner Bros.|Syncopy    7/16/2008   \n",
       "873   Bac Films|Canal+Polska|Heritage Films|Studio B...    9/24/2002   \n",
       "1082                      WingNut Films|New Line Cinema    12/1/2003   \n",
       "1184  Paramount Pictures|Appian Way|EMJAG Production...   12/25/2013   \n",
       "1192  Plan B Entertainment|Regency Enterprises|River...   10/18/2013   \n",
       "1801  Summit Entertainment|Newmarket Capital Group|T...   10/11/2000   \n",
       "\n",
       "      vote_count  vote_average  release_year      profit release_month  \\\n",
       "9           3935           8.0          2015   678708609             6   \n",
       "34          1520           8.0          2015    29401758            10   \n",
       "118         6498           8.0          2014   456752480            11   \n",
       "119         5612           7.9          2014   603312399             7   \n",
       "125         3478           8.0          2014   219555708            11   \n",
       "128         3720           7.9          2014   308330363            10   \n",
       "138         2802           7.9          2014   144600318             2   \n",
       "370         9767           7.9          2010   665500000             7   \n",
       "600         8432           8.1          2008   816921825             7   \n",
       "873          938           7.9          2002    85072577             9   \n",
       "1082        5636           7.9          2003  1024888979            12   \n",
       "1184        4027           7.9          2013   292000694            12   \n",
       "1192        2241           7.9          2013   167000000            10   \n",
       "1801        2144           7.9          2000    30723096            10   \n",
       "\n",
       "      original_title_len  word_len  \n",
       "9                     10         2  \n",
       "34                     4         1  \n",
       "118                   12         1  \n",
       "119                   23         4  \n",
       "125                   18         3  \n",
       "128                    9         2  \n",
       "138                   24         4  \n",
       "370                    9         1  \n",
       "600                   15         3  \n",
       "873                   11         2  \n",
       "1082                  45        10  \n",
       "1184                  23         5  \n",
       "1192                  16         4  \n",
       "1801                   7         1  "
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "answer_ls.append(1)\n",
    "\n",
    "data[(data.vote_average > np.percentile(data['vote_average'], 99))]\n",
    "              "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 35. Какие актеры чаще всего снимаются в одном фильме вместе\n",
    "Варианты ответа:\n",
    "1. Johnny Depp & Helena Bonham Carter\n",
    "2. Hugh Jackman & Ian McKellen\n",
    "3. Vin Diesel & Paul Walker\n",
    "4. Adam Sandler & Kevin James\n",
    "5. Daniel Radcliffe & Rupert Grint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(5)\n",
    "\n",
    "def cast_friendly(actor_1,actor_2): #Принимает имена актеров\n",
    "    result =len(data[data.cast.str.contains(actor_1) & data.cast.str.contains(actor_2)])\n",
    "    return result\n",
    "\n",
    "display(cast_friendly('Johnny Depp', 'Helena Bonham Carter'))\n",
    "display(cast_friendly('Hugh Jackman', 'Ian McKellen'))\n",
    "display(cast_friendly('Vin Diesel',  'Paul Walker'))\n",
    "display(cast_friendly('Adam Sandler', 'Kevin James'))\n",
    "display(cast_friendly('Daniel Radcliffe', 'Rupert Grint'))\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101\n",
    "Варианты ответа:\n",
    "1. Quentin Tarantino\n",
    "2. Steven Soderbergh\n",
    "3. Robert Rodriguez\n",
    "4. Christopher Nolan\n",
    "5. Clint Eastwood"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "85.71428571428571"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "76.92307692307692"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "72.72727272727273"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "100.0"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "83.33333333333333"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "answer_ls.append(4)\n",
    "\n",
    "#У какого из режиссеров самый высокий процент фильмов со сборами выше бюджета? Так написано в викторине!!!\n",
    "def profit_probability(director): # Прогнал все имена через цикл - много 100%. Решил вводить ручками из заданных.\n",
    "    total_film = data[(data.director.str.contains(director))]\n",
    "    profitable_film = total_film[(total_film.profit > 0)]\n",
    "    result = len(profitable_film) * 100 / len(total_film)\n",
    "    return result    \n",
    "\n",
    "display(profit_probability('Quentin Tarantino'))\n",
    "display(profit_probability('Steven Soderbergh'))\n",
    "display(profit_probability('Robert Rodriguez'))\n",
    "display(profit_probability('Christopher Nolan'))\n",
    "display(profit_probability('Clint Eastwood'))\n",
    "\n",
    "\n",
    "    \n",
    "    \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Submission"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "36"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(answer_ls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Id</th>\n",
       "      <th>Answer</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>11</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>12</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>13</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>14</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>15</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>16</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>17</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>18</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>19</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>21</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>22</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>23</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>24</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>25</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>26</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>27</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>28</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>29</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>30</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>31</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>32</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>33</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>34</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>35</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>36</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Id  Answer\n",
       "0    1       4\n",
       "1    2       2\n",
       "2    3       3\n",
       "3    4       2\n",
       "4    5       1\n",
       "5    6       5\n",
       "6    7       2\n",
       "7    8       1\n",
       "8    9       4\n",
       "9   10       5\n",
       "10  11       5\n",
       "11  12       1\n",
       "12  13       3\n",
       "13  14       4\n",
       "14  15       5\n",
       "15  16       1\n",
       "16  17       3\n",
       "17  18       3\n",
       "18  19       2\n",
       "19  20       1\n",
       "20  21       4\n",
       "21  22       2\n",
       "22  23       3\n",
       "23  24       1\n",
       "24  25       5\n",
       "25  26       1\n",
       "26  27       4\n",
       "27  28       2\n",
       "28  29       5\n",
       "29  30       2\n",
       "30  31       5\n",
       "31  32       5\n",
       "32  33       3\n",
       "33  34       1\n",
       "34  35       5\n",
       "35  36       4"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
