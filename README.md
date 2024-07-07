# Ragnar Setup Guide

Welcome to Ragnar MVP-v2! This guide will walk you through cloning the repository and starting the application using Docker.

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
5. Go to http://localhost:5173 
6. Wait a little bit, it may take some time to start the app (Around 5 minutes, you can track the progress in Ragnar container in docker, if there are lines 

" Loading WEBUI_SECRET_KEY from file, not provided as an environment variable.

Generating WEBUI_SECRET_KEY

Loading WEBUI_SECRET_KEY from .webui_secret_key "

then the app is starting normally)

7. When the logo of Ragnar appears on the page, the app is running

## Important! Configure LLM:
To start chatting with LLM we recomend to use phi3:mini model, you can set it up by clicking arrow-down icon to the right of "Select a model" label in the top-left corner of the chat window. Then type ```phi3:mini``` and press "Pull phi3:mini from Ollama.com". For this step you will need Internet connection but when the model is downloaded the app does not need Internet connection.


Congratulations! You have successfully started Ragnar. 