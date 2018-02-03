all:
		@pip install virtualenv
		@mkdir bin
		@virtualenv bin --python=python2.7
		@pip install -r src/requirements.txt

test:
		@echo "Nothing to do"

run:
		@python src/app.py

clean:
		@rm -r bin/
		@rm src/error.log
