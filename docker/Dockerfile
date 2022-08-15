FROM python:3.8-slim-buster

# set work directory
WORKDIR /app

# Copy project
COPY . .

# Install project dependencies 
RUN python -m pip install --no-cache-dir --upgrade pip \
  && python -m pip install --no-cache-dir -U poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev \
  && pip uninstall --yes poetry

CMD ["python", "scheduler.py"]
