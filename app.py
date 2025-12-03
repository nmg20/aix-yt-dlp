from fastapi import FastAPI, HTTPException, Query # type: ignore
from typing import List
from services.yt_dlp import parse_playlist
from models.track import Track

app = FastAPI(title="AIX Python Service")

@app.get("/playlists/parse", response_model=List[Track])
def api_parse_playlist(
    id: str = Query(..., description="ID de la playlist de YouTube")
):
    try:
        return parse_playlist(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
