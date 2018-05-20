
filedata = {'lines-of-code':37, 'lines':50, 'method':7,
            'class':3, 'file':3, 'directory':2, 'comment-lines': 13,
            'comments': '26%', 'time-range': ['2018-05-08', '2018-05-15'],
            'author': ['AAA', 'BBB', 'CCC'], 'bug':3}

methods = {'0':{'name': 'main', 'class': 'api', 'file': 'apt.java',
            'directory': 'Java/API', 'lines': 5, 'bugs': [], 'MID': '0',
            'related': [1], 'relations': [5]},
          }
relations = {'0': {'from':'6', 'to':'3'}
            }
git = { '6' :[
            {'author':'AAA', 'time':'2018-05-08 03:42:31', 'comment':'x','GID':'1d'},
            {'author':'CCC', 'time':'2018-05-11 08:32:12', 'comment':'cer2w','GID':'5p'},
            {'author':'BBB', 'time':'2018-05-15 08:32:12', 'comment':'gdfg6','GID':'8d'},
        ]
    }

#==================================
import json

bugs = []
for each in methods:
    each = methods[each]
    if len(each['bugs']) != 0:
        bugs.append(each['MID'])
        
force = {'nodes':[], 'links':[]}
for each in methods:
    bug = each in bugs
    each = methods[each]
    node = {'id': each['MID'], 'bug': bug, 'data': each}
    force['nodes'].append(node)

for each in relations:
    bug = relations[each]['from'] in bugs
    link = {'source': relations[each]['from'], 'target': relations[each]['to'], 'bug': bug}
    force['links'].append(link)
                
groupby = {'class':{}, 'file':{}, 'directory':{}, 'author': {}}
for each in methods:
    each = methods[each]
    if each['class'] not in groupby['class']:
        groupby['class'][each['class']] = []
    if each['file'] not in groupby['file']:
        groupby['file'][each['file']] = []
    if each['directory'] not in groupby['directory']:
        groupby['directory'][each['directory']] = []
    groupby['class'][each['class']].append(each['MID'])
    groupby['file'][each['file']].append(each['MID'])
    groupby['directory'][each['directory']].append(each['MID'])

for each in git:
    if len(git[each]) != 0:
        for commit in git[each]:
            if commit['author'] not in groupby['author']:
                groupby['author'][commit['author']] = []
            if each not in groupby['author'][commit['author']]:
                groupby['author'][commit['author']].append(each)

#namelist = {}
#for each in methods:
#    each = methods[each]
#    if each['name'] not in namelist:
#        namelist[each['name']] = each['MID']

data = {'filedata': filedata, 'force': force, 'groupby': groupby, 'git':git}
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)







    
