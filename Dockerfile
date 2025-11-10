FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget gnupg unzip curl fonts-liberation \
    libnss3 libxi6 libgbm1 libasound2 \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENV HEADLESS=true
ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
