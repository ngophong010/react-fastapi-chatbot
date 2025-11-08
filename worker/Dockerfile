# Stage 1: Build dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM python:3.11-slim AS production

WORKDIR /app

# Create non-root user first
RUN useradd --create-home --shell /bin/bash --uid 1002 worker

# Copy installed packages to worker user location
COPY --from=builder /root/.local /home/worker/.local

# Copy application code
COPY . .

# Fix ownership
RUN chown -R worker:worker /app /home/worker/.local

# Switch to non-root user
USER worker

# Add local packages to PATH
ENV PATH=/home/worker/.local/bin:$PATH

CMD ["python", "main.py"]