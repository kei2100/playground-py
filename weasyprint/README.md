Convert HTML to PDF server using WeasyPrint

```bash
make run
curl -X POST -F "html=@test.html" http://localhost:8000/convert -o output.pdf && open output.pdf
```

## Installation

```bash
brew install gtk+4 pkg-config
pyenv install
pip install -r requirements-dev.txt
```

## Development

```bash
make fmt
make lint
make run
make run.dev
```