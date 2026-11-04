
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.investigation import router as api_investigation_router

app = FastAPI(
    title="ECHO Backend API",
    description="Backend for the ECHO CyberSecurity Investigation Platform & Vulnerable Lab Analysis Engine",
    version="0.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://echo-cyber-security.vercel.app",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_investigation_router)


@app.get("/health")
def health_check():
    return {
        "status": "online",
        "service": "echo-backend",
        "message": "ECHO backend operational & lab ready"
    }


@app.post("/investigation/demo")
def legacy_demo():
    from app.api.investigation import run_demo_investigation
    return run_demo_investigation()


@app.post("/investigation/analyze")
def legacy_analyze():
    from app.services.pipeline import run_investigation_pipeline
    return run_investigation_pipeline(custom_events=[])


@app.get("/")
def read_root():
    return {
        "message": "ECHO API is running. Access /docs for API documentation."
    }
