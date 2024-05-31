parsing:
	jupyter notebook parsing.ipynb

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

venv:
	python3 -m venv venv
	source venv/bin/activate

activate: # won't work
	source venv/bin/activate