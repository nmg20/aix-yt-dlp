# aix-yt-dlp
Microservicio que se ocupa de gestionar conexión a YouTube usando la librería **yt-dlp**.

---

## Operaciones disponibles
- **Parse**. Recibe el *id* de la playlist de YouTube, construye la URL y hace la petición a *yt-dlp* para devolver los elementos procesados como **Track**s -> Endpoint: */playlists/parse*


## Operaciones futuras
- **Download**. Recibe el *id* de la playlist y la lista de Tracks conteniendo URLs (o URLs tal cual) y descarga la lista de tracks en base a sus URLs -> Endpoint: */playlists/download*
- Operaciones de gestión de playlists

## Operaciones internas
- Construcción unificada de URLs en base a *ids*
- Gestión interna eficiente de *playlists* y *tracks* en base a clases.
- Paralelización del proceso de recuperación de tracks y descarga.
- Tests
- Documentación

---

## Arranque del módulo
`cd .\aix-yt-dlp\`
`& C:/Users/nicog/Desktop/sw/aix-workspace/aix/.venv/Scripts/Activate.ps1`
`uvicorn app:app --reload --host 0.0.0.0 --port 8000`