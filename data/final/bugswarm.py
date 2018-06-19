import json
filedata = {'lines-of-code':37, 'lines':50, 'method':7,
            'class':3, 'file':3, 'directory':2, 'comment-lines': 13,
            'comments': '26%', 'time-range': ['2018-05-08', '2018-05-15'],
            'author': 52, 'bug':14}

with open('method.json') as f1:
    methods = json.load(f1)

with open('git.json') as f2:
    git = json.load(f2)

with open('relation.json') as f3:
    relations = json.load(f3)

with open('filedata.json') as f4:
    fdata = json.load(f4)
filedata['lines-of-code'] = fdata['lines']
filedata['time-range'] = fdata['timeRange']
filedata['class'] = 0
filedata['comments'] = '0%'

#==================================
import datetime
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
                
#codes = {}
#for each in methods:
#    with open('code_large/'+ each +'.txt', 'r') as myfile:
#      codes[each] = myfile.read()
#namelist = {}
#for each in methods:
#    each = methods[each]
#    if each['name'] not in namelist:
#        namelist[each['name']] = each['MID']

out_put={}
out_put_total={}
begin_date = datetime.datetime.strptime('2014-08-09', "%Y-%m-%d")
end_date = datetime.datetime.strptime('2018-06-08', "%Y-%m-%d")
while begin_date <= end_date:
    date_str = begin_date.strftime("%d-%b-%Y")
    out_put_total[date_str]=0
    begin_date += datetime.timedelta(days=1)

for i in range(168):
    out_put[str(i)]={}
    begin_date = datetime.datetime.strptime('2014-08-09', "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%d-%b-%Y")
        out_put[str(i)][date_str]=0
        begin_date += datetime.timedelta(days=1)

for method in git:
    for data in git[method]:
        tmp=datetime.datetime.strptime(data['time'].split()[0], "%Y-%m-%d")
        time=tmp.strftime("%d-%b-%Y")
        out_put[method][time]+=1
        out_put_total[time]+=1

out_put['total'] = out_put_total

time = {}
for each in out_put:
    time[each] = []
    for ele in out_put[each]:
        time[each].append({'date': ele, 'close': out_put[each][ele]})
gittmp=[]
for each in git:
    each = git[each]
    for ele in each:
        gittmp.append(ele)
git['total'] = gittmp

bardict = {}
bardict['total']={}
for each in git:
    bardict[each] = {}
    for ele in git[each]:
        if ele['author'] not in bardict[each]:
            bardict[each][ele['author']] = 0
        if ele['author'] not in bardict['total']:
            bardict['total'][ele['author']] = 0
        bardict[each][ele['author']] += 1
        bardict['total'][ele['author']] += 1
bar = {}
for each in bardict:
    bar[each] = []
    for ele in bardict[each]:
        bar[each].append({'label': ele, 'value': bardict[each][ele]})
        
codes = {}
for each in methods:
    with open('htmls/'+ each +'.html', 'r') as myfile:
      codes[each] = myfile.read()
      
data = {'filedata': filedata, 'force': force, 'groupby': groupby,
         'time': time, 'table': git, 'bar': bar, 'code':codes}
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
    

