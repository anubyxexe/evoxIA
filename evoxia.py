#setting
version = 0.1

#les import
import os
import datetime

#les def:
#clear
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#mise en place de l'interface
def logo():
    os.system('cls' if os.name=='nt' else 'clear')
    print("                        .__        ")
    print("  _______  _________  __|__|____   ")
    print("_/ __ \  \/ /  _ \  \/  /  \__  \  ")
    print("\  ___/\   (  <_> >    <|  |/ __ \_")
    print(" \___  >\_/ \____/__/\_ \__(____  /")
    print(f"     \/                \/       \/ V{version}") #la ou sera afficher a version
    #calcul entre sa date de creation et aujourd'hui
    today = datetime.datetime.now()
    firtcode = datetime.datetime(2023,2,21)
    time_diff = today - firtcode
    firtcodedays = time_diff.days
    print(f"  Evox-ia existe depuis {firtcodedays} jours")

#afficher le logo
logo()
