# Update this to give whichever name you want. This may be set on the command line:
# > make build OUT_FILE=../outfile.zip
OUT_FILE?=../deliverable.zip

### Below this point it should not need to be changed
# get absolute path of zipfile to deliver
DELIVERABLE=$(abspath $(OUT_FILE))

# Rebuild the delivrable
build:
	$(eval VENV = $(shell pipenv --venv))
	cd ${VENV}/lib/python3.7/site-packages && zip -r9 ${DELIVERABLE} ./*
	zip -r9 ${DELIVERABLE} *.py
