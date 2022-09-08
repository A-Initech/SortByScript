#-------------------------------------------------------------------------------
# Name:        Sortbyme
# Purpose:
#
# Author:      Grelou
#
# Created:     05/06/2021
# Copyright:   (c) Grelou 2021
# Licence:     <Greltik Indepance>
#-------------------------------------------------------------------------------

#Trie les fichiers d'un repertoire par type
import glob
import os
import shutil
import tkinter
from tkinter import *

#INTERFACE GRAPHIQUE
app = tkinter.Tk()
app.geometry("640x480")
app.title("SortByScript")
app.config(background="#582ea0")
app.iconbitmap("logo.ico")



#TEXTE
label_title= Label(app,text="SortByScript Alpha 0.1",font=("Courrier",20),bg ='#582ea0', fg='white')
label_title.pack(expand=YES)
#TEXTE 2
bouton = tkinter.Button (text ="Votre programme de rangement automatique",font=("Courrier",10),bg ='#582ea2', fg='white')

label_sub= Label(app,text="Commencer",font=("Courrier",18),bg ='#582ea0', fg='white')
label_sub.pack(expand=YES)


#Widget
mainmenu= tkinter.Menu(app)
#Boucle Principale
app.config(menu=mainmenu)
app.mainloop()



#DEBUT DU PROGRAMME
from os import path
extensionDocuments = ['.docx','.pdf','.pptx']
extensionMedia = ['.pnj','.jpeg','.png','.avi','.mkv','.mp4','.mp3']
extensionSource = ['.zip','.exe','.EXE','.7z','.msi','.torrent','.jar','.img','.rar','.gz','.xz','.iso']

base_folder = "C:\Users\Grelou\Downloads"
docFiles = os.path.join(base_folder,'Documents')
mediaFiles = os.path.join(base_folder,'Media')
SourceFiles = os.path.join(base_folder,'Source')
#LISTER LES CONTENUE D'UN REPERTOIRE
files =glob.glob(os.path.join(base_folder,"*"))

#TROUVER L'EXTENSION ET LISTER LES FICHIERS PAR TYPES


#DEPLACE DANS DOSSIER DOCUMENTS
for file in files :
 extension = os.path.splitext(file)[1].lower()
 if extension in extensionDocuments :

     if path.exists(docFiles):
        shutil.move(file,docFiles)
     else:
          os.mkdir(docFiles)
          shutil.move(file,docFiles)

#DEPLACE DANS DOSSIER MEDIA
for file in files :
 extension = os.path.splitext(file)[1].lower()
 if extension in extensionMedia :

     if (path.exists(mediaFiles)):
        shutil.move(file,mediaFiles)
     else:
          os.mkdir(mediaFiles)
          shutil.move(file,mediaFiles)

#DEPLACE DANS DOSSIER SOURCE
for file in files :
 extension = os.path.splitext(file)[1].lower()
 if extension in extensionSource :

     if (path.exists(SourceFiles)):
        shutil.move(file,SourceFiles)
     else:
          os.mkdir(SourceFiles)
          shutil.move(file,SourceFiles)
