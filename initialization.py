"""
This file provide global initialization.
If it is executed, all the perameters will be reseted.
"""

import sqlite3
import random

con = sqlite3.connect('generalAI.db')
con.execute("create table if not exists emotion(parameter_name, value)")
# con.execute("delete from emotion").rowcount ##delete the old data
emotion=[
    ('select_rate',random.random()*100),
    ('pleasure_value',0),
    ('strength', random.random()*100),
    ('stable', random.random()*100),
    ('change_fun', random.randint(0,5))
]

con.executemany("insert into emotion(parameter_name, value) values (?, ?)", emotion)
con.commit()
para=dict(con.execute("select * from emotion"))
print(para)

# for row in con.execute("select parameter_name, value from emotion"):
#     print(row)



