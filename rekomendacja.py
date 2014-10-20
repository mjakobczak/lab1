#  Wzorowane na przykÅ‚adzie Rona Zacharskiego
#

from math import sqrt

users = {
        "Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

def testManhattan(rating1, rating2, odleglosc):
    if manhattan(rating1, rating2) == odleglosc:
        return True
    else:
        return False

##print (testManhattan({'łzy': 5, 'TL':3},
##                    {'łzy':10},
##                    5)
##       )
##
##print (testManhattan({'łzy': 5, 'TL':3},
##                    {'BS':10},
##                    -1)
##       )
    
    
##odlegloscOdAniDoHeli = manhattan(users["Ania"], users["Hela"])
##print ("od Ani do Heli jest ", odlegloscOdAniDoHeli)

# print( recommend('Hela', users))
# print( recommend('Celina', users))

def obliczNajblizszegoSasiada(imie, uzytkownicy):
    """dla danego uÅ¼ytkownika, zwróć listę innych użytkowników według bliskości preferencji"""
    odleglosci = []
    for imie2 in uzytkownicy:
        odleglosc = 0
        if imie!=imie2:
            odleglosc = manhattan(uzytkownicy[imie], uzytkownicy[imie2])
            odleglosci.append((odleglosc, imie2))
    return sorted(odleglosci)

##print(obliczNajblizszegoSasiada('Hela',users))

def recommend(username, users):
    """Zwróć listę rekomendacji dla użytkownika"""
    # znajdź preferencje najbliższego sąsiada
    nearestName = obliczNajblizszegoSasiada(username, users)[0][1]
    print 'Najblizszy sasiad to: %s' % nearestName
    recommendations = []
    ratingOfNearest = users[nearestName]
    print 'Jego rekomendacje to:'
    print ratingOfNearest 
    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobi‚ to jego najbliższy sąsiad
    userRating = users[username]
    
    for artist in ratingOfNearest:
        if not artist in userRating:
            recommendations.append((artist, ratingOfNearest[artist]))
    # zwróć posortowane rekomendacje
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

print recommend('Hela', users)
