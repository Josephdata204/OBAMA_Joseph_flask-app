# 🐳 joseph-flask-app — TP Docker & DevOps

> **CC1 - Conduite de Projet (Agile, DevOps, Kanban)**  
> Travail individuel — Université de Yaoundé I  
> **Auteur :** Joseph

---

## 📁 Structure du projet

```
tp-docker/
├── app/
│   ├── app.py                  # Application Flask
│   ├── requirements.txt        # Dépendances Python
│   ├── Dockerfile              # Image Docker
│   └── commandes_historique.txt # Historique des commandes
├── jenkins/
│   └── pipeline.yml            # Jenkinsfile CI/CD
├── pritunl-vpn/
│   ├── docker-compose.yml      # Orchestration Pritunl + MongoDB
│   ├── .env                    # Variables d'environnement (non commité)
│   └── volumes/
│       ├── pritunl/            # Données persistantes Pritunl
│       └── mongodb/            # Données persistantes MongoDB
└── README.md
```

---

## TP1 — Docker (Dockerfile, Image, Conteneur)

### Lancer l'application localement

```bash
# 1. Cloner le dépôt
git clone https://github.com/josephndoumbe/joseph-flask-app.git
cd joseph-flask-app/app

# 2. Construire l'image
docker build -t joseph-flask-app .

# 3. Lancer le conteneur
docker run -d -p 5000:5000 --name joseph-flask-container joseph-flask-app

# 4. Accéder à l'application
# http://localhost:5000
```

### Image DockerHub
🔗 [https://hub.docker.com/r/josephndoumbe/joseph-flask-app](https://hub.docker.com/r/josephndoumbe/joseph-flask-app)

```bash
# Récupérer et lancer directement depuis DockerHub
docker pull josephndoumbe/joseph-flask-app:latest
docker run -d -p 5000:5000 josephndoumbe/joseph-flask-app:latest
```

---

## TP2 — CI/CD Jenkins

Le pipeline Jenkins (dans `jenkins/pipeline.yml`) automatise :
1. **Clonage** — Clone `app.py` et `requirements.txt` depuis GitHub
2. **Image** — Construit l'image Docker
3. **Publication** — Pousse l'image sur DockerHub

### Prérequis Jenkins
- Plugin Docker Pipeline installé
- Credentials DockerHub ajoutés avec l'ID : `dockerhub-credentials`

---

## TP3 — Docker Compose (Pritunl VPN)

```bash
cd pritunl-vpn

# Vérifier le module tun
lsmod | grep tun
# Si absent : sudo modprobe tun

# Lancer les services
docker-compose up -d

# Vérifier les conteneurs
docker-compose ps

# Voir les logs
docker-compose logs -f

# Arrêter
docker-compose down
```

**Accès à l'interface Pritunl :** https://localhost

---

## TP4 — Trello / Jira

Projet planifié dans Trello et Jira avec les pratiques Agile vues en cours.  
L'utilisateur `thomslegeni@gmail.com` a été invité au projet.

---

## 🔗 Liens

| Ressource | Lien |
|-----------|------|
| Dépôt GitHub | https://github.com/josephndoumbe/joseph-flask-app |
| Image DockerHub | https://hub.docker.com/r/josephndoumbe/joseph-flask-app |
| Application Web | http://localhost:5000 |
