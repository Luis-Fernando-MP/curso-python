"""
  -> Mujer: es-ES-ElviraNeural
  -> es-ES-AlvaroNeural

  -> Argentina
    Mujer: es-AR-ElenaNeural
    Hombre: es-AR-TomasNeural

  -> Chile
    Mujer: es-CL-CatalinaNeural
    Hombre: el mejor: es-CL-LorenzoNeural
  
  -> Colombia
    Mujer: es-CO-SalomeNeural
    Hombre: es-CO-GonzaloNeural

  -> Peru
    Mujer: es-PE-CamilaNeural
    Hombre: es-PE-AlexNeural
  
  -> Venezuela
    Mujer: es-VE-PaolaNeural
    Hombre: es-VE-SebastianNeural

  -> Panama
    Mujer: es-PA-MargaritaNeural
    Hombre: es-PA-RobertoNeural

  -> Costa Rica
    Mujer: es-CR-MariaNeural
    Hombre: es-CR-JuanNeural	

"""
import asyncio
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from edge_tts import Communicate

app = FastAPI()

@app.get("/tts")
async def tts_endpoint(text: str = Query(..., min_length=1)):
    output_path = "voz.mp3"
    tts = Communicate(text=text, voice="es-PE-CamilaNeural")
    await tts.save(output_path)
    return FileResponse(output_path, media_type="audio/mpeg", filename="voz.mp3")

@app.get("/")
def hello():
    return {"msg": "Hola, usa /tts?text=Tu texto para obtener el mp3"}
