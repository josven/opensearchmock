OPENSEARCHMOCK_VERSION='1.0.0'

install:
	pip3 install -r requirements.txt

test_install: install
	pip3 install -r requirements_test.txt

test: test_install
	python3.9 setup.py test

upload: create_dist
	pip3 install twine
	twine upload dist/*
	git push

create_dist: create_dist_no_commit update_pip
	rm -rf dist
	python3.9 setup.py sdist

create_dist_no_commit: update_pip
	rm -rf dist
	python3.9 setup.py sdist

create_dist_commit:
	git commit --all -m "Bump version ${OPENSEARCHMOCK_VERSION}"
	git tag ${OPENSEARCHMOCK_VERSION}

update_pip:
	pip3 install --upgrade pip
