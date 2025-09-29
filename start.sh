#!/bin/bash

echo "🚀 Démarrage d'ERP Algeria..."

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    exit 1
fi

# Créer l'environnement virtuel s'il n'existe pas
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances
echo "📥 Installation des dépendances..."
pip install -r requirements.txt

# Initialiser la base de données
echo "🗄️ Initialisation de la base de données..."
python -c "from app.database import init_db; init_db()"

# Créer les dossiers nécessaires
mkdir -p uploads logs static/css static/js static/images

# Démarrer l'application
echo "🎯 Démarrage de l'application..."
python app/main.py
