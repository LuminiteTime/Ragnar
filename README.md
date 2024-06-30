# Ragnar Setup Guide

Welcome to Ragnar v.0! This guide will walk you through cloning the repository and starting the application using Docker.

### **Features**:
- Bind Ollama so it is not needed to be downloaded separately
- Removed authentication with safety about all dependencies
- Changed logo and name
- Removed unnecessary functionality and options from "Settings"
- Removed admin and users system since the app is used locally

### **Fixed**:
- Build using Docker is now stable

## How to easily run:

1. Unzip release files
2. Ensure you have Docker installed and running on your machine
3. Open terminal
4. In terminal type:

    4.1.
    ```sh
    cd <path-to-release-folder>
    ```
    4.2.
    ```sh
    docker compose up -d
    ```
5. Go to http://localhost:3000
6. Wait a little bit, it may take some time to start the app (Around 5 minutes, you can track the progress in Ragnar container in docker, if there are lines 

" Loading WEBUI_SECRET_KEY from file, not provided as an environment variable.

Generating WEBUI_SECRET_KEY

Loading WEBUI_SECRET_KEY from .webui_secret_key "

then the app is starting normally)

7. When the logo of Ragnar appears on the page, the app is running


Congratulations! You have successfully started Ragnar. 