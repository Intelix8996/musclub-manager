FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /usr/local/musclub-manager-backend

# Install Poetry
RUN pip install poetry

# Copy dependencies file
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root --no-dev

# Copy backend code
COPY ./musclub_manager_backend ./musclub_manager_backend

# Install backend package
RUN poetry install --no-dev

# Expose port for HTTP
EXPOSE 8080

# Start backend
CMD ["poetry", "run", "fastapi", "run", "musclub_manager_backend/app.py", "--proxy-headers", "--port", "8080"]
