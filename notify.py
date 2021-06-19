import requests

def notify(msg):
    url = ('https://maker.ifttt.com/trigger/Warning/with/'+'key/cEQpmS1N785KvCnzcnxwNQ' 
    +'?value1='+str(msg)+'&value3=https://sites.google.com/site/beijixiongvincent0925/_/rsrc/1362484296848/home/65413131324.jpg?height=315&width=400')
    r = requests.get(url)      
    if r.text[:5] == 'Congr':  
        print('成功推送 (' +str(msg)+') 至 Line')
    return r.text

notify("測試")
    