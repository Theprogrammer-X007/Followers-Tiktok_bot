import json
import os
import random
import asyncio
from typing import List, Dict
from pyppeteer import launch
from pyppeteer.page import Page
from pyppeteer.errors import TimeoutError

# Configuration
CONFIG = {
    'USERS_FILE': "tiktok_utilisateurs.json",
    'COMMENTS_FILE': "commentaires.json",
    'TIMEOUT': 10000,  # 10 secondes
    'DELAY_BETWEEN_ACTIONS': 2000,  # 2 secondes
    'MAX_RETRIES': 3
}

class TikTokBot:
    def __init__(self):
        self.browser = None
        self.page = None
        self.users = self._load_json(CONFIG['USERS_FILE'], "utilisateurs")
        self.comments = self._load_json(CONFIG['COMMENTS_FILE'], "commentaires")

    @staticmethod
    def _load_json(file_path: str, key: str) -> List:
        """Charge les données depuis un fichier JSON avec gestion d'erreurs."""
        try:
            if not os.path.exists(file_path):
                TikTokBot._create_example_file(file_path, key)
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f).get(key, [])
        except json.JSONDecodeError:
            print(f"Erreur: Le fichier {file_path} contient du JSON invalide.")
            return []
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier {file_path}: {str(e)}")
            return []

    @staticmethod
    def _create_example_file(file_path: str, key: str):
        """Crée un fichier JSON d'exemple avec la structure appropriée."""
        example_data = {
            "utilisateurs": [
                {"nom_utilisateur": "exemple_utilisateur1", "mot_de_passe": "exemple_motdepasse1"}
            ] if key == "utilisateurs" else [],
            "commentaires": ["Super vidéo!", "Excellent contenu!"] if key == "commentaires" else []
        }
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({key: example_data[key]}, f, indent=4, ensure_ascii=False)

    async def init_browser(self):
        """Initialise le navigateur avec des options optimisées."""
        self.browser = await launch(
            headless=False,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
            defaultViewport={'width': 1920, 'height': 1080}
        )
        self.page = await self.browser.newPage()
        await self.page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

    async def safe_click(self, selector: str, retry: int = 0):
        """Effectue un clic sécurisé avec retries et gestion d'erreurs."""
        try:
            await self.page.waitForSelector(selector, {'timeout': CONFIG['TIMEOUT']})
            element = await self.page.querySelector(selector)
            if element:
                await element.click()
                await asyncio.sleep(CONFIG['DELAY_BETWEEN_ACTIONS'] / 1000)
            else:
                raise Exception(f"Élément non trouvé: {selector}")
        except Exception as e:
            if retry < CONFIG['MAX_RETRIES']:
                await asyncio.sleep(1)
                await self.safe_click(selector, retry + 1)
            else:
                print(f"Erreur lors du clic sur {selector}: {str(e)}")

    async def login(self, username: str, password: str) -> bool:
        """Gère la connexion avec validation."""
        try:
            await self.page.goto("https://www.tiktok.com/login")
            await self.page.waitForSelector('input[name="username"]')
            await self.page.type('input[name="username"]', username)
            await self.page.type('input[name="password"]', password)
            await self.safe_click('button[type="submit"]')
            
            # Vérifie si la connexion a réussi
            try:
                await self.page.waitForSelector('div[data-e2e="search-icon"]', {'timeout': CONFIG['TIMEOUT']})
                return True
            except TimeoutError:
                print(f"Échec de connexion pour l'utilisateur {username}")
                return False
                
        except Exception as e:
            print(f"Erreur de connexion: {str(e)}")
            return False

    async def interact_with_user(self, target_username: str):
        """Interagit avec l'utilisateur cible de manière optimisée."""
        try:
            await self.page.type('input[type="text"]', target_username)
            await self.page.keyboard.press('Enter')
            await self.safe_click('a[data-e2e="search-user-card"]')
            await self.safe_click('button[data-e2e="user-follow"]')

            videos = await self.page.querySelectorAll('div[data-e2e="user-post-item"]')
            for video in videos[:3]:  # Limite à 3 vidéos pour éviter les blocages
                await video.click()
                await self.safe_click('div[data-e2e="like-icon"]')
                
                comment = random.choice(self.comments)
                await self.page.type('textarea[data-e2e="comment-input"]', comment)
                await self.page.keyboard.press('Enter')
                
                await self.safe_click('div[data-e2e="close-icon"]')
                await asyncio.sleep(random.uniform(2, 4))  # Délai aléatoire

        except Exception as e:
            print(f"Erreur lors de l'interaction: {str(e)}")

    async def run(self, target_username: str):
        """Point d'entrée principal avec gestion des erreurs."""
        if not self.users or not self.comments:
            print("Erreur: Fichiers de configuration vides ou invalides")
            return

        try:
            await self.init_browser()
            for user in self.users:
                if await self.login(user["nom_utilisateur"], user["mot_de_passe"]):
                    await self.interact_with_user(target_username)
                await asyncio.sleep(random.uniform(5, 10))  # Délai entre les comptes
        finally:
            if self.browser:
                await self.browser.close()

async def main():
    bot = TikTokBot()
    target_username = input("Entrez le nom d'utilisateur à chercher : ").strip()
    await bot.run(target_username)

if __name__ == "__main__":
    asyncio.run(main())