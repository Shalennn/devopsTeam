# devopsTeam
Exercice : API Inventory Python
TechCorp veut une API REST pour gérer ses serveurs. Même principe que l'exercice
précédent, mais avec du Python au lieu de HTML.
PARTIE 1 : Organisation Agile
Rôles
● Product Owner
● Scrum Master
● Dev/Ops (2-3 personnes)
User Stories
Rédigez ces 4 User Stories :
1. En tant que SysOps, je veux une API REST pour lister les serveurs afin
d'automatiser mes rapports.
2. En tant que Développeur, je veux un Dockerfile multi-stage afin d'optimiser la taille
de l'image.
3. En tant que QA, je veux des tests automatisés PyTest afin de valider que l'API
fonctionne.
4. En tant que DevOps, je veux un pipeline CI/CD complet afin de garantir la qualité du
code.
Definition of Done
Définissez vos critères pour qu'une tâche soit "Terminée".
Exemples :
● Code review fait ?
● Tests passés ?
● Image Docker < 100 MB ?
● Pipeline au vert ?
Tableau Kanban
Créez un board : Backlog | À faire | En cours | Review | Terminé
PARTIE 2 : L'API Flask
Structure du Projet
● inventory-api/
● ├── app/
● │ └── main.py
● ├── tests/
● │ └── test_api.py
● ├── requirements.txt
● ├── Dockerfile
● └── .github/workflows/ci-cd.yml
requirements.txt
● Flask==3.0.0
● pytest==7.4.3
● flake8==6.1.0
L'API à Créer
Créez une API Flask avec 3 endpoints :
1. Health Check :
- GET /api/v1/health → {"status": "OK", "version": "1.0"}
2. Liste des serveurs :
- GET /api/v1/servers → {"servers": [...], "count": 2}
3. Serveur par ID :
- GET /api/v1/servers/1 → {"id": 1, "hostname": "web-prod-01", ...}
- GET /api/v1/servers/999 → {"error": "Server not found"} (404)
Base de données
Utilisez une simple liste Python avec 2 serveurs :
● id: 1, hostname: "web-prod-01", ip: "10.0.0.1", status: "up"
● id: 2, hostname: "db-prod-01", ip: "10.0.0.2", status: "down"
Test manuel
● pip install -r requirements.txt
● python app/main.py
● curl http://localhost:5000/api/v1/servers
PARTIE 3 : Tests PyTest
Créez tests/test_api.py avec minimum 4 tests :
● Test que /health retourne 200
● Test que /servers retourne la liste
● Test que /servers/1 retourne le bon serveur
● Test que /servers/999 retourne 404
Commande
● pytest tests/ -v
PARTIE 4 : Dockerfile Multi-Stage
Structure en 2 Stages
Stage 1 "builder"
● Image de base : python:3.11-slim
● Installe les dépendances
Stage 2 "runtime"
● Image de base : python:3.11-alpine
● Copie uniquement ce qui est nécessaire
● Créer un utilisateur non-root
● Exposer le port 5000
Objectif
L'image finale doit faire moins de 100 MB.
Workflow
1. Créer la branche develop
2. Faire une modification sur develop
3. Push → Le pipeline crée une PR automatique
4. Merger la PR → Déploiement automatique