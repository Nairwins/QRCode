from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import qrcode
import io

app = FastAPI()

@app.get("/")
def home():
    return {"message": "QR Code API is running"}

@app.get("/generate")
def generate_qr(text: str):
    qr = qrcode.make(text)
    
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    
    return StreamingResponse(buffer, media_type="image/png")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

