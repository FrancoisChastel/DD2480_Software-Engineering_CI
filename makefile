all:
		@pip install virtualenv
		@mkdir bin
		@virtualenv bin --python=python2.7
		@pip install -r src/requirements.txt

test:
		@python src/app.py --test

run:
		@python src/app.py --run

clean:
		@rm -r bin/
		@rm src/error.log
