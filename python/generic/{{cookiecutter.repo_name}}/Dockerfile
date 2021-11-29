FROM python:{python_version}-slim AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS python-deps

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


FROM base AS runtime

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY . .

# Run the executable
ENTRYPOINT ["python", "-m", "{{cookiecutter.repo_name}}"]
