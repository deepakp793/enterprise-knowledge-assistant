from fastapi import FastAPI

from enterprise_knowledge_assistant.api.routes.health import router as health_router


def create_app() -> FastAPI:
    application = FastAPI(title="Enterprise Knowledge Assistant", version="0.1.0")
    application.include_router(health_router)

    return application


app = create_app()
