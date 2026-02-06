# Stage 1: Builder [cite: 63]
FROM python:3.11-slim as builder

WORKDIR /app

# Installation des dépendances dans un dossier local
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime [cite: 66]
FROM python:3.11-alpine

WORKDIR /app

# Copie des bibliothèques depuis le builder
COPY --from=builder /install /usr/local

# Copie du code source
COPY app/ app/

# Créer un utilisateur non-root pour la sécurité [cite: 68]
RUN adduser -D myuser
USER myuser

# Exposer le port 5000 [cite: 69]
EXPOSE 5000

# Lancer l'application
CMD ["python", "app/main.py"]