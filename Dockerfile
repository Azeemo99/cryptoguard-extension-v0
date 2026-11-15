FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --default-timeout=1000 --extra-index-url https://download.pytorch.org/whl/cpu \
    -r requirements.txt

COPY core/config.py /app/core/config.py
COPY scripts/ app/scripts/

RUN --mount=type=secret,id=hf_token \
    HF_TOKEN=$(cat /run/secrets/hf_token) \
    python -m scripts.download_model

ENV HF_HUB_OFFLINE=1

COPY core/ app/core/
COPY api/ app/api/

EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "port", "8000"]