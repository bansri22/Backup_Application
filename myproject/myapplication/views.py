import requests
from django.db.models import Q
from django.shortcuts import render

from .models import *

# This method return main page.
def show(request):
    return render(request, 'home.html')

# This function works when create backup invoked which helps to get data from API and store it to database.
def index(request):
    response = requests.get("https://api.pokemontcg.io/v1/cards?setCode=base4")

    data2 = response.json()

    for c in data2['cards']:
        m = project()
        m.idd = c['id']
        m.name = c['name']
        m.imageUrl = c['imageUrl']
        m.imageUrlHiRes = c['imageUrlHiRes']
        m.supertype = c['supertype']
        m.subtype = c['subtype']
        m.number = c['number']
        m.artist = c['artist']
        m.rarity = c['rarity']
        m.series = c['series']
        m.set = c['set']
        m.setCode = c['setCode']
        m.text = c.get('text')
        m.nationalPokedexNumber = c.get('types')
        m.types = c.get('types')
        m.hp = c.get('hp')
        m.retreatCost = c.get('retreatCost')
        m.convertedRetreatCost = c.get(' convertedRetreatCost')
        m.attackDamage = c.get('attackDamage')
        m.attackCost = c.get('attackCost')
        m.attackName = c.get('attackName')
        m.attackText = c.get('attackText')
        m.weaknesses = c.get('weaknesses')
        m.resistances = c.get('resistances')
        m.abilityName = c.get('abilityName')
        m.abilityText = c.get('abilityText')
        m.abilityType = c.get('abilityType')
        m.evolvesFrom = c.get('evolvesFrom')
        m.save(c)
    data1 = project.objects.all()
    return render(request, 'show.html', {'data': data1})

#this method useful for filtering data based on name,hit point and rarity
def search(request):
    if request.method != 'POST':

        return render(request, 'search.html')

    else:
        name = request.POST['name']
        hp = request.POST['hp']
        r = request.POST['r']

        if ((name and r != 'NONE') and (r and name != 'NONE')):
            data1 = project.objects.filter(Q(rarity=r) & Q(name=name))
        elif ((hp and r != 'NONE') and (r and hp != 'NONE')):
            data1 = project.objects.filter(Q(rarity=r) & Q(hp=hp))
        elif ((hp and name != 'NONE') and (name and hp != 'NONE')):
            data1 = project.objects.filter(Q(name=name) & Q(hp=hp))
        elif (hp == ''):
            data1 = project.objects.filter(Q(rarity=r) | Q(hp=hp) | Q(name=name))
        elif (name == ''):
            data1 = project.objects.filter(Q(rarity=r) | Q(hp=hp) | Q(name=name))
        elif (r == ''):
            data1 = project.objects.filter(Q(rarity=r) | Q(hp=hp) | Q(name=name))
        else:
            data1 = project.objects.filter(Q(rarity=r) & Q(hp=hp) & Q(name=name))
        data = data1
        return render(request, 'search.html', {'data': data})

#this function delete all the record from database.
def delete(request):
    data = project.objects.all().delete()
    return render(request, 'delete.html', {'data': data})
