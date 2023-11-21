up:
	uvicorn main:app --host 0.0.0.0 --port 80 --reload

build-deps:
	pip install -t dependencies -r requirements.txt

build-zip-deps:
	(cd dependencies; zip ../aws_lambda_artifact.zip -r .) 
