from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
from api.schemas import PredictResponse, PredictRequest
from core.classifier import Classifier
from core.preprocessor import Preprocessor


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Loading classifier...")
    app.state.classifier = Classifier()
    app.state.preprocessor = Preprocessor()
    yield
    print("Shutting down classifier...")
    app.state.classifier = None
    app.state.preprocessor = None

app = FastAPI(
    title="CryptoGuard",
    description="Social Engineering Classifier",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://chrome/my_extension',
        'http://localhost:3000'
    ],
    allow_methods=['GET', 'POST'],
    allow_headers=['Content-Type']
)
@app.get('/health')
def health():
    return{
        "status":"healthy",
        "model_loaded":app.state.classifier is not None
    }

@app.post('/api/v1/predict', response_model=PredictResponse)
async def predict(payload:PredictRequest):
    if payload is None:
        return ""

    cleaned_text = app.state.preprocessor.clean_text(payload.text)
    if not cleaned_text:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid input"
        )

    result = await run_in_threadpool(app.state.classifier.predict,cleaned_text)

    return PredictResponse(**result)