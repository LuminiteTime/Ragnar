# Ragnar Setup Guide

Welcome to Ragnar v.0! This guide will walk you through cloning the repository and starting the application using Docker.

## Ollama installation (manual for now)

First, you need to install Ollama. Visit the [Ollama download page](https://ollama.com/download) to get the latest version of the Ollama library. Follow the installation instructions for your operating system. Then run the app (no interface will appear).

## Cloning the Repository

Then, you need to clone the Ragnar repository to your local machine. You can do this using either HTTPS or SSH. Choose the method that suits you best:

- **HTTPS:**

```sh
git clone https://gitlab.pg.innopolis.university/m.trifonov/ragnar.git
```

- **SSH:**
```sh
git clone git@gitlab.pg.innopolis.university:m.trifonov/ragnar.git
```

After cloning, navigate into the project directory:
```sh
cd ragnar
```

## Starting the Application
Ensure you have Docker installed and running on your machine.

To start the application, run the following command in the terminal:
```sh
docker compose up -d
```

This command will start the application in detached mode, allowing you to continue using the terminal. The application will be running in Docker, and you can start using the application.

Congratulations! You have successfully cloned and started Ragnar. 

## Start the work

- When docker compose is done, go to "http://localhost:3000"
- It is possible that you will need to wait some time before the home page appears
- Click "Sign up", enter any name, email, and password you want, then press "Create Account".
- To start the chat with LLM you have to click "Selecta model" in the top-left corner of the chat window, then click arrow-down button and write "phi3:mini". Then press "Pull phi3:mini from Ollama.com" and wait until LLM is downloaded (you will need Internet connection for it). When LLM has been downloaded, you can start chatting with it (Internet connection is not needed).