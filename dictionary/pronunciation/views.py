from django.shortcuts import render
import json
import requests
from playsound import playsound

def pnun(request):
    if (request.method=='POST'):
        myfile=open("g:\\djEnv\\dictionary\\word.txt","r")
        a=myfile.read()    
        app_id  = "7470dbc4"
        app_key  = "4dcc5a62c709873e5dce513cc82bceb4"
        endpoint = "entries"
        language_code = "en-us"
        word_id = a
        url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
        r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
        ansh=r.json()
        p=ansh['results'][0]['lexicalEntries'][0]['pronunciations'][1]['audioFile']
        playsound(p)

    return render(request,'pronun.html')
