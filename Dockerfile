# --- STAGE 1 : Builder ---
# On utilise une image "slim" pour installer les dépendances proprement
FROM python:3.11-slim AS builder

WORKDIR /app

# On copie le fichier des dépendances
COPY requirements.txt .

# Installation des dépendances dans le dossier local de l'utilisateur
# --no-cache-dir permet de gagner de la place immédiatement
RUN pip install --user --no-cache-dir -r requirements.txt


# --- STAGE 2 : Runtime ---
# Image finale ultra-légère (Alpine) pour respecter l'objectif < 100 MB
FROM python:3.11-alpine

WORKDIR /app

# Création d'un utilisateur non-root pour la sécurité (Partie 4 du TP)
RUN adduser -D devopsuser
USER devopsuser

# On récupère uniquement les packages installés lors du premier stage
COPY --from=builder /root/.local /home/devopsuser/.local

# On copie le code source de l'application
COPY app/ .

# Configuration des variables d'environnement
# On ajoute le chemin des bibliothèques installées au PATH de l'utilisateur
ENV PATH=/home/devopsuser/.local/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# On expose le port 5000
EXPOSE 5000

# Commande pour lancer l'API Flask
CMD ["python", "main.py"]

