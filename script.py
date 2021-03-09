category = {
    '家人': [],
    '师生': [],
    '朋友': [],
    '同事': [],
}

# 1
family = ['丈夫', '妻子', '父亲', '母亲', '儿子', '女儿']
# 2
school = ['附中同学', '学生', '老师', '同学']
# 3
friend = []
# 4
workmate = ['同事']

categoryArray = [{ "name": "核心人物" }, { "name": "家人" }, { "name": "学校" }, { "name": "朋友" }, { "name": "同事" }]

import pandas as pd

df = pd.read_csv('data/relation.csv', sep=',')
col1 = list(df['人物1'])
col2 = list(df['人物2'])
col3 = list(df['关系'])
print(col1, len(col1))
print(col2, len(col2))

nodes_people = [] # {"name": category}
links_people = []
nodes_people.append({"name": '曹国昌', "category": 0, "value": 10})

uu = 0
while uu < len(col1):
    if col1[uu] == '曹国昌':
        if col3[uu]:
            if col3[uu] in family:
                nodes_people.append({ "name": col2[uu], "category": 1, "value": 1})
            if col3[uu] in school:
                nodes_people.append({ "name": col2[uu], "category": 2, "value": 1})
            if col3[uu] in friend:
                nodes_people.append({ "name": col2[uu], "category": 3, "value": 1})
            if col3[uu] in workmate:
                nodes_people.append({ "name": col2[uu], "category": 4, "value": 1})

        links_people.append({ "source": col2[uu], "target": col1[uu], "weight": 1, "name": col3[uu]})
    uu += 1
    
print(nodes_people)
print(links_people)