streaming:
	python3 streaming.py

solving:
	python3 solving.py

training:
	python3 training.py

plot:
	jupyter notebook plots.ipynb

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

venv:
	python3 -m venv venv
	source venv/bin/activate

activate: # won't work apperantly
	source venv/bin/activate