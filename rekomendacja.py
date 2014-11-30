#  Wzorowane na przykÅ‚adzie Rona Zacharskiego
#

from math import sqrt # import funkcji sqrt z biblioteki math

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
# dla każdego użytkownika przypisany jest słownik zawierający znane zespoły oraz ich oceny (1-5)
# users - zmienna do której jest przypisany słownik (zawierająca słownik), klucz: użytkownik, wartość: słownik zespołów gdzie nazwa jest kluczem a wartością jego ocena




def manhattan(rating1, rating2): # całe to to definicja funkcji manhattan, rating1 i rating2 to jej aargumenty
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys() # do zmiennej klucze1 przypisuje się zbiór kluczy słownika rating1
    klucze2 = rating2.keys() # analogicznie
    odleglosc = 0 # przypisanie do zmiennej odleglosc wartosci 0
    udaloSiePorownac = False # przypisanie do zmiennej udaloSiePorownac wartość False

    for klucz in klucze1: # pętla, przejście po wszystkich kluczach z klucze1
        if klucz in rating2.keys(): # jeśli klucz na którym jesteśmy znajduje się w zbiorze klucze2 to:
            udaloSiePorownac = True # przypisanie do udaloSiePorownac wartosci True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz]) # obliczenie odleglosci i dodanie do zmiennnej odleglosc

    if (udaloSiePorownac==True): # jeśli porównano chociaż jeden zespół to zwraca odleglosc, w przeciwnym wypadku zwraca wartosc -1 (żeby pokazać, że coś poszło źle)
        return odleglosc
    else:
        return -1

def testManhattan(rating1, rating2, odleglosc): # definicja funkcji testManhattan, rating1, rating2, odleglosc - parametry, rating1/2 - slowniki zespolow, odleglosc
    if manhattan(rating1, rating2) == odleglosc: # jeżeli odleglosc policzona funkcja manhattan jest rowna odleglosci (parametrowi) to zwraca True, inaczej False
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

def obliczNajblizszegoSasiada(imie, uzytkownicy): # imie - imię uztkownika od którego ma być najbliższy, uzytkownicy - zbiór użytkowników 
    """dla danego uÅ¼ytkownika, zwróć listę innych użytkowników według bliskości preferencji"""
    odleglosci = [] # przypisanie do odleglosci pustej tablicy
    for imie2 in uzytkownicy: # przechodzimy po zbiorze/tablicy uzytkownicy i dla kazdego imienia:
        odleglosc = 0 
        if imie!=imie2: # jeśli imię imie (parametr funkcji) jest różne od tego na którym akurat jesteśmy to:
            odleglosc = manhattan(uzytkownicy[imie], uzytkownicy[imie2]) # odleglosc = manhattan ze słowników da użytkownika imie i użytkownika imie2
                                                                        #pobrane po imieniu z pierwszego "megasłownika")
            odleglosci.append((odleglosc, imie2)) # dodanie wartości odleglosc,imie do tablicy odleglosci
    return sorted(odleglosci)

##print(obliczNajblizszegoSasiada('Hela',users))

def recommend(username, users):  # definicja funkcji recommend, przyjmuje parametry: imię użytkownika - username, słownik użytkowników - users
    """Zwróć listę rekomendacji dla użytkownika"""
    # znajdź preferencje najbliższego sąsiada
    nearestName = obliczNajblizszegoSasiada(username, users)[0][1] # przypisuje do zmiennej nearestName imię najbliższego sąsiada
                                                                   # bierze listę/tablicę z funkcji obliczNajblizszegoSasiada, następnie bierze z niej pierwszy element
                                                                   # czyli parę (odległość, nazwa użytkownika) oraz z tej pary drugi element tj nazwę użytkownika
    print 'Najblizszy sasiad to: %s' % nearestName # wypisuje imię najbliższego sąsiada
    recommendations = [] # inicjalizowanie pustej tablicy
    ratingOfNearest = users[nearestName] # przypisanie do ratingOfNearest słownika zespołów dla tego najbliższego sąsiada
    print 'Jego rekomendacje to:'
    print ratingOfNearest
    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobi‚ to jego najbliższy sąsiad
    userRating = users[username] # przypisanie do userRating słownika zespołów użytkownika username (przekazanego jako parametr)
   
    for artist in ratingOfNearest: # dla każego zespołu ze słownika ratingOfNearest:
        if not artist in userRating: # jeśli ten zespół nie znajduje się w liście userRating (czyli lista zespołów użytkownika przekazanego jako parametr)
            recommendations.append((artist, ratingOfNearest[artist])) # dodaje do listy recommendations tego artystę
    # zwróć posortowane rekomendacje
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True) # zwraca posortowaną wg. nazwy listę rekomendacji
 
print recommend('Hela', users)
