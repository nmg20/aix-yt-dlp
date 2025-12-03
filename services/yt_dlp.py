from typing import List
from yt_dlp import YoutubeDL # type: ignore
from models.track import Track

ydl_opts = {
    "extract_flat": True,
    "quiet": True,
    "ignoreerrors": True,
    "skip_download": True,
}

def parse_playlist(list_id: str):
    """
    Recibimos el id de la playlist en lugar de la url completa.
    -> evitar errores de codificacion de la url
    TODO: - división y gestión de ids en base a videos o listas.
    """
    url = f"https://www.youtube.com/playlist?list={list_id}"

    with YoutubeDL(ydl_opts) as ydl:  # type: ignore
        info = ydl.extract_info(url, download=False)

    tracks = []

    for e in info.get("entries", []):
        track = Track(
            title=e.get("title"),
            artist=e.get("artist"),
            album=e.get("album"),
            duration=e.get("duration"),
            url=e.get("url"),
            path="",
        )  # type: ignore
        tracks.append(track)
    return tracks