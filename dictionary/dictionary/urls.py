from django.contrib import admin
from django.urls import path
from home import views as v1
from meaning import views as v2
from antonyms import views as v3
from synonyms import views as v4
from pronunciation import views as v5
from example_sentences import views as v6


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.words),
    path('a',v1.red),
    path('m',v2.mean),
    path('an',v3.ant,name='script'),
    path('s',v4.syn,name='script'),
    path('pn',v5.pnun,name='script'),
    path('e',v6.esen),
]
