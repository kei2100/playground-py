from aiohttp import web
import tempfile
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

font_configuration = FontConfiguration()


async def for_ab(request):
    # with tempfile.TemporaryFile(mode="wb+") as f:
    with tempfile.SpooledTemporaryFile(mode="wb+", max_size=65536) as f:
        html = HTML(filename="test.html")
        # html = HTML(filename="guide.html")
        html.write_pdf(target=f, font_config=font_configuration)
        f.seek(0)
        resp = web.StreamResponse(
            status=200,
            reason="OK",
            headers={"Content-Type": "application/pdf"},
        )
        await resp.prepare(request)
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            await resp.write(chunk)
        await resp.write_eof()
        return resp


app = web.Application()
app.add_routes([web.get("/for_ab", for_ab)])
web.run_app(app)
