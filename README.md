# Script d'Automatisation TikTok

Ce script d'automatisation utilise Pyppeteer pour interagir avec TikTok. Il permet de se connecter à TikTok, de rechercher un utilisateur, de le suivre, d'aimer ses vidéos et de poster des commentaires prédéfinis.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir les éléments suivants installés :

- Python 3.x
- Pyppeteer (`pip install pyppeteer`)
- asyncio (pré-installé avec Python 3.7+)
- Fichiers JSON contenant les informations utilisateur et les commentaires.
  
## Installation

1.Clonez
   ```bash
   git clone https://github.com/Theprogrammer-X007/Followers-Tiktok_bot.git
   ```
   ```bash
   cd Followers-Tiktok_bot
   ```

2. Installez les dépendances nécessaires :
```bash
pip install pyppeteer
```

3. Créez les fichiers JSON des utilisateurs et des commentaires en exécutant le script. Les fichiers sont générés automatiquement s'ils n'existent pas.

```bash
python TikTok-followers.py
```

Utilisation

1. Modifier le fichier le fichier tiktok_users.jsonavec l'identifiant de votre compte TikTok :
```bash
{
    "users": [
        {"username": "votre_nom_utilisateur_tiktok", "password": "votre_mot_de_passe"}
    ]
}

```

2. Modifier le fichier le fichiercomments.json avec les commentaires que vous souhaitez publier :
```bash
{
    "comments": [
        "Bon contenu",
        "Tu es le meilleur",
        "Continue comme ça"
    ]
}

```

3.Exécutez le script:

```bash
python script.py
```
ous serez invité à entrer le nom de l'utilisateur que vous souhaitez rechercher sur TikTok.



# Fonctionnalités

**Connexion à TikTok : Utilise les identifiants fournis dans le fichier tiktok_users.json**

**Recherche d'un utilisateur : Permet de rechercher un utilisateur par son nom.**

**Suivre l'utilisateur : Suivre l'utilisateur trouvé.**

**Interaction avec les vidéos: Aimer les vidéos de l'utilisateur**

**Commenter les vidéos : Poster des commentaires aléatoires issus d'une liste prédéfinie dans le fichier comments.json.**


# JSON files

tiktok_users.json:Contient les identifiants de connexion des utilisateurs TikTok.

comments.json: Contient les commentaires que le script peut poster sur les vidéos TikTok.


Les deux fichiers sont créés automatiquement s'ils n'existent pas. Assurez-vous de les modifier avec les informations adéquates.

# Attention

Ce script est destiné uniquement à des fins éducatives. L'utilisation non autorisée de bots ou de scripts d'automatisation sur des plateformes comme TikTok peut enfreindre leurs conditions d'utilisation. Utilisez ce script à vos risques et périls.

# Contributions

Si vous avez des suggestions ou des améliorations, n'hésitez pas à forker le projet et à envoyer une pull request.

# Developpeur :@The programmer

**Developer:** @The programmer
