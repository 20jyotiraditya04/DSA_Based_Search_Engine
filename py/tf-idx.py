
from logging.config import dictConfig
import operator
import numpy as np
import re
import string
import json
import os
from gensim.parsing.preprocessing import remove_stopwords,STOPWORDS
all_stopwords= STOPWORDS.union(set(['cses','input','output','example','testcase','submit','leetcode','codeforces','codechef','chef','code']),set(string.ascii_lowercase),set(string.punctuation),set(string.digits),set(string.ascii_uppercase),set(string.printable),set(string.hexdigits))
#bm25 params
k=1.25
b=0.75
file_names = open(os.path.join(os.path.dirname(__file__), 'prob_names.txt'), 'r').read().split('\n')
file_names = set([fn for fn in file_names if fn.strip()])
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Database'))
unique_keywords=[]
with open('uniqueKeys.json','r') as uk:
    unique_keywords=json.load(uk)
idx=[]
with open('idx_vec.json','r') as dx:
    idx=json.load(dx)

d=0
N=0
for file_name in file_names:
    # Ensure file_name ends with .txt
    if not file_name.endswith('.txt'):
        file_name_with_ext = file_name + '.txt'
    else:
        file_name_with_ext = file_name
    file_path = os.path.join(data_path, file_name_with_ext)
    if os.path.exists(file_path):
        print(f"Found: {file_path}")
        N += 1
        keywords = re.findall(r"[\w']+", open(file_path, 'r').read().lower())
        keywords = [word for word in keywords if not word in all_stopwords]
        d = d + len(keywords)
    else:
        print(f"Missing: {file_path}")
print(f"Total found: {N}")
davg=d/N

d=dict.fromkeys([name for name in file_names],[])
for file_name in file_names:
    if os.path.exists(data_path+file_name+'.txt'):
        keywords = re.findall(r"[\w']+", open(data_path+file_name+'.txt','r').read().lower())
        keywords = [word for word in keywords if not word in all_stopwords]
        temp = []
        for id, word in enumerate(unique_keywords):
            cnt = keywords.count(word) > 0
            if cnt > 0:
                temp.append([id, cnt * idx[id] * (k + 1)])
        if len(temp) > 0:
            for i in range(len(temp)):
                temp[i][1] = temp[i][1] / (len(temp) + k * (1 - b + b * (len(keywords) / davg)))
        # for i in range(len(temp)):
        #     temp[i][1]*=idx[temp[i][0]]
        d[file_name] = temp
print(len(file_names),len(d))
            
with open('tf-idf.json','w') as fi:
    json.dump(d,fi)
# d={}
# with open('tf-idf.json','r') as tf:
#     d=json.load(tf)
# print(len(d))

# print(d['Maximum Subarray Sum'][864])