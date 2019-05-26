.PHONY: all black flake8 test coverage coveralls bump dist upload clean

all:	black flake8 test coverage

test:
	py.test

coverage:
	coverage run --source openregister -m py.test && coverage report

coveralls:
	py.test --cov openregister tests/ --cov-report=term --cov-report=html

flake8:
	flake8 .

black:
	black .

bump:
	git tag $(shell python version.py)

dist:
	python setup.py sdist bdist_wheel

upload:	dist
	twine upload dist/*

# install dependencies
init:
	pip install .[test]

clean:
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
	-rm -rf dist
	-rm -rf build
	-rm -rf openregister.egg-info
