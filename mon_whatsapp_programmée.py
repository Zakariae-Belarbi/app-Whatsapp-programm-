import tkinter
import base64
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import PhotoImage
from datetime import datetime, timedelta
from tkinter import messagebox
import pywhatkit
import time
entry_telephone = None
entry_message=None
entry_heure = None
entry_minute = None
entry_repetitions = None

def envoyer_message(numero_telephone,message,heure_envoi,minute_envoie,repetitions,fenetre):
    try:
        for i in range(int(repetitions)):
            now = datetime.now()
            envoi_time = now.replace(hour=heure_envoi, minute=minute_envoie, second=0, microsecond=0)

            # Vérifier si l'heure d'envoi est trop proche
            if envoi_time <= now + timedelta(minutes=2):
                envoi_time = now + timedelta(minutes=2)  # Ajuster à 2 minutes dans le futur

            heure_envoi = envoi_time.hour
            minute_envoi = envoi_time.minute
            pywhatkit.sendwhatmsg(numero_telephone,message,heure_envoi,minute_envoie,15,True,4)
            time.sleep(20)
                    # Incrémenter les minutes pour les envois suivants
            minute_envoie += 1
            if minute_envoie >= 60:
                minute_envoie = 0
                heure_envoi += 1
                if heure_envoi >= 24:
                    heure_envoi = 0
        messagebox.showinfo("Succès", "Tous les messages ont été envoyés avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi du message n°{i + 1}: {e}")
    finally :
        fenetre.destroy()
    

    
import tkinter as tk
def interface2():
    global entry_telephone, entry_message, entry_heure, entry_minute, entry_repetitions

    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Planificateur de message")
    root.attributes('-fullscreen', True)
    root.config(bg="#EFEFEF")
    # Création d'un cadre pour contenir les éléments
    frame = tk.Frame(root, padx=20, pady=5)
    frame.pack(expand=True)

    # Création des labels et champs de saisie
    tk.Label(frame, text="Numéro de téléphone:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5, padx=10)
    entry_telephone = tk.Entry(frame, width=30)
    entry_telephone.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Message à envoyer:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5, padx=10)
    entry_message = tk.Entry(frame, width=50)
    entry_message.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Heure d'envoi (HH):", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5, padx=10)
    entry_heure = tk.Entry(frame, width=10)
    entry_heure.grid(row=2, column=1, pady=5, sticky="w")

    tk.Label(frame, text="Minute d'envoi (MM):", font=("Arial", 12)).grid(row=3, column=0, sticky="w", pady=5, padx=10)
    entry_minute = tk.Entry(frame, width=10)
    entry_minute.grid(row=3, column=1, pady=5, sticky="w")

    tk.Label(frame, text="Nombre de répétitions:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", pady=5, padx=10)
    entry_repetitions = tk.Entry(frame, width=10)
    entry_repetitions.grid(row=4, column=1, pady=5, sticky="w")


    def recuperer_données():
        global entry_telephone, entry_heure, entry_minute, entry_repetitions,entry_message
        # Récupérer les valeurs des champs
        numero_telephone = entry_telephone.get()
        message=entry_message.get()
        heure_envoi = entry_heure.get()
        minute_envoi = entry_minute.get()
        repetitions = entry_repetitions.get()

        # Vérifier que les données sont valides
        if not numero_telephone or not heure_envoi or not minute_envoi or not repetitions:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        try:
            # Convertir l'heure, la minute et le nombre de répétitions en entiers
            heure_envoi = int(heure_envoi)
            minute_envoi = int(minute_envoi)
            repetitions = int(repetitions)
        except ValueError:
            messagebox.showerror("Erreur", "L'heure, la minute et les répétitions doivent être des nombres.")
            return
        # Affichage des données (ou envoi d'un message, etc.)
        messagebox.showinfo("Données reçues", f"Numéro: {numero_telephone}\nMessage: {message}\nHeure d'envoi: {heure_envoi}:{minute_envoi}\nRépétitions: {repetitions}")
        envoyer_message(numero_telephone,message,heure_envoi,minute_envoi,repetitions,root)

        # Bouton pour envoyer les données
    btn_envoyer = tk.Button(
        frame, 
        text="Envoyer", 
        font=("Arial", 12), 
        bg="green", 
        fg="white", 
        command=recuperer_données  
    )
    btn_envoyer.grid(row=5, column=0, columnspan=2, pady=10)
    # Résumé des informations
    resume_text = tk.StringVar()
    resume_text.set("Résumé : Les informations saisies vont être envoyée via whatsapp web au destinataire.")
    resume_label = tk.Label(
        root,
        textvariable=resume_text,
        font=("Arial", 12),
        bg="#EFEFEF",
        fg="black",
        justify="left",
        width=70,
        height=3,
        relief="sunken"
    )
    resume_label.pack(pady=(4,4))#permet l'affichage du label dans la fenetre

    # Historique des messages
    historique_label = tk.Label(root, text="Together to kill the old whatsapp :", font=("Arial", 12, "bold"), bg="#EFEFEF")
    historique_label.pack()
    texte=("Your ideas and thoughts mean so much to us,they can spark fresh strategies and open doors to creating amazing new possibilities together.\n"
    "Contact me: +212697997953\n"
    "Gmail:belarbizakaria18@gmail.com")
    historique_frame = tk.Text(root, width=60, height=4, font=("Times New Roman", 15), wrap="word")#wrap="word" : Enveloppe automatiquement le texte au mot suivant lorsqu'une ligne est trop longue.
    historique_frame.insert("1.0",texte)#insert("1.0", texte) :
                                        #1.0 indique où insérer le texte.
                                        #Le 1 correspond à la première ligne.
                                        #Le 0 correspond à la première position (colonne) de cette ligne.
    #Désactive la zone pour empêcher l'utilisateur de modifier le texte affiché.
    historique_frame.pack(pady=4)
    # Conseils
    aide_label = tk.Label(
        root,
        text=(
            "Conseils :\n"
            "- Assurez-vous que le numéro est valide (format international recommandé).\n"
            "- Utilisez le format 24 heures pour l'heure.\n"
            "- Connecter Whatsapp web à votre whatsapp d'usage"
        ),
        font=("Arial", 10),
        bg="#F5F5F5",
        fg="blue",
        justify="left",
        relief="groove"
    )
    aide_label.pack(pady=4)

        # Lancer la boucle principale de tkinter
    root.mainloop()


def effacer_root(fenetre_secondaire):
    fenetre_secondaire.destroy()
    
    

def effacer_root1(fenetre_principale):
    fenetre_principale.destroy() 
    interface2()

def interface():
   
    root1 = tkinter.Tk()
    root1.title("§ ZakaSched §")
    root1.attributes('-fullscreen', True)
    with open(r"C:\Users\lenovo\OneDrive\Images\18ae721c-46af-47a3-9252-bf1a31647b99.webp", "rb") as image_file:
        image_data = base64.b64encode(image_file.read())
 
# Décoder l'image et la charger dans tkinter
    image_data = base64.b64decode(image_data)
    image = Image.open(BytesIO(image_data))
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    # Créer un Canvas pour gérer le fond et les éléments
    canvas = tkinter.Canvas(root1, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Ajouter un texte rectangulaire au-dessus du logo
    label1 = tkinter.Label(
        root1,
        text="App d'envoie programmée des messages.\nCliquez sur commencer",
        bg="#E3F2FD",
        font=("Times New Roman", 24, "bold"),
        fg="#1E88E5",
        padx=20,  # Pour ajouter un peu d'espace à l'intérieur du rectangle
        pady=10
    )
    canvas.create_window(screen_width//2, screen_height//8, window=label1)

    # Bouton "Commencer" avec style modernisé
    boutton1 = tkinter.Button(
        root1,
        text="Commencer",
        command=lambda: effacer_root1(root1),
        font=("Times New Roman", 18, "bold"),
        bg="#28A745",
        fg="white",
        activebackground="#F5F5DC",
        activeforeground="white",
        cursor="hand2",
        bd=5,
        relief="raised"
    )
    canvas.create_window(screen_width//2, screen_height//2+200, window=boutton1)

    # Déplacer "Made by Zakariae" vers la droite
    # Définir les participants
        # Définir les participants
    participants = ["BELARBI Zakariae"]
    participants_text = "\n".join(participants)

    # Taille du texte (ajustement manuel selon police et taille)
    text_width = 180  # Largeur estimée du texte
    text_height = 50  # Hauteur estimée du texte (deux lignes)

    # Dimensions dynamiques du rectangle
    rect_padding = 10  # Espace supplémentaire autour du texte
    rect_x1 = screen_width - text_width - 2 * rect_padding
    rect_y1 = screen_height - text_height - 2 * rect_padding
    rect_x2 = screen_width - 20
    rect_y2 = screen_height - 20

    # Créer le rectangle
    cadre_participants = canvas.create_rectangle(
        rect_x1, rect_y1, rect_x2, rect_y2,
        fill="#FFFFFF", outline="#1E88E5", width=5
    )

    # Centrer le texte à l'intérieur du rectangle
    label_x = (rect_x1 + rect_x2) // 2  # Centre horizontal
    label_y = (rect_y1 + rect_y2) // 2  # Centre vertical

    # Créer le label pour le texte
    participants_label = tkinter.Label(
        root1,
        text=f"Made by :\n{participants_text}",
        bg="#FFFFFF",
        fg="#1E88E5",
        font=("Times New Roman", 14, "bold"),
        justify="center"  # Centrer le texte
    )

    # Ajouter le label au canvas
    canvas.create_window(label_x, label_y, window=participants_label)


    # Ajouter le label au canvas
    canvas.create_window(label_x, label_y, window=participants_label)



    root1.mainloop()
interface()