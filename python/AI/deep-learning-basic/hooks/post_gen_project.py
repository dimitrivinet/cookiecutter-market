import sys
import venv
import time
import subprocess

SUCCESS = "\x1b[1;32m"
INFO = "\x1b[1;33m"
TERMINATOR = "\x1b[0m"

project_slug = "{{ cookiecutter.project_slug }}"


def create_virtualenv():
    builder = venv.EnvBuilder(with_pip=True)
    builder.create("./.venv")


def install_dev_deps():
    subprocess.call(["./.venv/bin/pip3", "install", "-r", "requirements_dev.txt"])


def install_deps():
    subprocess.call(["./.venv/bin/pip3", "install", "-r", "requirements.txt"])


def main():
    create_virtualenv()
    print(SUCCESS + "Virtualenv created" + TERMINATOR)
    time.sleep(0.5)

    install_dev_deps()
    print(SUCCESS + "Installed development dependencies" + TERMINATOR)
    install_deps()
    print(SUCCESS + "Installed running dependencies" + TERMINATOR)
    
    print(INFO + "To start your project, run: " + TERMINATOR)
    print(INFO + f"    cd {project_slug} && source .venv/bin/activate" + TERMINATOR)
    print(INFO + f"    git init" + TERMINATOR)
    print(INFO + f"    pre-commit install -t pre-commit" + TERMINATOR)
    print(INFO + f"    pre-commit install -t pre-push" + TERMINATOR)
    print()
    print(INFO + f"Finally, install PyTorch according to your system specs here: https://pytorch.org/get-started/locally/" + TERMINATOR)
    time.sleep(0.5)

if __name__ == "__main__":
    main()
