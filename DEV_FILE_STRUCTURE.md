│  (Dockerfile, Makefile, README.md + sh and js files)
│
├───backend (FastAPI to load html pages)
│   │
│   ├───apps (FastAPIs)
│   │   ├───audio
│   │   │
│   │   ├───images
│   │   │
│   │   ├───ollama
│   │   │
│   │   ├───openai
│   │   │
│   │   ├───rag
│   │   │   │
│   │   │   └───search
│   │   │       │
│   │   │       └───testdata
│   │   │
│   │   ├───socket
│   │   │
│   │   └───webui
│   │       │
│   │       ├───internal (Database interactions)
│   │       │   │
│   │       │   └───migrations
│   │       │
│   │       ├───models
│   │       │
│   │       └───routers (FASTAPI)
│   │
│   ├───data (Prompt suggestions json file and config file)
│   │
│   ├───open_webui (app = typer.Typer())
│   │
│   ├───static (FRONTEND)
│   │   │
│   │   └───fonts
│   │
│   └───utils
│
├───cypress (FRONTEND TypeScript files)
│
├───docs (Documentation)
│
├───kubernetes (NOT NEEDED)
│
├───scripts (FRONTEND js files)
│
├───src (FRONTEND)
│   │
│   ├───lib
│   │   │
│   │   ├───apis
│   │   │
│   │   ├───components (svelte files)
│   │   │
│   │   ├───i18n (languages translations)
│   │   │
│   │   └─── ... (TypeScript files)
│   │
│   └─── ... (Svelte files)
│
├───static (FRONTEND)
│
└───test (TEST)

Socket:
Manipulations with USER_POOL, SESSION_POOL and USAGE_POOL
USER_POOL - dictionary, where key - user id, value - array of session ids (sids)
SESSION_POOL - dictionary, where key - session id, value - user id
USAGE_POOL\[model_id]\["sids"]
USAGE_POOL\[model_id]\["callback"]

