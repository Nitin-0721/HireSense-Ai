import threading
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ats import router as ats_router
from routes.upload import router as upload_router
from routes.chat import router as chat_router


@asynccontextmanager
async def lifespan(app):
    # Warm up the embedding model in the background so the
    # server starts instantly and the first upload is fast
    from utils import get_model
    threading.Thread(target=get_model, daemon=True).start()
    yield


app = FastAPI(
    title="HireSense AI",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(ats_router)


@app.get("/")
def home():
    return {
        "message": "HireSense AI Running 🚀"
    }