# Use an official Node.js runtime as a parent image
FROM node:20-slim AS node-base

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json ./

# Install Node.js dependencies
RUN npm install --production

# Copy all project files
COPY . .

# --- Python dependencies ---
# Use an official Python runtime as a parent image
FROM python:3.12-slim AS python-base

# Set working directory
WORKDIR /app

# Copy only the Python scripts and requirements
COPY py/ ./py/

# Install Python dependencies
RUN pip install numpy gensim

# --- Final image ---
FROM node:20-slim

WORKDIR /app

# Copy Node.js app (from node-base)
COPY --from=node-base /app /app

# Copy Python environment (from python-base)
COPY --from=python-base /app/py /app/py

# Expose the port the app runs on
EXPOSE 3000

# Start the Node.js server
CMD ["npm", "start"]
