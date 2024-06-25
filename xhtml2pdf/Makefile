fmt:
	black --exclude .venv/ .

lint:
	flake8 --exclude .venv/ .

run:
	uvicorn main:app --port 8001

run.dev:
	uvicorn main:app --reload --port 8001
