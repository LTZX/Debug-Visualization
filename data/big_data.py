filedata = {'lines-of-code':288, 'lines':376, 'method':28,
            'class':11, 'file':12, 'directory':5, 'comment-lines': 15,
            'comments': '5.0%', 'time-range': ['2018-05-08', '2018-06-15'],
            'author': ['zhiyi', 'xiaojie', 'yumeng','ruolan'], 'bug':8}

methods = {'0':{'name': 'main', 'class': 'Application', 'file': 'Application.java',
            'directory': '/java', 'lines': 3, 'bugs': [], 'MID': '1',
            'related': [], 'relations': []},

           '1':{'name': 'start', 'class': 'Application', 'file': 'Application.java',
            'directory': '/java', 'lines': 12, 'bugs': [], 'MID': '2',
            'related': [], 'relations': []},

           '3':{'name': 'stop', 'class': 'Application', 'file': 'Application.java',
            'directory': '/java', 'lines': 3, 'bugs': [], 'MID': '3',
            'related': [], 'relations': []},

           '4':{'name': 'OpenUrl', 'class': 'AddSensorUrl', 'file': 'AddSensorUrl.java',
            'directory': '/java/API', 'lines': 9, 'bugs': [3], 'MID': '4',
            'related': [2], 'relations': [0]},

           '5':{'name': 'Interact', 'class': 'AddSensorUrl', 'file': 'AddSensorUrl.java',
            'directory': '/java/API', 'lines': 5, 'bugs': [], 'MID': '5',
            'related': [4], 'relations': [5]},

           '6':{'name': 'OpenUrl', 'class': 'DeleteSensorUrl', 'file': 'DeleteSensorUrl.java',
            'directory': '/java/API', 'lines': 9, 'bugs': [3], 'MID': '6',
            'related': [2], 'relations': [1]},

           '7':{'name': 'Interact', 'class': 'DeleteSensorUrl', 'file': 'DeleteSensorUrl.java',
            'directory': '/java/API', 'lines': 5, 'bugs': [], 'MID': '7',
            'related': [6], 'relations': [6]},

           '8':{'name': 'OpenUrl', 'class': 'GetAllSensorsUrl', 'file': 'GetAllSensorsUrl.java',
            'directory': '/java/API', 'lines': 9, 'bugs': [3], 'MID': '8',
            'related': [2], 'relations': [2]},

           '9':{'name': 'Interact', 'class': 'GetAllSensorsUrl', 'file': 'GetAllSensorsUrl.java',
            'directory': '/java/API', 'lines': 5, 'bugs': [], 'MID': '9',
            'related': [8], 'relations': [7]},

           '10':{'name': 'OpenUrl', 'class': 'GetSensorDataUrl', 'file': 'GetSensorDataUrl.java',
            'directory': '/java/API', 'lines': 9, 'bugs': [3], 'MID': '10',
            'related': [2], 'relations': [3]},

           '11':{'name': 'Interact', 'class': 'GetSensorDataUrl', 'file': 'GetSensorDataUrl.java',
            'directory': '/java/API', 'lines': 4, 'bugs': [], 'MID': '11',
            'related': [10], 'relations': [8]},

           '12':{'name': 'OpenUrl', 'class': 'PostSensorDataUrl', 'file': 'PostSensorDataUrl.java',
            'directory': '/java/API', 'lines': 9, 'bugs': [3], 'MID': '12',
            'related': [2], 'relations': [4]},

           '13':{'name': 'Interact', 'class': 'PostSensorDataUrl', 'file': 'PostSensorDataUrl.java',
            'directory': '/java/API', 'lines': 5, 'bugs': [], 'MID': '13',
            'related': [12], 'relations': [9]},

           '14':{'name': 'DatabaseState', 'class': '[]', 'file': 'DataBaseState.java',
            'directory': '/java/database', 'lines': 4, 'bugs': [], 'MID': '14',
            'related': [], 'relations': []},

           '15':{'name': 'DBConnector', 'class': 'DBConnector', 'file': 'DBConnector.java',
            'directory': '/java/database', 'lines': 15, 'bugs': [9,12], 'MID': '15',
            'related': [], 'relations': []},

           '16':{'name': 'insert', 'class': 'DBConnector', 'file': 'DBConnector.java',
            'directory': '/java/database', 'lines': 7, 'bugs': [], 'MID': '16',
            'related': [23], 'relations': [15]},

           '17':{'name': 'find', 'class': 'DBConnector', 'file': 'DBConnector.java',
            'directory': '/java/database', 'lines': 12, 'bugs': [10], 'MID': '17',
            'related': [21], 'relations': [19]},

           '18':{'name': 'Read', 'class': 'DBConnector', 'file': 'DBConnector.java',
            'directory': '/java/database', 'lines': 3, 'bugs': [], 'MID': '18',
            'related': [26], 'relations': [18]},

           '19':{'name': 'Update', 'class': 'DBConnector', 'file': 'DBConnector.java',
            'directory': '/java/database', 'lines': 3, 'bugs': [], 'MID': '19',
            'related': [24], 'relations': [16]},

           '20':{'name': 'Delete', 'class': 'DBConnector', 'file': 'DBConnector.java',
            'directory': '/java/database', 'lines': 3, 'bugs': [], 'MID': '20',
            'related': [25], 'relations': [17]},

           '21':{'name': 'GetSensorData', 'class': 'SensorRoute', 'file': 'SensorRoute.java',
            'directory': '/java/Sonsors', 'lines': 7, 'bugs': [], 'MID': '21',
            'related': [11], 'relations': [13]},

           '22':{'name': 'UpdateSensorData', 'class': 'SensorRoute', 'file': 'SensorRoute.java',
            'directory': '/java/Sonsors', 'lines': 7, 'bugs': [], 'MID': '22',
            'related': [13], 'relations': [14]},

           '23':{'name': 'AddSensor', 'class': 'SensorRoute', 'file': 'SensorRoute.java',
            'directory': '/java/Sonsors', 'lines': 4, 'bugs': [], 'MID': '23',
            'related': [5], 'relations': [10]},

           '24':{'name': 'UpdateSensor', 'class': 'SensorRoute', 'file': 'SensorRoute.java',
            'directory': '/java/Sonsors', 'lines': 4, 'bugs': [], 'MID': '24',
            'related': [], 'relations': []},

           '25':{'name': 'DeleteSensor', 'class': 'SensorRoute', 'file': 'SensorRoute.java',
            'directory': '/java/Sonsors', 'lines': 4, 'bugs': [], 'MID': '25',
            'related': [7], 'relations': [11]},

           '26':{'name': 'GetAllSensors', 'class': 'SensorRoute.java', 'file': 'SensorRoute.java',
            'directory': '/java/Sonsors', 'lines': 4, 'bugs': [], 'MID': '26',
            'related': [9], 'relations': [12]}
          }
relations = {'0': {'from':'2', 'to':'4'},
             '1': {'from':'2', 'to':'6'},
             '2': {'from':'2', 'to':'8'},
             '3': {'from':'2', 'to':'10'},
             '4': {'from':'2', 'to':'12'},
             '5': {'from':'4', 'to':'5'},
             '6': {'from':'6', 'to':'7'},
             '7': {'from':'8', 'to':'9'},
             '8': {'from':'10', 'to':'11'},
             '9': {'from':'12', 'to':'13'},
             '10': {'from':'5', 'to':'23'},
             '11': {'from':'7', 'to':'25'},
             '12': {'from':'9', 'to':'26'},
             '13': {'from':'11', 'to':'21'},
             '14': {'from':'13', 'to':'22'},
             '15': {'from':'23', 'to':'16'},
             '16': {'from':'24', 'to':'19'},
             '17': {'from':'25', 'to':'20'},
             '18': {'from':'26', 'to':'18'},
             '19': {'from':'21', 'to':'17'},
             '20': {'from':'22', 'to':'16'}
            }

git = { '0': [
            {'author':'ruolan', 'time':'2018-05-08 12:32:32', 'comment':'zxcas','GID':'1b'},
            {'author':'xiaoju', 'time':'2018-05-12 12:32:32', 'comment':'dasfe','GID':'3c'},
            {'author':'ruolan', 'time':'2018-05-13 12:32:32', 'comment':'qwreqwr','GID':'5c'}
        ],
        '1': [
            {'author':'yumeng', 'time':'2018-05-10 12:32:32', 'comment':'rsddtgs','GID':'8j'}
        ],
        '2': [
            {'author':'zhiyi', 'time':'2018-05-08 12:32:32', 'comment':'trey','GID':'7k'},
            {'author':'zhiyi', 'time':'2018-05-10 12:32:32', 'comment':'ghffgh','GID':'3f'},
            {'author':'yumeng', 'time':'2018-05-15 12:32:32', 'comment':'wrfef','GID':'5k'}
        ],
        '3' :[
            {'author':'ruolan', 'time':'2018-05-11 12:32:32', 'comment':'8i87o','GID':'9h'}
        ],
        '4' :[
            {'author':'zhiyi', 'time':'2018-05-11 08:32:12', 'comment':'dsfgg','GID':'4v'}
        ],
        '5' :[
            {'author':'xiaoju', 'time':'2018-05-11 03:42:31', 'comment':'asfdsg','GID':'9o'}
        ],
        '6' :[
            {'author':'ruolan', 'time':'2018-05-08 03:42:31', 'comment':'x','GID':'1d'},
            {'author':'xiaoju', 'time':'2018-05-11 08:32:12', 'comment':'cer2w','GID':'5p'},
            {'author':'zhiyi', 'time':'2018-05-15 08:32:12', 'comment':'gdfg6','GID':'8d'},
        ],
        '7' :[
            {'author':'ruolan', 'time':'2018-06-08 12:32:32', 'comment':'zxcase','GID':'1a'},
            {'author':'xiaoju', 'time':'2018-06-12 12:32:32', 'comment':'dasfee','GID':'3b'},
            {'author':'ruolan', 'time':'2018-06-13 12:32:32', 'comment':'qwreqwre','GID':'5b'}
        ],
        '8': [
            {'author':'yumeng', 'time':'2018-06-10 12:32:32', 'comment':'rsddtgse','GID':'8c'}
        ],
        '9': [
            {'author':'yumeng', 'time':'2018-06-08 12:32:32', 'comment':'treye','GID':'7d'},
            {'author':'yumeng', 'time':'2018-06-10 12:32:32', 'comment':'ghffghe','GID':'3e'},
            {'author':'zhiyi', 'time':'2018-06-15 12:32:32', 'comment':'wrfefe','GID':'5f'}
        ],
        '10' :[
            {'author':'ruolan', 'time':'2018-06-11 12:32:32', 'comment':'8i87oe','GID':'9g'}
        ],
        '11' :[
            {'author':'zhiyi', 'time':'2018-06-11 08:32:12', 'comment':'dsfgge','GID':'4h'}
        ],
        '12' :[
            {'author':'xiaoju', 'time':'2018-06-11 03:42:31', 'comment':'asfdsge','GID':'9i'}
        ],
        '13' :[
            {'author':'ruolan', 'time':'2018-06-08 03:42:31', 'comment':'xe','GID':'1j'},
            {'author':'xiaoju', 'time':'2018-06-11 08:32:12', 'comment':'cer2we','GID':'5k'},
            {'author':'zhiyi', 'time':'2018-06-15 08:32:12', 'comment':'gdfg6e','GID':'8l'},
        ],
        '14': [
            {'author':'yumeng', 'time':'2018-06-10 12:32:32', 'comment':'rsddtgse','GID':'8c'}
        ],
        '15': [
            {'author':'yumeng', 'time':'2018-06-08 12:32:32', 'comment':'treye','GID':'7d'},
            {'author':'yumeng', 'time':'2018-06-10 12:32:32', 'comment':'ghffghe','GID':'3e'},
            {'author':'zhiyi', 'time':'2018-06-15 12:32:32', 'comment':'wrfefe','GID':'5f'}
        ],
        '16' :[
            {'author':'ruolan', 'time':'2018-06-11 12:32:32', 'comment':'8i87oe','GID':'9g'}
        ],
        '17' :[
            {'author':'zhiyi', 'time':'2018-06-11 08:32:12', 'comment':'dsfgge','GID':'4h'}
        ],
        '18' :[
            {'author':'xiaoju', 'time':'2018-06-11 03:42:31', 'comment':'asfdsge','GID':'9i'}
        ],
        '19' :[
            {'author':'ruolan', 'time':'2018-06-08 03:42:31', 'comment':'xe','GID':'1j'},
            {'author':'xiaoju', 'time':'2018-06-11 08:32:12', 'comment':'cer2we','GID':'5k'},
            {'author':'zhiyi', 'time':'2018-06-15 08:32:12', 'comment':'gdfg6e','GID':'8l'},
        ],
        '20' :[
            {'author':'ruolan', 'time':'2018-06-08 03:42:31', 'comment':'xe','GID':'1j'},
            {'author':'xiaoju', 'time':'2018-06-11 08:32:12', 'comment':'cer2we','GID':'5k'},
            {'author':'zhiyi', 'time':'2018-06-15 08:32:12', 'comment':'gdfg6e','GID':'8l'},
        ],
        '21': [
            {'author':'yumeng', 'time':'2018-06-10 12:32:32', 'comment':'rsddtgse','GID':'8c'}
        ],
        '22': [
            {'author':'yumeng', 'time':'2018-06-08 12:32:32', 'comment':'treye','GID':'7d'},
            {'author':'yumeng', 'time':'2018-06-10 12:32:32', 'comment':'ghffghe','GID':'3e'},
            {'author':'zhiyi', 'time':'2018-06-15 12:32:32', 'comment':'wrfefe','GID':'5f'}
        ],
        '23' :[
            {'author':'ruolan', 'time':'2018-06-11 12:32:32', 'comment':'8i87oe','GID':'9g'}
        ],
        '24' :[
            {'author':'zhiyi', 'time':'2018-06-11 08:32:12', 'comment':'dsfgge','GID':'4h'}
        ],
        '25' :[
            {'author':'xiaoju', 'time':'2018-06-11 03:42:31', 'comment':'asfdsge','GID':'9i'}
        ],
        '26' :[
            {'author':'ruolan', 'time':'2018-06-08 03:42:31', 'comment':'xe','GID':'1j'},
            {'author':'xiaoju', 'time':'2018-06-11 08:32:12', 'comment':'cer2we','GID':'5k'},
            {'author':'zhiyi', 'time':'2018-06-15 08:32:12', 'comment':'gdfg6e','GID':'8l'},
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







    
