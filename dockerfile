FROM python:3.13-slim
# Evita prompts interactivos
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \ PIP_NO_CACHE_DIR=1 \ PYTHONDONTWRITEBYTECODE=1 \ PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY  embeding.py .

EXPOSE 7860

CMD ["python", "embeding.py"]
