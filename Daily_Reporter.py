# Daily Reporter

'''
    PURPOSE : This code is a tool that collect daily feed back from eployee about their missions of the day
    AUTHOR : A. BRAURE
    Last update DATE : 2/10/2025

    Input :
    - 

    Ouput : 
    - 
'''


# Libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import date
from pathlib import Path


# Functions
def ask_id():
    '''
        PURPOSE : This function ask the user to fulfill is name and surname

        Input : 
        - NaN

        Output: 
        - name and SURNAME of the user as a single str
    '''
    
    user = str(input("Entrez votre prénom NOM : "))

    return user

def ask_missions():
    '''
        PURPOSE : This function ask the user to fulfill what have been done today

        Input : 
        - NaN

        Output: 
        - Missions of the day as a single str
    '''
    
    missions = str(input("Qu'avez-vous fais aujourd'hui ? "))

    return missions

def ask_strong():
    '''
        PURPOSE : This function ask the user to fulfill the strong point of the day

        Input : 
        - NaN

        Output: 
        - strong point of the day as a single str
    '''
    
    good_pts = str(input("Qu'elle etait le point positif du jour / La plus grosse réussite ? "))

    return good_pts

def ask_weak():
    '''
        PURPOSE : This function ask the user to fulfill the weak point of the day

        Input : 
        - NaN

        Output: 
        - strong point of the day as a single str
    '''
    
    weak_pts = str(input("Qu'elle etait le point negatif du jour / La plus grosse difficulté ? "))

    return weak_pts

def daily_report_md(
    chemin_sortie: str,
    name: str,
    missions: str,
    strong_pts: str,
    weak_pts: str,
) -> str:
    """
        Purpose : Génère un fichier Markdown au format "Daily Report".

        Input : 
        - chemin_sortie : chemin du fichier .md à créer
        - name : nom de la personne
        - missions : missions de la journée (chaîne ou texte multi-ligne)
        - strong_pts : points forts
        - weak_pts : points à améliorer
        - date_doc : date du rapport (par défaut = date du jour)

        Output : 
        - fichier : Path where the md is saved 
    """
    date_doc = str(date.today())

    contenu = f"""# Daily Report 
Name : {name}
Date : {date_doc}
    
## Missions of the day : 
{missions}

## Strong point : 
{strong_pts}
    
## Thing to improve : 
{weak_pts}
"""

    # Écriture du fichier
    name_b = name.replace(" ", "_")
    p = Path(chemin_sortie)
    p.mkdir(parents=True, exist_ok=True)
    fichier = p / f"{name_b}_{date_doc}.md"

    fichier.write_text(contenu, encoding="utf-8")

    return str(fichier)


# Inputs
expediteur = "ton_mail@gmail.com"
mot_de_passe = "ton_mot_de_passe"  # ⚠️ utilise un mot de passe d'application
destinataire = "destinataire@mail.com"

# Main
if __name__ == "__main__":
    ## Write the markdown
    name = ask_id()
    missions = ask_missions()
    strong_pts = ask_strong()
    weak_pts = ask_weak()
    p = daily_report_md("Reports/", name, missions, strong_pts, weak_pts)


# End.