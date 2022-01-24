# %% [markdown]
# importing necessary libs

# %%
import re
from sys import displayhook
import numpy as np
import pandas as pd
import datetime as dt
import regex
from datetime import *

# %%
def startsWithDateAndTime(s):
    pattern = '^([0-9]+)(/)([0-9]+)(/)([0-9][0-9]), ([0-9]+):([0-9][0-9]) (AM|PM) -'
    result = re.match(pattern, s)
    if result:
        return True
        return False

# %%
def findAuthor(s):
    patterns=[
        '([w]+):',
        '([w]+[s]+[w]:',
        '([+]d{2} d{5} d{5}):',
        '([w]+)[u263a-U0001f999]+:',
    ]
    pattern = '^' + '|'.join(patterns)
    result = re.match(pattern, s)
    if result:
        return True
    return False

# %%
def getdatapoint(line):
    splitline = line.split('--')
    DateTime = splitline[0]
    date, time = datetime.split(',')
    message = ' '.join(splitline[1:])
    if findAuthor(message):
        splitmessage =  message.split(': -')
        author = splitmessage[0]
        message = ' '.join(splitmessage[1:])
    else:
        author = None
        return date, time, author, message

# %%
parsedata = []
filepath = 'D:\Python-whatsapp-data-analytics\WhatsApp Chat with MIT BENGALURU.txt'
with open(filepath, encoding="utf-8") as fp:
    fp.readline()
    buffer = []
    date, time, author = None, None, None
    while True :
        line = fp.readline()
        if not line:
            break
        line = line.strip()
        if startsWithDateAndTime(line):
            if len(buffer) > 0:
                parsedata.append([date, time, author, ' '.join(buffer)])
                buffer.clear() 
                date, time, author, message = getdatapoint(line)
                buffer.append(message)
            else:
                buffer.append(line)
df = pd.DataFrame(parsedata, columns=['Date', 'Time', 'Author', 'Message'])
df["Date"] = pd.to_datetime(df["Date"])
print(df)


-