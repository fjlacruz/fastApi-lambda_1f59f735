# FastApi Project
This project uses **FastAPI** to create a fast and efficient API. Follow the instructions to set up and run the project.
https://fastapi.tiangolo.com/




### 1. Requirements

- Python 3.8 or higher
- Recommended virtual environment (`venv`)
- Dependencies listed in `requirements.txt`


### 1. Create virtual env

```bash
pip install virtualenv
python -m venv env (env environment name)
.\env\Scripts\activate    (activate env in a power Shell)
pip list (list all dependencies)
pip freeze > requirements.txt   (save all dependencies )
pip install -r requirements.txt  (install all dependencies)

```


### 2. project command
```bash
invoke options
```


### 3. start project

```bash
invoke start

```

### 4. Documentation

```bash
http://localhost:8000/docs

```


### 5. Project structure
my_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── item.py
│   │   └── user.py
│   └── schemas/
│       ├── __init__.py
│       ├── item.py
│       └── user.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_items.py
│   └── test_users.py
├── requirements.txt
├── .gitignore
└── README.md


