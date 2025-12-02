from typing import List
from urllib.parse import parse_qs, urlparse
from yt_dlp import YoutubeDL
from models.track import Track

ydl_opts = {
    "extract_flat": True,
    "quiet": True,
    "ignoreerrors": True,
    "skip_download": True,
}

ydl_opts_download = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "quiet": False,
    "ignoreerrors": True,
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "320"
    }]
}

def normalize_url(url: str) -> str:
    """
    Separar url si es un vídeo o una lista de reproducción
    """
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    list_id = query.get("list")
    if list_id:
        return f"https://www.youtube.com/playlist?list={list_id[0]}"
    return url

def parse_playlist(url: str):
    with YoutubeDL(ydl_opts) as ydl: # type: ignore
        info = ydl.extract_info(normalize_url(url), download=False)
    tracks = []
    for e in info.get("entries", []):
        track = Track(
            title = e.get("title"),
            artist = e.get("artist"),
            album = e.get("album"),
            duration = e.get("duration"),
            url = e.get("url"),
        )
        tracks.append(track)
    return tracks

# def download_track(track_url: str, output_dir: str = './downloads'):
#     ydl_opts_download = {
#         'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
#         "format": "bestaudio/best",
#         "quiet": False,
#         "ignoreerrors": True,
#         "postprocessors": [{
#             "key": "FFmpegExtractAudio",
#             "preferredcodec": "mp3",
#             "preferredquality": "320"
#         }]
#     }
#     with YoutubeDL(ydl_opts_download) as ydl: # type: ignore
#         info = ydl.extract_info(track_url, download=True)
    
#     return Track(
#         title=info.get('title'), # type: ignore
#         artist=info.get('uploader'),
#         album=None,
#         duration=info.get('duration'),
#         url=track_url,
#     )