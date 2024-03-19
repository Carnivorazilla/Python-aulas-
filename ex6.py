def hipotenusa(catO,catA):
    return (catO**2 + catA**2)**0,5

def seno (catO, catA):
    h = hipotenusa(catO,catA)
    return catO/h

def cosseno (catO, catA):
    h = hipotenusa(catO,catA)
    return catA/h

def tangente (catO,catA):
    return catA/catO

