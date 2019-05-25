.PHONY: all black flake8 test coverage coveralls dist clean

all:	black flake8 test coverage

test:
	py.test

coverage:
	coverage run --source openregister -m py.test && coverage report

coveralls:
	py.test --cov openregister tests/ --cov-report=term --cov-report=html

flake8:
	flake8 openregister tests

black:
	black openregister tests

dist:
	python3 setup.py sdist upload

init:
	pip install .[test]

clean:
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
	-rm -rf dist
	-rm -rf build
	-rm -rf openregister.egg-info
