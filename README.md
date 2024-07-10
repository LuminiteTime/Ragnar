
<a id="readme-top"></a>
<br />

<div>
    <div align="center">
        <p>
            <img src="image/logo.png" alt="logo">
            <h1>Ragnar</h1>
            An open source solution for conducting research and managing  notes with the help of RAG models
        </p>
    </div>
</div>

<details>
    <summary>Table of content</summary>
    <ol>
        <li> <a href="#about-ragnar">About Ragnar</a> </li>
        <ul>
            <li> <a href="#features">Features</a> </li>
            <li> <a href="#build-with">Build with</a> </li>
        </ul>
        <li> <a href="#ragnar-setup-guide">Ragnar Setup Guide </a></li>
        <ul>
            <li> <a href="#how-to-easily-run">How to easily run</a> </li>
            <li> <a href="#important-configure-llm"> Important configure llm</a></li>
        </ul>
        <li>
            <a href="#usage">Usage</a>
            <ul>
                <li> <a href="#important-configure-llm">Important configure LLM</a> </li>
            </ul>
        </li>
        <li>
            <a href="#contacts">Contacts</a>
        </li>
    </ol>
</details>

# About Ragnar

<!-- [![Contributors][contributors-shield]][contributors-url] -->
<!-- [![Forks][forks-shield]][forks-url] -->
<!-- [![Stargazers][stars-shield]][stars-url] -->
<!-- [![Issues][issues-shield]][issues-url] -->
<!-- [![MIT License][license-shield]][license-url] -->

Project Ragnar is an innovative open-source tool designed to address the growing need for efficient and accurate document summarization and information retrieval. In an era where information overload is a common challenge, Ragnar stands out by providing users with concise summaries of documents and enabling them to query large language models (LLMs) about the content, ensuring responses are grounded solely in the uploaded documents. This unique feature mitigates the risk of hallucinations, a common issue with LLMs that generate responses not based on the provided data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

1.	**Document Summarization:** \
At the heart of Project Ragnar is its ability to generate brief, coherent summaries of documents. This feature is particularly beneficial for users dealing with extensive texts, allowing them to quickly grasp the main points without wading through pages of content. By employing advanced natural language processing (NLP) techniques, Ragnar extracts key information and presents it in a digestible format, saving time and enhancing productivity.

2.	**Accurate Information Retrieval:** \
Unlike conventional LLMs that can produce responses based on a mix of learned data and the current input, Ragnar ensures that all responses are derived strictly from the uploaded documents. This is achieved by restricting the model’s access to external data sources, thereby eliminating the potential for misinformation or fabricated answers. Users can confidently query the content, knowing that the answers provided are accurate reflections of the original documents.
3.	**Open-Source Accessibility:** \
As an open-source project, Ragnar invites collaboration and innovation from the global developer community. This openness not only fosters a collaborative environment for continuous improvement but also ensures transparency and trust in the tool’s functionality. Users and developers alike can contribute to and benefit from the collective expertise of the community, enhancing the tool’s capabilities and reliability.
4.	**User-Friendly Interface:** \
Project Ragnar is designed with user experience in mind. Its intuitive interface allows users to easily upload documents, request summaries, and ask questions. The straightforward design ensures that even those with limited technical expertise can utilize the tool effectively, democratizing access to advanced document processing capabilities.

## Build with

[![Svelte][Svelte.dev]][Svelte-url]
[![Python][Python]][Python-url]
[![TypeScript][TypeScript]][TypeScript-url]
[![Shell][Shell]][Shell-url]
[![Css][Css]][Css-url]
[![Docker][Docker]][Docker-url]

# Ragnar Setup Guide

Welcome to Ragnar MVP-v2! This guide will walk you through cloning the repository and starting the application using Docker.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How to easily run:

### Without Olama app

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

### With Ollama app

1. Download [Ollama](https://ollama.com) from official site 
2. Run in terminal command to download LLM:
    ``` sh
    ollama run NAME_OF_THE_MODEL
    ```
    in our case:
    ``` sh
    ollama run phi3:mini
    ```
3. Ensure you have Docker installed and running on your machine
4. When instalation will be succesfully ended run next command in terminal
   ```sh
   docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v ragnar:/app/backend/data --name ragnar --restart always brainpumpkin/ragnar:latest
   ```
5. Enjoy using ragnar
6. For next runnnings you will need run ollama ([step 2](#with-ollama-app)) and run docker container ([step 4](#with-ollama-app))

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

### Important! Configure LLM:
To start chatting with LLM we recomend to use phi3:mini model, you can set it up by clicking arrow-down icon to the right of "Select a model" label in the top-left corner of the chat window. Then type ```phi3:mini``` and press "Pull phi3:mini from Ollama.com". For this step you will need Internet connection but when the model is downloaded the app does not need Internet connection.


Congratulations! You have successfully started Ragnar. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Contacts

Mikhail Trifonov – Backend Developer: [GitLab](https://gitlab.pg.innopolis.university/m.trifonov), [Email](m.trifonov@innopolis.university) \
Artyom Grishin – ML-engineer: [GitLab](https://gitlab.pg.innopolis.university/ar.grishin), [Email](ar.grishin@innopolis.university) \
Savva Ponomarev – DevOps-engineer: [GitLab](https://gitlab.pg.innopolis.university/s.ponomarev), [Email](s.ponomarev@innopolis.university) \
Ilsaf Abdulkhakov – Frontend Web Developer, UX/UI Designer: [GitLab](https://gitlab.pg.innopolis.university/i.abdulkhakov), [Email](i.abdulkhakov@innopolis.university) \
Azalia Alisheva – Backend Developer: [GitLab](https://gitlab.pg.innopolis.university/a.alisheva), [Email](a.alisheva@innopolis.university)




Project Link: [Ragnar](https://gitlab.pg.innopolis.university/m.trifonov/ragnar/-/tree/main?ref_type=heads)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org

[TypeScript]: https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white
[TypeScript-url]: https://www.typescriptlang.org

[Shell]: https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white
[Shell-url]: https://www.powershellgallery.com

[Css]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[Css-url]: https://www.w3.org/Style/CSS/Overview.en.html

[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
<!-- [contributors-url] -->
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/gitlab/issues-raw/gitlab.pg.innopolis.university/m.trifonov/ragnar
[issues-url]: https://gitlab.pg.innopolis.university/m.trifonov/ragnar/-/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
