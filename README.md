# Followers-Tiktok_bot

Script d'Automatisation TikTok

Ce script d'automatisation utilise Pyppeteer pour interagir avec TikTok. Il permet de se connecter à TikTok, rechercher un utilisateur, le suivre, aimer ses vidéos, et poster des commentaires prédéfinis.

Prérequis

Avant de lancer le script, assurez-vous d'avoir installé les éléments suivants :

Python 3.x
Pyppeteer (pip install pyppeteer)
asyncio (pré-installé avec Python 3.7+)

Installation

1. Clonez le dépôt :
git clone https://github.com/Theprogrammer-X007/Followers-Tiktok.git

cd followers-tiktok

2.Installez les dépendances nécessaires :
pip install pyppeteer

3. Créez les fichiers JSON des utilisateurs et des commentaires en exécutant le script. Les fichiers sont automatiquement générés s’ils n’existent pas.

python TikTok-followers.py

Utilisation

1. Modifiez le fichier tiktok_utilisateurs.json avec les identifiants de vos utilisateurs TikTok :

{
    "utilisateurs": [
        {"nom_utilisateur": "votre_nom_utilisateur_tiktok", "mot_de_passe": "votre_mot_de_passe"}
    ]
}


2. Modifiez le fichier commentaires.json avec les commentaires que vous souhaitez poster :

{
    "commentaires": [
        "Bonne vidéo",
        "Tu es le meilleur",
        "Continue comme ça"
    ]
}


3. Lancez le script :

python script.py

Vous serez invité à entrer le nom de l’utilisateur que vous souhaitez rechercher sur TikTok.



Fonctionnalités

Connexion à TikTok : Utilisez les identifiants fournis dans le fichier tiktok_utilisateurs.json.

Rechercher un utilisateur : Trouvez le nom d’utilisateur que vous entrez lorsque le script vous le demande.

Suivre un utilisateur : Suivez l’utilisateur trouvé.

Interagir avec les vidéos : Aimez les vidéos de l’utilisateur.

Commenter les vidéos : Postez des commentaires aléatoires à partir d’une liste prédéfinie dans le fichier commentaires.json.


Fichiers JSON

tiktok_utilisateurs.json : Contient les identifiants de connexion des utilisateurs TikTok.

commentaires.json : Contient les commentaires que le script peut publier sur les vidéos TikTok.


Ces deux fichiers sont créés automatiquement s’ils n’existent pas. Assurez-vous de les remplir avec les informations appropriées.

Avertissement

Ce script est destiné à des fins éducatives uniquement. L'utilisation non autorisée de bots ou de scripts d'automatisation sur des plateformes comme TikTok peut enfreindre leurs politiques d'utilisation. Utilisez ce script à vos risques et périls.

Contributions

Si vous avez des suggestions ou des améliorations, n'hésitez pas à forker le projet et à envoyer une pull request.

Développeur : @The programmer



