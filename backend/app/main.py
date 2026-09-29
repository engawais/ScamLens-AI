from fastapi import FastAPI

app = FastAPI(
    title="ScamLens AI API",
    description="Multimodal scam detection and digital safety intelligence API.",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "project": "ScamLens AI",
        "status": "Phase 1 backend is running",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}
