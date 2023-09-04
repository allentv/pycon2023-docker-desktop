format:
	isort src/
	black src/
	# mypy src/


start:
	python src/app.py
