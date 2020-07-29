list1=[(1,2,3),[1,2],['a', 'hit', 'less']]
res=[ ]
for each in list1:
    if type(each)==type(list1):
          res=res+each
    elif type(each)==tuple:
          res.extend(each)
    else:
         res.append(each)
    print(res)
