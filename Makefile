up:
	uvicorn main:app --host 0.0.0.0 --port 8000 --reload

build-deps:
	pip install -t dependencies -r requirements.txt

run:
	celery -A videocombiner-backend worker --loglevel=info