parsing:
	jupyter notebook

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

venv:
	python3 -m venv venv
	source venv/bin/activate