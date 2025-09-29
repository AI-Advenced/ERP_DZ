# ERP Algeria - Système de Gestion Intégré Complet

## Description

ERP Algeria est un système de gestion d'entreprise (Enterprise Resource Planning) complet et moderne, spécialement conçu pour répondre aux besoins des entreprises algériennes. Ce système intègre plus de 30 modules métiers couvrant tous les aspects de la gestion d'entreprise.

## 🚀 Fonctionnalités Principales

### Modules Principaux
- **CRM Complet** - Gestion de la relation client
- **Comptabilité Professionnelle Algérienne** - Conforme aux normes algériennes
- **Gestion des Stocks** - Inventaire et approvisionnement
- **Ressources Humaines** - Gestion complète des employés
- **Ventes & Achats** - Cycle commercial complet
- **Trésorerie & Banques** - Gestion financière
- **Manufacturing** - Gestion de la production

### Modules Spécialisés
- **POS Restaurant Algérie** - Point de vente pour restaurants
- **Gestion Pharmacie** - Spécialement pour les pharmacies algériennes
- **Oil & Gas** - Gestion pétrolière et gazière
- **Ingénierie & Construction** - Gestion des projets BTP
- **Healthcare** - Gestion hospitalière et médicale
- **Banking & Finance** - Services bancaires et financiers
- **E-commerce & Marketplaces** - Commerce électronique
- **Supply Chain Management** - Chaîne d'approvisionnement
- **Business Intelligence** - Tableaux de bord et analyses

### Modules Techniques
- **WMS** - Gestion d'entrepôt
- **Transport & Flotte** - Gestion des véhicules
- **Maintenance & Actifs** - Gestion des équipements
- **Qualité** - Management de la qualité
- **Risk Management** - Gestion des risques
- **RPA** - Automatisation des processus
- **Helpdesk** - Support technique

## 🛠️ Technologies Utilisées

- **Backend**: FastAPI (Python 3.8+)
- **Base de données**: SQLite (développement) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Desktop**: PyWebView pour l'application bureau
- **ORM**: SQLAlchemy
- **Templates**: Jinja2

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- SQLite3

## ⚡ Installation Rapide

1. **Cloner le repository**
```bash
git clone https://github.com/votre-username/erp-algeria.git
cd erp-algeria
```
    Créer un environnement virtuel

python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

    Installer les dépendances

pip install -r requirements.txt

    Initialiser la base de données

python -c "from app.database import init_db; init_db()"

    Lancer l'application

python app/main.py

🐳 Installation avec Docker

# Construction de l'image
docker build -t erp-algeria .

# Lancement du conteneur
docker run -p 8000:8000 erp-algeria

Ou avec Docker Compose :

docker-compose up -d

🔧 Configuration
Variables d'environnement

Créez un fichier .env :

DATABASE_URL=sqlite:///./erp_algeria_complet.db
SECRET_KEY=your-secret-key-here
DEBUG=True
HOST=127.0.0.1
PORT=8000

Configuration de production

Pour la production, modifiez DATABASE_URL dans config.py :

DATABASE_URL = "postgresql://user:password@localhost/erp_algeria"

📖 Documentation API

Une fois l'application lancée, accédez à :

    Documentation interactive : http://127.0.0.1:8000/docs
    Documentation ReDoc : http://127.0.0.1:8000/redoc

🧪 Tests

# Lancer les tests
pytest

# Tests avec couverture
pytest --cov=app tests/

🚀 Déploiement
Production avec Gunicorn

gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker

Nginx (reverse proxy)

server {
    listen 80;
    server_name votre-domaine.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

🔒 Sécurité

    Authentification JWT intégrée
    Gestion des rôles et permissions
    Chiffrement des données sensibles
    Audit trail complet
    Sauvegarde automatique

📞 Support & Contribution
Contribution

    Fork le projet
    Créer une branche (git checkout -b feature/AmazingFeature)
    Commit (git commit -m 'Add AmazingFeature')
    Push (git push origin feature/AmazingFeature)
    Ouvrir une Pull Request

Support

    📧 Email: support@erp-algeria.com
    💬 Discord: Serveur ERP Algeria

    📚 Documentation: docs.erp-algeria.com

📄 Licence

Distribué sous licence MIT. Voir LICENSE pour plus d'informations.
🏆 Crédits

    Développé avec ❤️ pour les entreprises algériennes
    Merci à toute la communauté open source

ERP Algeria v2.0.0 - Système de gestion intégré moderne pour l'Algérie
