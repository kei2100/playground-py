Convert HTML to PDF server using xhtml2pdf

```bash
make run
curl -X POST -F "html=@test.html" http://localhost:8001/convert -o output.pdf && open output.pdf
```

## Installation

```bash
pip install -r requirements.txt
```

## Development

```bash
make fmt
make lint
make run
make run.dev
```