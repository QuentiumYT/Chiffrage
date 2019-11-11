import os, sys, urllib.request
from tkinter import *
from tkinter.messagebox import *

__version__ = 3
__filename__ = "Chiffrage"
__basename__ = os.path.basename(sys.argv[0])
__savepath__ = os.path.join(os.environ['APPDATA'], "QuentiumPrograms")
__iconpath__ = __savepath__ + "/{}.ico".format(__filename__)

try:urllib.request.urlopen("https://www.google.fr/", timeout=1); connection = True
except:connection = False
if not os.path.exists(__iconpath__):
    try:os.mkdir(__savepath__)
    except:pass
    if connection == True:
        try:urllib.request.urlretrieve("http://quentium.fr/+++PythonDL/{}.ico".format(__filename__), __iconpath__)
        except:pass

if connection == True:
    try:script_version = int(urllib.request.urlopen("http://quentium.fr/programs/index.php").read().decode().split(__filename__ + "<!-- Version: ")[1].split(" --></h2>")[0])
    except:script_version = __version__
    if script_version > __version__:
        if os.path.exists(__iconpath__):popup = Tk(); popup.attributes("-topmost", 1); popup.iconbitmap(__iconpath__); popup.withdraw()
        ask_update = askquestion(__filename__ + " V" + str(script_version), "Une mise à jour à été trouvée, souhaitez vous la télécharger puis l'éxécuter ?", icon="question")
        if ask_update == "yes":
            try:os.rename(__basename__, __filename__ + "-old.exe")
            except:os.remove(__filename__ + "-old.exe"); os.rename(__basename__, __filename__ + "-old.exe")
            if "-32" in str(__basename__):urllib.request.urlretrieve("http://quentium.fr/download.php?file={}-32.exe".format(__filename__), __filename__ + ".exe")
            else:urllib.request.urlretrieve("http://quentium.fr/download.php?file={}.exe".format(__filename__), __filename__ + ".exe")
            showwarning(__filename__, "Le programme va redémarrer pour fonctionner sous la nouvelle version.", icon="warning")
            os.system("start " + __filename__ + ".exe"); os._exit(1)

__filename__ = __filename__ + " V" + str(__version__)

from tkinter.filedialog import *
from tkinter.scrolledtext import *
from tkinter import *

def chiffrage(chaine, cle):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(\/][}{_èçàéù*-+=.,?!;:"
    liste = ""
    for caractere in chaine:
        try:
            index = alpha.index(caractere)
            numero = index + cle
            cle = cle + cle
            if cle > 85:
                cle = cle - 85
            if numero > 85:
                numero = numero - 86
            liste+=alpha[numero]
        except:
            liste+=caractere
    return liste

def dechiffrage(chaine, cle):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(\/][}{_èçàéù*-+=.,?!;:"
    liste = ""
    for caractere in chaine:
        try:
            index = alpha.index(caractere)
            numero = index - cle
            cle = cle + cle
            if cle > 85:
                cle = cle - 85
            if numero < 0:
                numero = numero + 86
            liste+=alpha[numero]
        except:
            liste+=caractere
    return liste

def make_cipher():
    try:
        key_cipher = int(value_key_cipher.get())
        mot_cipher = value_text_cipher.get()
        if key_cipher <= 85:
            result_cipher = chiffrage(mot_cipher, key_cipher)
            canvas.insert(canvas_id, 5000, "CHIFFREMENT :" + "\n")
            canvas.insert(canvas_id, 5000, "Le mot à chiffrer est > " +str(mot_cipher) + "\n")
            canvas.insert(canvas_id, 5000, "La clée pour chiffrer est > " +str(key_cipher) + "\n")
            canvas.insert(canvas_id, 5000, "Le mot chiffré est > ")
            canvas.insert(canvas_id, 5000, str(result_cipher) + "\n" + "\n")
            canvas.configure(scrollregion=canvas.bbox("all"))
            txtBox.mark_set(INSERT, END)
            txtBox.insert(INSERT, str(result_cipher))
            txtBox.insert(INSERT, "\n")
        else:
            showwarning("Erreur", "La clée de chiffrement ne doit pas dépasser 85 !")
            return False
    except:
        showwarning("Erreur", "La clée de chiffrement n'est pas un nombre !")

def make_decipher():
    try:
        key_decipher = int(value_key_decipher.get())
        mot_decipher = value_text_decipher.get()
        if key_decipher <= 85:
            result_decipher = dechiffrage(mot_decipher, key_decipher)
            canvas.insert(canvas_id, 5000, "DECHIFFREMENT :" + "\n")
            canvas.insert(canvas_id, 5000, "Le mot à déchiffrer est > " +str(mot_decipher) + "\n")
            canvas.insert(canvas_id, 5000, "La clée pour déchiffrer est > " +str(key_decipher) + "\n")
            canvas.insert(canvas_id, 5000, "Le mot déchiffré est > " +str(result_decipher) + "\n" + "\n")
            canvas.configure(scrollregion=canvas.bbox("all"))
            txtBox.mark_set(INSERT, END)
            txtBox.insert(INSERT, str(result_decipher))
            txtBox.insert(INSERT, "\n")
        else:
            showwarning("Erreur", "La clée de déchiffrement ne doit pas dépasser 85 !")
            return False
    except:
        showwarning("Erreur", "La clée de déchiffrement n'est pas un nombre !")

def menu_chiffrage():
    menu_chiffrage = Tk()
    if os.path.exists(__iconpath__):
        menu_chiffrage.iconbitmap(__iconpath__)
    width = 800
    height = 180
    menu_chiffrage.update_idletasks()
    x = (menu_chiffrage.winfo_screenwidth() - width) // 2
    y = (menu_chiffrage.winfo_screenheight() - height) // 2
    menu_chiffrage.geometry("{}x{}+{}+{}".format(width , height, int(x), int(y)))
    menu_chiffrage.title("Informations Chiffrement")
    menu_chiffrage.resizable(width=False, height=False)
    Label(menu_chiffrage, text="Le chiffrement se fait avec les caractères :", font="impact 15").pack(pady=5)
    Label(menu_chiffrage, text="'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(\/][}{_èçàéù*-+=.,?!;:'", font="impact 15").pack(pady=5)
    Label(menu_chiffrage, text="remplaçant les lettres de votre mot à chiffrer par d'autre lettres grâce à l'algorythme de césar,", font="impact 15").pack(pady=5)
    Label(menu_chiffrage, text="dépendant de votre clé de crypatge. La clée de chiffrement ne doit pas dépasser 85 !", font="impact 15").pack(pady=5)

def menu_dechiffrage():
    menu_dechiffrage = Tk()
    if os.path.exists(__iconpath__):
        menu_dechiffrage.iconbitmap(__iconpath__)
    width = 800
    height = 180
    menu_dechiffrage.update_idletasks()
    x = (menu_dechiffrage.winfo_screenwidth() - width) // 2
    y = (menu_dechiffrage.winfo_screenheight() - height) // 2
    menu_dechiffrage.geometry("{}x{}+{}+{}".format(width , height, int(x), int(y)))
    menu_dechiffrage.title("Informations Déchiffrement")
    menu_dechiffrage.resizable(width=False, height=False)
    Label(menu_dechiffrage, text="Le déchiffrement se fait avec les caractères :", font="impact 15").pack(pady=5)
    Label(menu_dechiffrage, text="'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(\/][}{_èçàéù*-+=.,?!;:'", font="impact 15").pack(pady=5)
    Label(menu_dechiffrage, text="remplaçant les lettres de votre mot chiffré par d'autres lettres grâce à l'algorythme de césar,", font="impact 15").pack(pady=5)
    Label(menu_dechiffrage, text="dépendant de votre clé de décrypatge. La clée de déchiffrement ne doit pas dépasser 85 !", font="impact 15").pack(pady=5)

def onclose():
    if askokcancel("Quitter", "Voulez vous quitter le programme ?"):
        win_cipher.destroy()

def notclose():
    return

def propos():
    win_propos = Tk()
    win_propos.configure(bg = "lightgray")
    if os.path.exists(__iconpath__):
        win_propos.iconbitmap(__iconpath__)
    width = 350
    height = 250
    win_propos.update_idletasks()
    x = (win_propos.winfo_screenwidth() - width) // 2
    y = (win_propos.winfo_screenheight() - height) // 2
    win_propos.geometry("{}x{}+{}+{}".format(width , height, int(x), int(y)))
    win_propos.title("A propos")
    win_propos.protocol("WM_DELETE_WINDOW", notclose)
    win_propos.resizable(width=False, height=False)
    Label(win_propos, text="Programme crée et designé par Quentium. \n Pour plus d'informations, \n merci de me contacter par e-mail : \n quentin.lienhardt@gmail.com", font="impact 15", fg="black", bg="lightgray").pack(pady=20)
    def close():
        win_propos.destroy()
    Button(win_propos, text="Fermer", relief=GROOVE, width = 10, font="impact 15", fg="black", command=close).pack(pady=20)

def mouse_wheel(event):
    direction = 0
    if event.num == 5 or event.delta == -120:
        direction = 1
    if event.num == 4 or event.delta == 120:
        direction = -1
    canvas.yview_scroll(direction, "units")

win_cipher = Tk()
win_cipher.configure(bg = "lightgray")
if os.path.exists(__iconpath__):
    win_cipher.iconbitmap(__iconpath__)
win_cipher.state("zoomed")
win_cipher.title("Programme de chiffrage V" + str(__version__))
win_cipher.protocol("WM_DELETE_WINDOW", onclose)

canvas = Canvas(win_cipher, width=960, background="white")
scroll = Scrollbar(win_cipher, orient=VERTICAL)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=canvas.yview)
canvas.config(yscrollcommand=scroll.set)
canvas.pack(side=RIGHT, fill=BOTH)
canvas.bind("<MouseWheel>", mouse_wheel)

canvas_id = canvas.create_text(10, 10, font="impact 12", anchor="nw")

txtBox = Text(canvas, height = 10, wrap = WORD, font="impact 15")
txtBox.grid(row = 0, column = 0, sticky = W)
txtBox.pack(side=BOTTOM)

Label(win_cipher, text="Entrez ci-dessous la clée de chiffrement :", font="impact 15", fg="black", bg="lightgray").pack(pady=20)
value_key_cipher = StringVar()
value_key_cipher.set("")
Entry(win_cipher, textvariable=value_key_cipher, width=30, font="impact 15").pack()
Label(win_cipher, text="Entrez ci-dessous le mot à chiffrer :", font="impact 15", fg="black", bg="lightgray").pack(pady=20)
value_text_cipher = StringVar()
value_text_cipher.set("")
Entry(win_cipher, textvariable=value_text_cipher, width=30, font="impact 15").pack()
Button(win_cipher, text="Chiffrer !", relief=GROOVE, width = 20, font="impact 15", fg="black", command=make_cipher).pack(pady=20)

Label(win_cipher, text="Entrez ci-dessous la clée de déchiffrement :", font="impact 15", fg="black", bg="lightgray").pack(pady=20)
value_key_decipher = StringVar()
value_key_decipher.set("")
Entry(win_cipher, textvariable=value_key_decipher, width=30, font="impact 15").pack()
Label(win_cipher, text="Entrez ci-dessous le mot à déchiffrer :", font="impact 15", fg="black", bg="lightgray").pack(pady=20)
value_text_decipher = StringVar()
value_text_decipher.set("")
Entry(win_cipher, textvariable=value_text_decipher, width=30, font="impact 15").pack()
Button(win_cipher, text="Déchiffrer !", relief=GROOVE, width = 20, font="impact 15", fg="black", command=make_decipher).pack(pady=20)

menubar = Menu(win_cipher)
menu1 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menu1)
menu1.add_command(label="Chiffrement Infos", command=menu_chiffrage)
menu1.add_command(label="Déchiffrement Infos", command=menu_dechiffrage)
menu1.add_separator()
menu1.add_command(label="Quitter", command=onclose)
menu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Aide", menu=menu2)
menu2.add_command(label="A propos", command=propos)
win_cipher.config(menu=menubar)

win_cipher.mainloop()
