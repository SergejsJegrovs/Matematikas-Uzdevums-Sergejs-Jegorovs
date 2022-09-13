#Lai mainit pirmo teoriju, mainiet so tekstu
Teorija1 = """
Vienādojumus, kuriem ir vienas un tās pašas saknes, sauc par ekvivalentiem vienādojumiem.
Par ekvivalentiem pārveidojumiem sauc pārveidojumus, kuru rezultātā no dotā vienādojuma iegūst tam ekvivalentu vienādojumu.
1. Vienādojuma abām pusēm pieskaitot vienu un to pašu skaitli vai izteiksmi, iegūst tam ekvivalentu vienādojumu.
Piemērs:
3x−2=7      |+2
3x−2+2=7+2
3x=9 
2. Vienādojuma abas puses reizinot vai dalot ar vienu un to pašu skaitli, kurš nav nulle, iegūst tam ekvivalentu vienādojumu.
Piemērs:
12x=24      |:12
12x:12=24:12
x=2
"""

#Lai mainit otro teoriju, mainiet so tekstu
Teorija2 = """
Vienādojums ir vienādība, kurā nezināmais skaitlis apzīmēts ar burtu.
Par vienādojuma sakni sauc skaitli, kuru ievietojot vienādojumā mainīgā vietā iegūst patiesu skaitlisku vienādību.
Piemērs:
5x−8=7
5x=7+8
x=15:5
x=3
 
3 ir vienādojuma sakne, jo 5⋅3−8=7.
Atrisināt vienādojumu nozīmē atrast visas tā saknes vai pamatot, ka vienādojumam sakņu nav.
Lineāram vienādojumam var būt viena sakne, bezgalīgi daudz saknes vai arī neviena sakne.
Ja vienādojuma labajā un kreisajā pusē uzrakstītās izteiksmes ir identiski vienādas, tad vienādojumam ir bezgalīgi daudz atrisinājumu.
Piemērs:
3x−9=3x−9
3x−3x=9−9
0=0

x var būt jebkurš skaitlis.
Ja vienādojuma labajā un kreisajā pusē uzrakstītās izteiksmes ne ar kādām x vērtībām nevar būt vienādas, tad vienādojumam nav atrisinājuma.
Piemērs:
2x+4=2x−6
2x−2x=−6−4
0=−10
0≠−10x∈∅
(atrisinājuma nav)
Visos pārējos gadījumos lineāram vienādojumam ir tieši viena sakne.
"""

#Lai mainit treso teoriju, mainiet so tekstu
Teorija3 = """
Ja vienādība satur vienu mainīgo un jāatrod mainīgā visas tās vērtības, ar kurām vienādība ir patiesa, tad saka, ka dotā vienādība ir vienādojums ar vienu mainīgo.
Piemēram, vienādība 2+(3−1)=4 nav vienādojums, bet 2+(x−1)=4 ir vienādojums, kura sakne ir 3.
Tās mainīgā vērtības, ar kurām vienādība ir patiesa, sauc par vienādojuma atrisinājumiem jeb saknēm.
 
Vienādojuma sakne var būt tikai skaitlis, kas pieder pie vienādojuma definīcijas apgabala.   
Piemērs:
Atrisini vienādojumu
x2−4x+2=0{x2−4=0x+2≠01)x2=4x=±22)x+2≠0x≠−2
 
Tātad šim vienādojumam ir tikai viena sakne x=2, jo x=−2 nepieder definīcijas apgabalam.
Viens no vienādojumu veidiem ir lineārs vienādojums.  
Par lineāru vienādojumu sauc vienādojumu ax+b=0, kur a un b ir reāli skaitļi.
 
Risinājuma soļi
Piemērs
1) ax+b=0ax=−b	
6x−24=06x=24
2) x=−ba	
x=246x=4
  
 
Lineāra vienādojuma atrisinājuma atkarība no parametra:
  
Ja a nav 0, tad vienādojumam ir viena sakne.
Piemēram, ja 2x−4=0, tad x=2.
 
Ja a=0, bet b≠0, tad vienādojumam nav sakņu.
Piemēram, 0x=3. Nav tādas x vērtības, kuru sareizinot ar 0 varētu iegūt 3.
 
Ja a=0 un b=0, tad vienādojuma atrisinājums ir jebkurš skaitlis.
Piemēram, 0x=0. Nulli sareizinot ar jebkuru skaitli iegūst 0.
"""

Uzdevums1 = ["Kurš no skaitļiem ir vienādojuma 2−6y=−22 sakne?","4",1]
Uzdevums2 = ["Atrisini lineāru vienādojum! −9+4f=4","3,25",1]
Uzdevums3 = ["Atrisini lineāru vienādojum! −5b+2=−18","4",1]
Uzdevums4 = ["Atrisini lineāru vienādojum! 0,5f+13=−3","32",1]
Uzdevums5 = ["Nosaki vienādojuma 3(2x−8)−19=5(x+2) sakni!","53",4]

punkti = 0
x = ""

while x != "0":
    print("Lai pabeigt darbu ievadiet 0")
    print("Lai sakt lasit teoriju ievadiet 1")
    print("Lai sakt risinat uzdevumus ievadiet 2")
    x = input()
    if x == "1":
        print(Teorija1)
        print("Nakama teorija - ievadiet 1")
        print("Atpakal - ievadiet 2")
        x = input()
        if x == "1":
            print(Teorija2)
            print("Nakama teorija - ievadiet 1")
            print("Atpakal - ievadiet 2")
            x = input()
            if x == "1":
                print(Teorija3)
    elif x == "2":
        print(Uzdevums1[0])
        print("Par so uzdevumu tu sanemsi",Uzdevums1[2],"punktu")
        atbilde = input()
        if atbilde == Uzdevums1[1]:
            punkti += Uzdevums1[2]
            print("Pareizi.")
        else:
            print("Nepareizi. Pareiza atbilde ir",Uzdevums1[1])
        print(Uzdevums2[0])
        print("Par so uzdevumu tu sanemsi",Uzdevums2[2],"punktu")
        atbilde = input()
        if atbilde == Uzdevums2[1]:
            punkti += Uzdevums2[2]
            print("Pareizi.")
        else:
            print("Nepareizi. Pareiza atbilde ir",Uzdevums2[1])
        print(Uzdevums3[0])
        print("Par so uzdevumu tu sanemsi",Uzdevums3[2],"punktu")
        atbilde = input()
        if atbilde == Uzdevums3[1]:
            punkti += Uzdevums3[2]
            print("Pareizi.")
        else:
            print("Nepareizi. Pareiza atbilde ir",Uzdevums3[1])
        print(Uzdevums4[0])
        print("Par so uzdevumu tu sanemsi",Uzdevums4[2],"punktu")
        atbilde = input()
        if atbilde == Uzdevums4[1]:
            punkti += Uzdevums4[2]
            print("Pareizi.")
        else:
            print("Nepareizi. Pareiza atbilde ir",Uzdevums4[1])
        print(Uzdevums5[0])
        print("Par so uzdevumu tu sanemsi",Uzdevums5[2],"punktu")
        atbilde = input()
        if atbilde == Uzdevums5[1]:
            punkti += Uzdevums5[2]
            print("Pareizi.")
        else:
            print("Nepareizi. Pareiza atbilde ir",Uzdevums5[1])
        print("Tu sanem",punkti,"punktiem no 8")
        print("Tava atzime ir",int(punkti/0.8))