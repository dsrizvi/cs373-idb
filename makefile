FILES :=                              \
    .travis.yml                       \
    .gitignore                        \
    makefile                          \
    apiary.apib                       \
    model.html                        \
    models.py                         \
    IDB1.log                          \
    UML.pdf                           \
    tests.py

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

config:
	git config -l

scrub:
	make clean
	rm -f  model.html
	rm -f  IDB1.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: tests.py
    python3 tests.py

model.html: models.py
	pydoc3 -w models

IDB1.log:
	git log > IDB1.log
