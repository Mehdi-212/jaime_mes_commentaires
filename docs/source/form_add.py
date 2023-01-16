# On importe les modules nécessaires
from tkinter import*
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import csv


def envoyer():
    """
    Fonctions permettant d'envoyer la liste des employées
    """
    with open('liste_employes.csv', 'a', newline='') as fichiercsv:
        writer = csv.writer(fichiercsv)
        writer.writerow([str(entry_03.get()),  str(entry_02.get()),
                        str(entry_04.get()),  str(entry_05.get())])
    base.destroy()


if __name__ == "__main__":

    # On crée la fenêtre principale
    base = Tk()

    # On définit la taille de la fenêtre et son titre
    base.geometry('500x500')
    base.title("Ajout d'employé")

    # On crée un label pour le titre de la fenêtre
    labl_0 = Label(base, text="Ajout d'un employé",
                   width=20, font=("bold", 20))
    labl_0.place(x=90, y=53)

    # On crée un label et un champ d'entrée pour le nom
    labl_1 = Label(base, text="Nom", width=20, font=("bold", 10))
    labl_1.place(x=80, y=130)

    entry_02 = Entry(base)
    entry_02.place(x=240, y=130)

    # On crée un label et un champ d'entrée pour le prénom
    labl_2 = Label(base, text="Prénom", width=20, font=("bold", 10))
    labl_2.place(x=80, y=160)

    entry_03 = Entry(base)
    entry_03.place(x=240, y=160)

    # On crée un label et un champ d'entrée pour la date
    labl_3 = Label(base, text="Date", width=20, font=("bold", 10))
    labl_3.place(x=80, y=190)

    # On crée un widget de sélection de date
    entry_04 = DateEntry(base, bg="darkblue", fg="white", year=2022)
    # On place le widget dans la fenêtre
    entry_04.grid()
    entry_04.place(x=240, y=190)

    # On crée un label et un champ de sélection pour la profession
    labl_4 = Label(base, text="Profession", width=20, font=("bold", 10))
    labl_4.place(x=80, y=220)

    # On lit le contenu du fichier 'postes.txt' et on crée une liste avec les différentes professions
    listeProfession = open("postes.txt", "r").read()
    listeProfession = listeProfession.split()
    # On crée un widget de sélection avec la liste des professions
    entry_05 = ttk.Combobox(base, values=listeProfession)
    # On sélectionne la première profession par défaut
    entry_05.current(0)
    # On place le widget dans la fenêtre
    entry_05.pack()
    entry_05.place(x=240, y=220)

    # On définit une fonction pour envoyer les données saisies

    # bouton envoyer
    Envoyer = Button(base, text="ENVOYER", command=envoyer,
                     pady=2).place(x=240, y=280)

    base.mainloop()

    print("Enregistrement bien effectué.")
