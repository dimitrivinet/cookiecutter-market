import sys
import venv
import time
import subprocess

SUCCESS = "\x1b[1;32m"
INFO = "\x1b[1;33m"
TERMINATOR = "\x1b[0m"

module_name = "{{ cookiecutter.repo_name }}"


def set_python_version():
    python_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)

    file_names = ["Dockerfile", ".github/workflows/test.yml"]
    for file_name in file_names:
        with open(file_name) as f:
            contents = f.read()
            contents = contents.replace(r"{python_version}", python_version)
        with open(file_name, "w") as f:
            f.write(contents)


def create_virtualenv():
    builder = venv.EnvBuilder(with_pip=True)
    builder.create("./.venv")


def install_dev_deps():
    subprocess.call(["./.venv/bin/pip3", "install", "-r", "requirements.txt.dev"])


def main():
    set_python_version()
    print(SUCCESS + "Project successfully initialized" + TERMINATOR)
    time.sleep(0.5)

    create_virtualenv()
    print(SUCCESS + "Virtualenv created" + TERMINATOR)
    time.sleep(0.5)

    install_dev_deps()
    print(SUCCESS + "Installed development dependencies" + TERMINATOR)
    print(INFO + "To start your project, run: " + TERMINATOR)
    print(INFO + f"    cd {module_name} && source .venv/bin/activate" + TERMINATOR)
    print(INFO + f"    git init" + TERMINATOR)
    print(INFO + f"    pre-commit install -t pre-commit" + TERMINATOR)
    print(INFO + f"    pre-commit install -t pre-push" + TERMINATOR)
    time.sleep(0.5)

if __name__ == "__main__":
    main()
