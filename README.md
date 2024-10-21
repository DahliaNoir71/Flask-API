# Projet Flask-API

## Table des Matières
- [Introduction](#introduction)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Endpoints de l'API](#endpoints-de-lapi)
- [Contribution](#contribution)
- [Licence](#licence)

## Introduction
Ce projet est une API RESTful construite avec Flask, conçue pour fournir divers services. L'API est conçue pour être légère, rapide et facile à utiliser, en utilisant plusieurs bibliothèques Python pour différentes fonctionnalités telles que la géolocalisation, la gestion des données et l'apprentissage automatique.

## Fonctionnalités
- Gestion des utilisateurs (opérations CRUD)
- Conception d'API RESTful
- Utilisation de Flask

## Installation

### Prérequis
- Python 3.12.7
- Flask
- Jinja2
- Werkzeug
- Click
- Geopy
- Networkx
- Numpy
- Pandas
- Pip
- Pytz
- Requests
- Scikit-learn
- Scipy
- Six

### Étapes
1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votreutilisateur/votre-repo-name.git
    ```
2. Accédez au répertoire du projet :
    ```bash
    cd votre-repo-name
    ```
3. Créez un environnement virtuel :
    ```bash
    python -m venv venv
    ```
4. Activez l'environnement virtuel :
    - Sous Windows :
        ```bash
        venv\Scripts\activate
        ```
    - Sous macOS/Linux :
        ```bash
        source venv/bin/activate
        ```
5. Installez les packages requis :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation
1. Lancez l'application Flask :
    ```bash
    flask run
    ```
2. L'API sera accessible à `http://127.0.0.1:5000/`.

## Endpoints de l'API
Voici quelques exemples de endpoints. Consultez le code pour une liste complète des endpoints disponibles.

### Gestion des Utilisateurs
- **GET /users** : Récupère une liste d'utilisateurs.
- **POST /users** : Crée un nouvel utilisateur.
- **GET /users/<id>** : Récupère un utilisateur spécifique par ID.
- **PUT /users/<id>** : Met à jour un utilisateur spécifique par ID.
- **DELETE /users/<id>** : Supprime un utilisateur spécifique par ID.

## Contribution
Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou soumettre une pull request pour toute modification ou amélioration.

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.