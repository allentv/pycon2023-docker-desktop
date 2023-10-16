format:
	isort src/
	black src/
	# mypy src/

start:
	python3 src/screen.py
