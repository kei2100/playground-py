import os
import tempfile
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from xhtml2pdf import pisa
from starlette.background import BackgroundTask

app = FastAPI()

@app.post("/convert")
def convert(html: UploadFile):
    with tempfile.NamedTemporaryFile(mode="wb+", delete=False) as f:
        pisa.CreatePDF(html.file, dest=f)
        f.close()
        return FileResponse(
            f.name,
            media_type="application/pdf",
            background=BackgroundTask(lambda: os.remove(f.name)),
        )

@app.get("/for_ab")
def for_ab():
    with open("test.html", "rb") as hf:
        with tempfile.NamedTemporaryFile(mode="wb+", delete=False) as f:
            pisa.CreatePDF(hf, dest=f)
            f.close()
            return FileResponse(
                f.name,
                media_type="application/pdf",
                background=BackgroundTask(lambda: os.remove(f.name)),
            )