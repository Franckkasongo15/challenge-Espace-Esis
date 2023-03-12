import os
import time

def main():
    # Code à exécuter toutes les 10 minutes
    print("Le programme se lance toutes les 10 minutes :)! ")
    
    # Attendre 10 minutes avant de relancer le programme
    time.sleep(600)

if __name__ == '__main__':
    # Vérifier si le fichier de flag existe
    if os.path.isfile("flag.txt"):
        while True:
            main()
    else:
        # Créer le fichier de flag
        open("flag.txt", "w").close()
        main()
