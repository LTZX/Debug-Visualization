import json

gitt = { '0': [
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

def sp(string):
    tmp = string.split('/')
    l = len(tmp)
    return tmp[l-1]

methodtofile = {}
with open('method.json') as f1:
    method = json.load(f1)

with open('gitdata.json') as f2:
    git = json.load(f2)

gitmap = {}
for each in method:
    methodtofile[method[each]['name']] = method[each]['file']
    gitmap[method[each]['file']] = []
#print methodtofile
for commit in git:
    cdata = {'author': commit['committer'], 'time':commit['date'][:19], 'comment':commit['comment'],'GID':commit['GID']}
    #print cdata
    for fl in commit['files']:
        fl = sp(fl)
        if fl not in gitmap:
            continue
        gitmap[fl].append(cdata)
results = {}
for each in method:
    m = method[each]
    results[each] = gitmap[m['file']]
with open('git.json', 'w') as outfile:
    json.dump(results, outfile)
    

