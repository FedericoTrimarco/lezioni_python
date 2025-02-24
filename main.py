from datetime import date
#per inizilizzare un progetto lanciare il comando -> python -m venv nomeProgetto

# lezione 1 - log di python
# print("ciao")

##########################################################################################
# lezione 2 - variabili + mesaggio in input
""" messaggio = input("inserisci qualcosa: ")
print(messaggio) """

##########################################################################################
#lezione 3 - variabili
""" print("\nLEZIONE 3")
x = 5
y = 10

a, b, c = 2, 4, 6
l = m = n = 246
e, i, o = [4, 8, 16]

print("\nPRIMO TEST VAR")
print(a)
print(b)
print(c)

print("\nSECONDO TEST VAR")
print(l)
print(m)
print(n)

print("\nTERZO TEST VAR")
print(e)
print(i)
print(o) """

##########################################################################################
#lezione 4: tip di variabili

# str: new_var_type = "ciao"
# int: new_var_type = 5
# float: new_var_type = 5.5
# bool: new_var_type = True

# list: new_var_type = ["ROMA", "MILANO", "NAPOLI"]
# tuple: new_var_type = ("roma", "milano", "napoli")
# range: new_var_type = range(6)
# dict: new_var_type = {"nome": "luca", "eta": 27}
# set: new_var_type = {"roma", "milano", "napoli"}

""" new_var_type = "ciao"

print("\nLEZIONE 4")

print(type(new_var_type)) """

##########################################################################################
#lezione 5: casting
#conversione di variabili

""" print("\nLEZIONE 5")

a = float(5)
b = float("5.6")
c = a + b
print(c)

d = "ciao sono "
e = str(5)
f = d + e
g = int("234234234")
print(f)
print(g) """

##########################################################################################
#lezione 6: stringe

# 1 andare a capo
# 2 stringhe trattate come array
# 3 lunghezza di una stringa
# 4 ottenere l'ultima lettera/elemento di una stringa
# 5 ciclare una stringa
# 6 prendere parte di una stringa
# 7 modifiche una stringa -> upper(), lower(), strip(), replace()
# 8 concatenare stringhe e numeri

""" a = "ciao forza napoli fratm"

b = 'lello'
x = "ciao sono Federico"

# 1
print("\n1° parte ")
print(a)
print(b)

# 2
print("\n2° parte ")
print(a[0])

# 3
print("\n3° parte ")
print(len(b))

# 4
print("\n4° parte ")
print(b[len(b)-1])

# 5
print("\n5° parte ")
for lettera in b:
    print(lettera)

# 6
print("\n6° parte ")
print(x[:3])
print(x[2:])
print(x[2:8])
print(x[-8:])

# 7
print("\n7° parte ")
print(x.upper())
print(x.lower())
print(x.replace("Federico", "Lello"))

y = "  froza napoli 1926      "
print(y.strip()) #il trim di JS

# 8
print("\n8° parte ")
z = "CONCATENAZIONE STRNGA-NUMERO CON IL NUM: {}, peso {}, altezza {}"
print(z.format(5, 67, 70))

z2 = "CONCATENAZIONE STRNGA-NUMERO CON IL NUM: {2}, peso {0}, altezza {1}"
print(z2.format(5, 67, 70))

z3 = "Sono nato nel mese del \"lupo\""
z4 = 'Sono alla ricerca dell\'amore'
print(z3)
print(z4) """

##########################################################################################
#lezione 7: booleani

#1
""" print("\n1° parte ")
print(bool(1))
print(bool(0))
x = 0
y = 2

#2
print("\n2° parte ")
if x == y:
    print(True)
elif y == 1:
    print(True)
else:
    print(False) """

##########################################################################################
#lezione 8: Operazioni aritmetiche

""" print("\n1° parte ")
x = 10
y = 3
z = 6
z += 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) #floor-division -> ci restituirà il risultato arrotondato per difetto
print(x % y)  #per prendere solo il resto con il quale si può pire se il risultato è pari o dispari
print(x ** y) #potenza (10 alla 5°)
print(z)

print("\n2° parte (minx, max, abs, pow)")

a = min(5, 10, 25) #restituisce il minimo
b = max(5, 10, 25) #restituisce il minimo
c = abs(-7) #valore assoluto
d = pow(5, 3) #potenza (5 alla terza)
print(a)
print(b)
print(c)
print(d) """

##########################################################################################
#lezione 9: Condizioni (if, elif, else)

#le condizioni AND, OR in python si scrivono and - or a differenza di js o java che si scrivono && - ||
#condizione not sarebbe la negazione (!)
""" x = 25
y = 20
z = 5

if not(25 != 25):
    print("NEGAZIONE")

if x == y or x > z:
    print(x+y)
elif y % 5 == 0 and y == 20:
    print("non vi è nessun resto")
else:
    print("fora napoli 1926")

print("\nOperatore ternario:\n")
print("è maggiore di 10") if z > 10 else print("non lo è") """

##########################################################################################
#lezione 10: Liste / Iterazioni-cicli
""" x = ["Milano", "Roma", "Napoli"]
y = 0

print("\n1° CICLO FOR:\n")
for citta in x:
    print(citta)
    if citta == "Napoli":
        print("A città cchiù bell ro munn\n")
    else: 
        print("città non bella come napoli\n")

print("\n2° CICLO FOR:\n")
for el in range(9):
    print(el)
else:
    print("ho inito il 2° ciclo for")

print("\nCICLO WHILE:\n")
while y < 6:
    y += 1
    print(y)
else:
    print("ciclo while finito") """

##########################################################################################
#lezione 11: collezioni di dati
# list, tuple, set, dictionary
# 1 lunghezza liste
# 2 inserire alla fine di una lista (append)
# 3 inserire in una lista (insert)
# 4 estendere una lista con un altra lista
# 5 rimuovere elementi -> remove(), pop(), del(), clear()
# 6 list comprension
# 7 ordinamento list -> sort
# 8 copiare una lista -> copy()
# 9 unire le liste

""" print("\n1° parte:\n")
a = ["milano", "roma", "napoli", "venezia"]
b = ["milano", 27, True]
c = list(("forza", "napoli", "1926"))

print(len(a))
print(len(b))
print(len(c))

print("\n2° parte:\n")
a.append("firenze")
print(a)

print("\n3° parte:\n")
a.insert(0, "bologna")
print(a)

print("\n4° parte:\n")
d = ["portici", "pomigliano"]
a.extend(d)
print(a)

print("\n5° parte:\n")
a.remove("milano")
a.pop() #rimuove l'ultimo elemento
print(a)

del a[0] #eliminare l'oggetto
print(a)

print(b)
b.clear() #per pulire la lista
print(b)

print("\n6° parte:")
#regole per la print("\n5° parte:\n"):
#  [espressione for item lista condizione (opzionale)]

#esempio senza condizione
print("\n6.1° parte:\n")
[print(citta) for citta in a]

#esempio con condizione
print("\n6.2° parte:\n")
[print(citta) for citta in a if citta != "napoli"]

#la list comprension può essere utilizzat per creare una nuova lista partendo da una lista
print("\n6.3° parte:\n")
a2 = [citta for citta in a if citta != "napoli"]
print(a2)

print("\n7° parte:\n")

lista_citta = ["milano", "roma", "napoli", "venezia"]
lista_citta.sort()
print(lista_citta)
#ordinamento inverso
lista_citta.sort(reverse=True)
print(lista_citta)

print("\n8° parte:\n")
print("\n8.1° parte:")
lista_citta_2 = ["milano", "roma", "napoli", "venezia"]
lista_citta_3 = lista_citta_2
#le liste diventano uguali ma la modifica di uno i ripercuote anche sull'altro
lista_citta_3[0] = "luche"
print(lista_citta_2)
print(lista_citta_3)

print("\n8.2° parte:")
lista_citta_4 = lista_citta_2.copy()
lista_citta_4[0] = "GIORGIONE"
print(lista_citta_2)
print(lista_citta_4)

print("\n8.3° parte:")
lista_citta_5 = list(lista_citta_2)
lista_citta_5[0] = "MICHELE"
print(lista_citta_2)
print(lista_citta_5)

print("\n9° parte:")
lista_citta_6 = ["roma", "milano"]
lista_citta_7 = ["napoli", "firenze"]

print("\n9.1° parte: prima concatenazione con il +")
lista_citta_8 = lista_citta_6 + lista_citta_7

print(lista_citta_6)
print(lista_citta_7)
print(lista_citta_8)

print("\n9.2° parte: seconda concatenazione con il metodo append e ciclo for")
[lista_citta_6.append(citta) for citta in lista_citta_7]
print(lista_citta_6)

print("\n9.3° parte: terza concatenazione co extends")
lista_citta_9 = ["roma", "milano"]
lista_citta_10 = ["napoli", "firenze"]

lista_citta_9.extend(lista_citta_10)
print(lista_citta_9) """

#lezione 12: tuple
# collezioni di dati ordinati, indicizzati, non modificabili e permettono duplicati
# se si prova a fare lista[0] = 'lello' il codice darà errore perchè gli elementi di una tupla non sono modificabili
# 1 condizione er vedere se è una tupla
# 2 construttore tuple + recupero elementi dalla lista
# 3 vedere se l'elemento è incluso nella lista (funzionanto anche per le list [])
# 4 assegnazione singole variabili
# 5 metodo count() e index()

""" print("\n1° parte:")
lista_tuple_1 = ("milano", "roma", "napoli")
lista_tuple_2 = ("milano", True, 45)
print(type(lista_tuple_2))
print(type(lista_tuple_2) is tuple)

print("\n2° parte:")

lista_tuple_3 = tuple(("milano", "roma", "napoli", "firenze"))

print(type(lista_tuple_3))
print(lista_tuple_3[0])
print(lista_tuple_3[-1])
print(lista_tuple_3[:2])
print(lista_tuple_3[2:])
print(lista_tuple_3[1:3])

print("\n3° parte:")
if "milano" in lista_tuple_3:
    print("ok")

print("\n4° parte:")
lista_tuple_4 = ("milano", "roma", "napoli", "firenze")
(c1, c2, c3, c4) = lista_tuple_4

print("\n4.1° parte:")
print(c1)
print(c2)
print(c3)
print(c4)

print("\n4.2° parte:")
(c5, c6, *c7) = lista_tuple_4
print(c5)
print(c6)
print(c7)

print("\n5° parte:")

print("\n5.1° parte:")
lista_tuple_5 = ("milano", "roma", "napoli", "firenze", "napoli", "napoli")
# stringa pythonic
print(f"il numero totale di elementi trovati con la stringa napoli è: {lista_tuple_5.count('napoli')}")

print("\n5.2° parte:")
lista_tuple_5 = ("milano", "roma", "napoli", "firenze")
print(f"il numero index di napoli è: {lista_tuple_5.index('napoli')}") """

#lezione 13: set
# Collezioni di dati non ordinate, non indicizzate, non modificabili e non permettono duplicati
# 1 creare un set (normale e/o mischiato) + construttore
# 2 vedere se un elemnto è presente nel set
# 3 siccome non è indicizzato non si può accedere ad un elemento con nome_lista[0] ma bisogna per forza ciclare il set
# 4 aggiungere elementi
# 5  unire un set con un altro (union) e quindi creare un nuovo set, aggiornare set (update)
# 6 rimuovere elementi
# 7 intersezioni (intersection_update, intersection, symmetric_difference_update, symmetric_difference)

""" lista_set_1 = {"milano", "roma", "napoli"}
lista_set_2 = {"napoli", 24, False}

print("\n1° parte:")
print("\n1.1° parte:")
print(type(lista_set_1))
print(len(lista_set_1))

print("\n1.2° parte: (CONSTRUTTORE)")
lista_set_3 = set({"milano", "roma", "napoli", "firenze"})


print("\n2° parte: ")
citta_da_verificare = "napoli"
is_in_set_3 = citta_da_verificare in lista_set_3
print(f"{citta_da_verificare} è presente nel set lista_set_3? {is_in_set_3}")

print("\n3° parte:")
print("\n3.1° parte:")
# print(lista_set_1[0]) #darà errore
print(lista_set_1) # gli elementi appariranno in un ordine casuale -> {"milano", "roma", "napoli"} - {'napoli', 'roma', 'milano'}

print("\n3.2° parte:")
#iterazione per prendere il singolo elemento (anche questi appariranno in ordine casuale)
for citta in lista_set_3:
    print(f"città -> {citta}")

print("\n4° parte:")
lista_set_4 = {"milano", "roma", "napoli"}
lista_set_4.add("venezia")
print(lista_set_4)

print("\n5° parte:")
print("\n5.1° parte:")
lista_set_5 = {"milano", "roma", "napoli"}
lista_set_6 = {"firenze", "brescia"}

lista_set_7 = lista_set_5.union(lista_set_6)

print(lista_set_5)
print(lista_set_6)
print(f"unione -> {lista_set_7}")

print("\n5.1° parte:")
lista_set_8 = {"milano", "roma", "napoli"}
lista_set_9 = {"firenze", "brescia"}
print(lista_set_8)
print(lista_set_9)

lista_set_8.update(lista_set_9)
print(f"update -> {lista_set_8}")

print("\n6° parte:")
lista_set_10 = {"milano", "roma", "napoli", "brescia", "udine"}

# lista_set_10.remove("firenze") # darà errore perchè non esiste l'elemento nel set
lista_set_10.remove("roma")
lista_set_10.discard("firenze") # la differenza con il remove è che se anche non esiste l'elemento nel set NON DARA' ERRORE
lista_set_10.pop()              # rimuove l'ultimo elemento
print(lista_set_10)

print("\n6.1° parte: pulire tutto il set")
lista_set_10.clear()              # rimuove tutto
print(lista_set_10)
print(lista_set_10)

print("\n6.2° parte: eliminare il set")
del lista_set_10 # elimina il set quindi il terminale darà errore poiche non esiste più quella variabile
# print(lista_set_10)

print("\n7° parte:")
lista_set_11 = {"milano", "roma", "napoli"}
lista_set_12 = {"firenze", "brescia", "napoli"}
lista_set_13 = lista_set_11.union(lista_set_12)

print(lista_set_13) # napoli non verrà duplicata poichè il set per natura non può avere elementi duplicati

print("\n7.1° parte: intersection_update (restituisce solo gli elementi in comune e aggiorna il set)")
lista_set_14 = {"milano", "roma", "napoli"}
lista_set_15 = {"firenze", "brescia", "napoli", "roma"}

lista_set_14.intersection_update(lista_set_15)
print(lista_set_14)

print("\n7.2° parte: intersection (restituisce solo gli elementi in comune e crea un nuovo set)")
lista_set_16 = {"milano", "roma", "napoli"}
lista_set_17 = {"firenze", "brescia", "napoli", "roma"}
lista_set_18 = lista_set_16.intersection(lista_set_17)
print(lista_set_18)

print("\n7.3° parte: symmetric_difference_update (restituisce solo gli elementi non in comune e aggiorna set)")
lista_set_19 = {"milano", "roma", "napoli"}
lista_set_20 = {"firenze", "brescia", "napoli", "roma"}
lista_set_19.symmetric_difference_update(lista_set_20)
print(lista_set_19)

print("\n7.3° parte: symmetric_difference (restituisce solo gli elementi non in comune e crea un nuovo set)")
lista_set_21 = {"milano", "roma", "napoli"}
lista_set_22 = {"firenze", "brescia", "napoli", "roma"}
lista_set_23 = lista_set_21.symmetric_difference(lista_set_22)
print(lista_set_23)
 """

#lezione 14: dictionary
# Collezioni di dati ordinate, modificabili ma non permettono duplicati
# Sono equivalenti agli oggeti in JS
# 1 creare un dictionary
# 2 tipo, lunghezza
# 3 accedere agli elementi
# 4 condizione per vedere se esiste una chiave nel nostro dictionary
# 5 modificare gli elementi
# 6 rimuovere gli elementi -> pop(key), popitem(), clear(), del per eliminare il dictionary
# 7 iterazione di una dictionary
# 8 copiare un dict -> copy(), dict()
# 9 dict annidati (oggetti in oggetti)

""" print("\n1° parte:")
persona = {
    "nome": "Luca",
    "cognome": "Alfredino",
    "anni": 27
}
print(persona)

print("\n2° parte:")
print(type(persona))
print(len(persona)) #restituirà il numero totale delle chiavi

print("\n3° parte:")
print("\n3.1° parte: persona['cognome']")
print(persona["cognome"])

print("\n3.2° parte: get")
print(persona.get("nome"))

print("\n3.3° parte: keys, -> restituisce solo le chiavi")
x = persona.keys()
print(x)

print("\n3.4° parte: values, -> restituisce solo i valori")
y = persona.values()
print(y)

print("\n3.5° parte: items, -> restituisce una list di tuple")
z = persona.items()
print(z)
print("\ncicliamo la nostra list di tuple")
for el in z:
    print(el)

print("\n4° parte:")
chiave_1 = "nome"
chiave_2 = "data_nascita"
exist_chiave_1 = chiave_1 in persona
exist_chiave_2 = chiave_2 in persona

print(f"La chiave {chiave_1} esiste in persona? {exist_chiave_1}")
print(f"La chiave {chiave_2} esiste in persona? {exist_chiave_2}")

print("\n5° parte:")
print("\n5.1° parte: persona['anni'], persona['nazione_preferita'] per creare una nuova chiave-valore")
persona["anni"] = 37
persona["nazione_preferita"] = "Giappone"
print(persona)

print("\n5.2° parte: update")
persona.update(
    {
        "nome": "Lellone",
        "cognome": "Napoletani"
    }
)
print(persona)

print("\n5.2° parte: update per aggiungere una nuova chiave-valore")
persona.update(
    {
        "colore_preferito": "viola"
    }
)
print(persona)

print("\n6° parte: pop(key)")
print("\n6.1° parte:")

persona.pop("nome")
print(persona)

print("\n6.2° parte: popitem() -> rimuove ultimo elemento")

persona.popitem()
print(persona)

print("\n6.3° parte: clear() -> per pulire il dict")

persona.clear()
print(persona)

print("\n6.4° parte: clear() -> per pulire il dict")

persona.clear()
print(persona)

print("\n7° parte:")
print(date.ctime)
data_attuale = date.today()
persona_2 = {
    "nome": "Federico",
    "cognome": "Trimarco",
    "anni": (int(data_attuale.year) - 1998)
}

print(persona_2)

print("\n7.1° parte:")
print("\nciclo per prendere solo le chiavi")
for el in persona_2: #restituirà solo le chiavi
    print(f"el -> {el}")

print("\nciclo per prendere solo i valori ( for el in persona_2 )")
for el in persona_2: #per prendere il valore
    print(f"persona_2[el] -> {persona_2[el]}")

print("\nciclo per prendere solo i valori ( for el in persona_2.values() )")
for el2 in persona_2.values(): #per prendere il valore
    print(f"el2 -> {el2}")

print("\nciclo per prendere solo chiave valore (tuple) ( for el2 in persona_2.items() )")
for x, y in persona_2.items(): #per prendere il valore
    print(x, y)

print("\n8° parte:")
print("\n8.1° parte: copy()")

persona_3 = persona_2.copy()
print(persona_3)

print("\n8.2° parte: construttore dict()")
persona_4 = dict(persona_2)
print(persona_4)

print("\n9° parte:")
persona_5 = {
    "nome": "Federico",
    "cognome": "Trimarco",
    "anni": (int(data_attuale.year) - 1998),
    "indirizzo": {
        "via": "via bromberi",
        "num_civico": 6,
        "cap": "80046"
    }
}

print(persona_5["indirizzo"])
print(persona_5["indirizzo"]["num_civico"]) #per prendere il valore di chiave dentro un dict che sta in un dict """

#FINE COLLEZIONE DI DATI
##########################################################################################

# lezione 15: funzioni
# 1- definizione di una funzione (def)

print("\nESEMPI:")
print("\n1° parte:")

#definizione
def fare_la_pasta():
    print("metti acqua")
    print("fai bollire")
    print("metti la pasta")

#chiamata alla funzione
fare_la_pasta()

print("\n2° parte: enumerate per utilizzare l'index")
#argomenti

def visualizza_ingredienti(lista_ingredienti):

    for index, ingr in enumerate(lista_ingredienti):
        print(f"{index} -> {ingr}")


visualizza_ingredienti(["milano", "roma", "napoli"])

print("\n3° parte: numero di argomenti indefinito")

def fai_la_cacio_e_pepe(*opzioni):
    print(opzioni[0])
    print(opzioni[1])
    print(opzioni[2])

fai_la_cacio_e_pepe("cacio e pepe", 10, True)

print("\n4° parte: argomenti con chiave valore \nAnche se gli argomenti non vengono passati nell\'ordine stabilito funzioneranno tramite la loro chiave")

def fare_pasta_al_sugo(tipo_pasta, sugo):
    print(tipo_pasta)
    if sugo:
        print("sugo SI")

fare_pasta_al_sugo(sugo = True, tipo_pasta = "Fusilli")

print("\n4° parte: argomenti con chiave valore \nAnche se gli argomenti non vengono passati nell\'ordine stabilito funzioneranno tramite la loro chiave")

def fare_pasta_al_pomodoro(tipo_pasta = "spaghetti"):
    print(tipo_pasta)

fare_pasta_al_pomodoro("fusilli")
fare_pasta_al_pomodoro()

print("\n5° parte: return valori")


def is_maggiore_di_20(valore):
    if valore > 20:
        print("VERO")
        return True
    else:
        print("FALSO")
        return False

valore_1 = is_maggiore_di_20(10)
valore_2 = is_maggiore_di_20(30)

if valore_1 :
    print("froza napoli 1")

if valore_2 :
    print("froza napoli 2")
