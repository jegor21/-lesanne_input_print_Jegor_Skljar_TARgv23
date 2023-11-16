from math import *
# 1.ülesanne
print("1.harjutus")
print("Tere, maailm!") 
nimi=input("Mis on sinu nimi?: ") #kirjutame enda nimi
print("Tere, maailm! Tervitan sind {0}".format(nimi)) #tervist
vanus=int(input("Kui vana sa oled?: ")) #vanus
print("Tere, maailm! Tervitan sind {0}! Sa oled {1} aastat vana.".format(nimi,vanus)) #täis tervist



# 2.ülesanne
vanus = 18 #int
eesnimi = "Jaak" #str
pikkus = 16.5 #float
kas_käib_koolis = True #bool




# 3.ülesanne
print("3.harjutus")
kommide_arv=int(input("Laual olevate kommide arv: "))
print("Laua peal on {0}".format(kommide_arv))
mitu=int(input("Mitu kommi sa soovid süüa: "))
kommide_arv-=mitu
print("Nüüd laua peal on {0}".format(kommide_arv))



# 4.ülesanne
print("4.harjutus")
print("Puu läbimõõdu arvutamine")
C=float(input("Ümbermõõt: ")) # C=2*pi*R=pi*d
d=round(C/pi,2)
print("Läbimõõt: ",d)




# 5.ülesanne
print("5.harjutus")
print("Leiame diagonaali")
a=float(input("Esimene kaatet "))
b=float(input("Teine kaatet "))
d=sqrt(a**2+b**2)

print("Teie vastus {0}".format(d))


# 6.ülesanne
print("6.harjutus")
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg #oli aeg / teepikkus

print("Sinu kiirus oli " + str(kiirus) + " km/h")




# 7.ülesanne
print("7.harjutus")
print("Arvutame aritmeetilise keskmise.")
print("Kirjutage 5 arvud")
arv71=int(input("1.Arv = "))
arv72=int(input("2.Arv = "))
arv73=int(input("3.Arv = "))
arv74=int(input("4.Arv = "))
arv75=int(input("5.Arv = "))

arvsumma7=arv71+arv72+arv73+arv74+arv75
arvkeskmine7=arvsumma7/5

print("Teie tulemus on "+str(arvkeskmine7))




# 8.ülesanne
print("8.harjutus")
print("  @..@") 
print(" (----)")
print("( \__/ )")
print("^^''''^^")




# 9.ülesanne
print("9.harjutus")
print("Arvutame kolmnurga ümbermõõdu.")
na=int(input("a = "))
nb=int(input("b = "))
nc=int(input("c = "))
P=na+nb+nc

print("P = "+str(P))


# 10.ülesanne
print("10.harjutus")
print("Võtsite P sõbraga suure pitsa hinnaga 12,90€")
print("Jätate teenindajale 10% jootraha")
pitsa=12.9
jootraha=0.1
rõõmus=round((pitsa*jootraha+pitsa)/2,2)
print("Igaüks maksab peaegu "+str(rõõmus))