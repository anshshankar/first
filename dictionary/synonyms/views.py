from django.shortcuts import render
import requests
import nltk
from nltk.corpus import wordnet 
def syn(request):
    myfile=open("g:\\djEnv\\dictionary\\word.txt","r")
    a=myfile.read()    
    synonyms = [] 
    for syn in wordnet.synsets(a):
        for l in syn.lemmas():
            synonyms.append(l.name())
    synonyms=set(synonyms) 
    print(synonyms)
    data=synonyms
    return render(request,'synonym.html',{'data':data})


