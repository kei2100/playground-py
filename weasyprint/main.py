import os
import tempfile
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
from starlette.background import BackgroundTask

app = FastAPI()
# FontConfiguration() をマルチスレッド環境化で呼び出すと Segmentation fault が発生するため、
# ここでオブジェクトを作成しておく（ffi の影響？）
font_configuration = FontConfiguration()


@app.post("/convert")
def convert(html: UploadFile):
    with tempfile.NamedTemporaryFile(mode="wb+", delete=False) as f:
        html = HTML(file_obj=html.file)
        html.write_pdf(target=f, font_config=font_configuration)
        f.close()
        return FileResponse(
            f.name,
            media_type="application/pdf",
            background=BackgroundTask(lambda: os.remove(f.name)),
        )


@app.get("/for_ab")
def for_ab():
    with tempfile.NamedTemporaryFile(mode="wb+", delete=False) as f:
        html = HTML(filename="test.html")
        html.write_pdf(target=f, font_config=font_configuration)
        f.close()
        return FileResponse(
            f.name,
            media_type="application/pdf",
            background=BackgroundTask(lambda: os.remove(f.name)),
        )
