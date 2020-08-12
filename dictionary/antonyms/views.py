from django.shortcuts import render
import requests
import nltk
from nltk.corpus import wordnet
from home import views as v1


def ant(request):
    myfile=open("g:\\djEnv\\dictionary\\word.txt","r")
    a=myfile.read()    
    synonyms = [] 
    antonyms = [] 
    for syn in wordnet.synsets(a):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    antonyms=set(antonyms)
    print(antonyms)
    data=antonyms
    return render(request,'antonym.html',{'data':data})

