import json

filedata = {'lines-of-code':37, 'lines':50, 'methods':7,
            'classes':3, 'files':3, 'dictories':3, 'comment-lines': 13,
            'comments': 0.26, 'time-range': ['2018-05-08', '2018-05-15'],
            'authors': ['AAA', 'BBB', 'CCC']}

methods = [{'name': 'main', 'class': 'api', 'file': 'apt.java',
            'directory': 'Java/API', 'lines': 5, 'bugs': [], 'MID': '0',
            'related': [1], 'relations': [5]},
           {'name': 'reverseString', 'class': 'api', 'file': 'apt.java',
            'directory': 'Java/API', 'lines': 6, 'bugs': [], 'MID': '1',
            'related': [], 'relations': []},
           {'name': 'main', 'class': 'database', 'file': 'database.java',
            'directory': 'Java/Database', 'lines': 5, 'bugs': [4], 'MID': '2',
            'related': [0,3], 'relations': [3,4]}, 
           {'name': 'calculateArea', 'class': 'sensor', 'file': 'sensor.java',
            'directory': 'Java/Sensor', 'lines': 3, 'bugs': [], 'MID': '3',
            'related': [6], 'relations': [0]},
           {'name': 'calculateArea', 'class': 'sensor', 'file': 'sensor.java',
            'directory': 'Java/Sensor', 'lines': 3, 'bugs': [], 'MID': '4',
            'related': [6], 'relations': [1]},
           {'name': 'calculateArea', 'class': 'sensor', 'file': 'sensor.java',
            'directory': 'Java/Sensor', 'lines': 4, 'bugs': [], 'MID': '5',
            'related': [6], 'relations': [2]},
           {'name': 'main', 'class': 'sensor', 'file': 'sensor.java',
            'directory': 'Java/Sensor', 'lines': 18, 'bugs': [2,12], 'MID': '6',
            'related': [], 'relations': []}]
relations = {'0': {'from':6, 'to':3},
             '1': {'from':6, 'to':4},
             '2': {'from':6, 'to':5},
             '3': {'from':3, 'to':2},
             '4': {'from':0, 'to':2},
             '5': {'from':1, 'to':0}}
git = { '0': [
            {'author':'AAA', 'time':'2018-05-08 12:32:32', 'comment':'zxcas','GID':'1b'},
            {'author':'CCC', 'time':'2018-05-12 12:32:32', 'comment':'dasfe','GID':'3c'},
            {'author':'AAA', 'time':'2018-05-13 12:32:32', 'comment':'qwreqwr','GID':'5c'}
        ],
        '1': [
            {'author':'AAA', 'time':'2018-05-10 12:32:32', 'comment':'rsddtgs','GID':'8j'}
        ],
        '2': [
            {'author':'BBB', 'time':'2018-05-08 12:32:32', 'comment':'trey','GID':'7k'},
            {'author':'BBB', 'time':'2018-05-10 12:32:32', 'comment':'ghffgh','GID':'3f'},
            {'author':'BBB', 'time':'2018-05-15 12:32:32', 'comment':'wrfef','GID':'5k'}
        ],
        '3' :[
            {'author':'AAA', 'time':'2018-05-11 12:32:32', 'comment':'8i87o','GID':'9h'}
        ],
        '4' :[
            {'author':'BBB', 'time':'2018-05-11 08:32:12', 'comment':'dsfgg','GID':'4v'}
        ],
        '5' :[
            {'author':'CCC', 'time':'2018-05-11 03:42:31', 'comment':'asfdsg','GID':'9o'}
        ],
        '6' :[
            {'author':'AAA', 'time':'2018-05-08 03:42:31', 'comment':'x','GID':'1d'},
            {'author':'CCC', 'time':'2018-05-11 08:32:12', 'comment':'cer2w','GID':'5p'},
            {'author':'BBB', 'time':'2018-05-15 08:32:12', 'comment':'gdfg6','GID':'8d'},
        ]
    }
force = {'nodes':[], 'links':[]}
for each in methods:
    node = {'id': each['name'], 'group': each['class'], 'data': each, 'MID': each['MID']}
    force['nodes'].append(node)

for each in relations:
    link = {'source': relations[each]['from'], 'target': relations[each]['to'], 'value':1, 'RID': each}
    force['links'].append(link)

bugs = {'methods':[], 'relations':[]}
for each in methods:
    if len(each['bugs']) == 0:
        continue
    else:
        bugs['methods'].append(each['MID'])
        for related in each['related']:
            if related not in bugs['methods']:
                bugs['methods'].append(related)
        for relation in each['relations']:
            if relation not in bugs['relations']:
                bugs['relations'].append(relations)
                
groupby = {'class':{}, 'file':{}, 'directory':{}, 'author': {}}
for each in methods:
    if each['class'] not in groupby['class']:
        groupby['class'][each['class']] = []
    if each['file'] not in groupby['file']:
        groupby['file'][each['file']] = []
    if each['directory'] not in groupby['directory']:
        groupby['directory'][each['directory']] = []
    groupby['class'][each['class']].append(each['MID'])
    groupby['file'][each['file']].append(each['MID'])
    groupby['directory'][each['directory']].append(each['MID'])
    if len(git[each['MID']]) == 0:
        continue
    else:
        for commit in git[each['MID']]:
            if commit['author'] not in groupby['author']:
                groupby['author'] = []
            groupby['author'].append(each['MID'])


data = {'filedata': filedata, 'force': force, 'bugs': bugs, 'groupby': groupby, 'git':git}
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)







    
