from Berles import Berles
from Szemelyautok import Szemelyautok, sz_auto1, sz_auto2, sz_auto3
from Teherauto import Teherauto, t_auto1,t_auto2,t_auto3
from Autokolcsonzo import Autokolcsonzo
from datetime import datetime

autok =[sz_auto1,sz_auto2,sz_auto3]
teherautok = [t_auto1,t_auto2,t_auto3]
kolcsonzo = Autokolcsonzo("Roli Autókölcsönző")
kolcsonzo.auto_hozzaadasa(sz_auto1)
kolcsonzo.auto_hozzaadasa(sz_auto2)
kolcsonzo.auto_hozzaadasa(sz_auto3)

kolcsonzo.auto_hozzaadasa(t_auto1)
kolcsonzo.auto_hozzaadasa(t_auto2)
kolcsonzo.auto_hozzaadasa(t_auto3)

kolcsonzo.auto_berlese("AA-BB-12","2024-11-21")
kolcsonzo.auto_berlese("FF-CC-10","2025-03-16")
kolcsonzo.auto_berlese("XX-XX-88","2025-01-28")
kolcsonzo.auto_berlese("XX-XX-77","2024-12-06")





while True:
        print("------Üdvözöllek az Autókölcsönzőben!------")
        print("Válassz az alábbi lehetőségek közül.")
        print("1. Autó bérlése.")
        print("2. Bérlés lemondása.")
        print("3. Bérlések listázása.")
        print("4. Kilépés")
        valasz = input("Válassz egy opciót: ")
        print("--------------------------------------------")

        if valasz=="1":
            print("1. Bérelhető Személyautók")
            print("2. Bérelhető Teherautók")

            valasz=input("Válassz egy opciót:")
            if valasz=="1":
                for auto in autok:
                    print(auto.info())

                rendszam = input("Add meg az autó rendszámát: ")
                datum = input("Add meg a bérlés dátumát (ÉÉÉÉ-HH-NN formátumban): ")
                print(kolcsonzo.auto_berlese(rendszam, datum))

            elif valasz == "2":
                for auto in teherautok:
                    print(auto.info())
                rendszam = input("Add meg az autó rendszámát: ")
                datum = input("Add meg a bérlés dátumát (ÉÉÉÉ-HH-NN formátumban): ")
                print(kolcsonzo.auto_berlese(rendszam, datum))

        elif valasz == "2":
            print("-------Bérlés lemondása.-------")
            rendszam = input("Add meg a lemondandó bérlés rendszámát: ")
            datum = input("Add meg a lemondandó bérlés dátumát: ")
            print(kolcsonzo.berles_lemondasa(rendszam,datum))
            print("-------------------------------")
        elif valasz == "3":
            print("-------Bérelt járművek listázása.-------")
            kolcsonzo.berlesek_listazasa()
            print("-------------------------------------")
        elif valasz == "4":
            print("Kilépés...")
            break
        else:
            print("Nincs ilyen lehetőség.")







