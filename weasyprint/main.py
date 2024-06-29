import asyncio
import concurrent.futures
import os
import tempfile
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
from starlette.background import BackgroundTask

app = FastAPI()
executor = concurrent.futures.ProcessPoolExecutor()
font_configuration = FontConfiguration()


@app.on_event("shutdown")
def shutdown_event():
    executor.shutdown()


@app.post("/files")
def upload_files(files: list[UploadFile]):
    """
    curl -X POST http://127.0.0.1:8000/files -F "files=@memo.md" -F "files=@image.jpg"
    {"filenames":["memo.md","image.jpg"]}
    """
    return {"filenames": [file.filename for file in files]}


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


def render_pdf():
    with tempfile.NamedTemporaryFile(mode="wb+", delete=False) as f:
        html = HTML(filename="guide.html")
        # html = HTML(filename="test.html")
        html.write_pdf(target=f, font_config=font_configuration)
        f.close()
        return f.name


@app.get("/for_ab")
async def for_ab():
    loop = asyncio.get_event_loop()
    filename = await loop.run_in_executor(executor, render_pdf)
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     filename = await loop.run_in_executor(pool, render_pdf)

    return FileResponse(
        filename,
        media_type="application/pdf",
        background=BackgroundTask(lambda: os.remove(filename)),
    )

# @app.get("/for_ab")
# async def for_ab():
#     with tempfile.NamedTemporaryFile(mode="wb+", delete=False) as f:
#         html = HTML(filename="test.html")
#         html.write_pdf(target=f, font_config=font_configuration)
#         f.close()
#         return FileResponse(
#             f.name,
#             media_type="application/pdf",
#             background=BackgroundTask(lambda: os.remove(f.name)),
#         )
