from django.shortcuts import render
import csv
def words(request):
          return render(request,'page1.html')

def red(request):
     a=dict()
     print(request.method)
     if request.method=='POST':
          print(request.method,"2")
          dict1=request.POST
          print(dict1,type(dict1))
          dict1=dict(dict1.dict())
          a['name']=dict1['word']
          a=a['name']
          file=open('word.txt','w')
          file.write(a)
          file.close()
     return render(request,'page2.html')
