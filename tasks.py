import shutil
from invoke import task
import os

@task
def activate_env(c):
    """=====> Activate the virtual environment."""
    venv_path = ".\\env\\Scripts\\activate"

    if not os.path.exists(venv_path):
        print("Virtual environment not found. Please create it first (e.g., 'python -m venv env').")
        return

    c.run(f"cmd /k {venv_path}")

@task
def start(c):
    """=====> Start the project (default port: 3000)."""
    c.run("uvicorn app.main:app --reload --port 3000")

@task
def start_port(c, port=3000):
    """=====> Start the project on a specific port (e.g., invoke start_port --port=3001)."""
    c.run(f"uvicorn app.main:app --reload --port {port}")

@task
def install(c):
    """=====> Install dependencies from requirements.txt."""
    c.run("pip install -r requirements.txt")

@task
def test(c):
    """=====> Run tests using pytest."""
    c.run("pytest --cov=app --cov-branch --cov-fail-under=90")
    
@task
def test_coverage(c):
    """=====> Run tests using pytest with html coverag report."""
    c.run("pytest --cov=app --cov-report=html")
    
    
@task
def package(c):
    """Package the project code into a .zip file."""
    project_dir = os.getcwd()  # Obtén el directorio actual del proyecto
    zip_filename = "project.zip"  # Nombre del archivo .zip de salida

    # Elimina cualquier archivo zip existente
    if os.path.exists(zip_filename):
        os.remove(zip_filename)

    # Empaquetar el proyecto en un archivo .zip
    shutil.make_archive(zip_filename.replace(".zip", ""), 'zip', project_dir)

    print(f"Project has been packaged into {zip_filename}")   

@task
def options(c):
    """=====> List all available tasks."""
    c.run("invoke --list")
