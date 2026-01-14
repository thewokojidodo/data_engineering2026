# Dockerizing data pipeline with UV

FROM python:3.11.13-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY .python-version pyproject.toml uv.lock ./
RUN uv sync --locked

COPY ingest_data.py ./

ENTRYPOINT ["python", "ingest_data.py"]
