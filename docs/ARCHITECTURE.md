├── .env
├── app
│   ├── controllers
│   │   ├── auth
│   │   │   ├── LoginController.py
│   │   │   └── RegisterController.py
│   │   ├── TestController.py
│   │   └── UserController.py
│   └── models
│       ├── categorie.py
│       ├── file.py
│       ├── produit.py
│       ├── test.py
│       └── user.py
├── config
│   ├── app.py
│   ├── database.py
│   ├── log.py
│   └── session.py
├── creator
├── database
│   ├── creator.db
│   └── migrations
│       ├── 2024_10_07_create_categories_table.py
│       ├── 2024_10_07_create_produits_table.py
│       ├── 2024_12_10_create_tests_table.py
│       └── 2024_12_23_create_users_table.py
├── docs
│   └── ARCHITECTURE.md
├── lang
│   └── en
│       ├── alert.json
│       ├── custom.json
│       ├── password.json
│       ├── settings.json
│       └── validation.json
├── main.py
├── public
│   ├── .htaccess
│   ├── app.py
│   ├── assets
│   │   ├── css
│   │   │   └── creator.css
│   │   └── images
│   │       ├── logo
│   │       │   ├── favicon.ico
│   │       │   └── logo.png
│   │       └── test.png
│   ├── index-.html
│   └── index.html
├── requirements.json
├── resources
│   └── views
│       ├── app.cre
│       ├── auth
│       │   ├── login.cre
│       │   └── register.cre
│       ├── components
│       │   └── alert.cre
│       ├── dashboard.cre
│       ├── includes
│       │   ├── debug.cre
│       │   ├── footer.cre
│       │   └── header.cre
│       └── pages
│           ├── main.cre
│           └── test
│               ├── create.cre
│               ├── edit.cre
│               ├── index.cre
│               └── view.cre
├── routes
│   ├── app.py
│   ├── auth.py
│   └── route.py
└── storage
    ├── backups
    │   ├── backup_20250125_095936.zip
    │   ├── backup_20250203_105328.zip
    │   └── backup_20250210_101833.zip
    ├── sessions
    │   └── creator.json
    └── versions
        ├── creator_0.1.51-beta.zip
        ├── creator_0.1.55-beta.zip
        └── creator_1.0.0.zip
