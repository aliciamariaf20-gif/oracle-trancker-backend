from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Libera acesso do frontend (V0 / Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Oracle Tracker backend is running"}

@app.post("/analyze")
def analyze_video(data: dict):
    """
    Aqui no futuro entra:
    - Optical Flow
    - Kalman Filter
    - Tracking X/Y
    """
    return {
        "correct_chest": "middle",
        "confidence": 0.92
    }
