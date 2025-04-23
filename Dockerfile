FROM python:3.13-bookworm

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && apt-get clean

# Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV CARGO_HOME=/root/.cargo
ENV PATH=$CARGO_HOME/bin:$PATH

# Poetry installation
RUN pip install poetry \
    && poetry config virtualenvs.create false
ENV PATH="/root/.local/bin:$PATH"

# Poetry config
COPY pyproject.toml poetry.lock* ./
COPY app ./app
RUN poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000