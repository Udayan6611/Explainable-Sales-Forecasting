# Start with an official, lightweight Python 3.11 image.
FROM python:3.11-slim

# --- NEW LINE ---
# Install system dependencies required by LightGBM.
RUN apt-get update && apt-get install -y libgomp1

# Set the working directory inside the container to /app.
WORKDIR /app

# Copy the requirements file into the container at /app.
COPY requirements.txt .

# Upgrade pip to the latest version.
RUN pip install --upgrade pip


# Install the Python dependencies listed in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's code (app.py, model files, etc.) into the container.
COPY . .

# The command to run when the container starts.
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]