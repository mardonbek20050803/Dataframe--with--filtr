# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wm0NGbqF09B5te4KlQSf-wbzOPH14yk4
"""

import pandas as pd
malumot={
    "FISH":[ "Tursunov Mardonbek","Rasulov Omatbek", "Qambbarov SAmandar","Rasulova Odina","Axmatov SHohruh","Tursunova Marjona","Inomjonov Muhammadsher","Soliyeva Nigora" ],
    "Yoshi":["12","14","16","15","13","17","18","19" ],
    "jinsi":["o'g'il bola","o'g'il bola","o'g'il bola","qiz bola","o'g'il bola","qiz bola","o'g'il bola","qiz bola"   ],
    "maktab raqami":[ "10","13","15","16","17","34","40","50"  ]
}
df=pd.DataFrame(malumot)
print(df)

filtr=df.loc[df["jinsi"]=="qiz bola"]
print(filtr)

filtr=df.loc[df["jinsi"]=="o'g'il bola"]
print(filtr)



filtr=df.loc[df["jinsi"]=="o'g'il bola"]&(filtr=)
print(filtr)