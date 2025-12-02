# app.py
from fastapi import FastAPI, HTTPException, Query
from typing import List
from services.yt_dlp import parse_playlist
from models.track import Track

app = FastAPI(title="JAIX Python Service")

@app.get("/playlists/parse", response_model=List[Track])
def api_parse_playlist(url: str = Query(..., description="URL de la playlist a parsear")):
    try:
        return parse_playlist(url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
