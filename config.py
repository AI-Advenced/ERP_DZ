"""
Configuration générale de l'application ERP Algeria
"""
import os
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Configuration de l'application"""
    
    # Configuration de base
    app_name: str = "ERP Algeria"
    app_version: str = "2.0.0"
    app_description: str = "Système de Gestion Intégré Complet pour l'Algérie"
    
    # Configuration du serveur
    host: str = "127.0.0.1"
    port: int = 8000
    debug: bool = True
    reload: bool = True
    
    # Base de données
    database_url: str = "sqlite:///./erp_algeria_complet.db"
    
    # Sécurité
    secret_key: str = "votre-clé-secrète-très-sécurisée-changez-moi"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS
    allowed_origins: list = ["*"]
    allowed_methods: list = ["*"] 
    allowed_headers: list = ["*"]
    
    # Uploads
    max_file_size: int = 10 * 1024 * 1024  # 10MB
    upload_dir: str = "uploads"
    
    # Email (optionnel)
    smtp_server: Optional[str] = None
    smtp_port: Optional[int] = 587
    smtp_username: Optional[str] = None
    smtp_password: Optional[str] = None
    
    # Algérie spécifique
    timezone: str = "Africa/Algiers"
    currency: str = "DZD"
    language: str = "fr"
    
    # Desktop app
    window_title: str = "ERP Algeria - Desktop"
    window_width: int = 1200
    window_height: int = 800
    window_resizable: bool = True
    window_maximized: bool = True
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instance globale des paramètres
settings = Settings()

# Configuration pour différents environnements
class DevelopmentConfig(Settings):
    debug: bool = True
    reload: bool = True
    database_url: str = "sqlite:///./erp_algeria_dev.db"


class ProductionConfig(Settings):
    debug: bool = False
    reload: bool = False
    database_url: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://user:password@localhost/erp_algeria_prod"
    )


class TestConfig(Settings):
    debug: bool = True
    database_url: str = "sqlite:///./test_erp_algeria.db"


def get_settings() -> Settings:
    """Retourne la configuration selon l'environnement"""
    env = os.getenv("ENVIRONMENT", "development").lower()
    
    if env == "production":
        return ProductionConfig()
    elif env == "test":
        return TestConfig()
    else:
        return DevelopmentConfig()
