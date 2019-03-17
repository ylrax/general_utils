## Ubuntu clean install


From a totally clean installation:

Install firefox:

Go to https://www.mozilla.org/es-ES/firefox/new/?utm_medium=referral&utm_source=support.mozilla.org

	tar xjf firefox-*.tar.bz2
	# inside the firefox folder:
	~/firefox/firefox

	# or:
	sudo apt-get update
	sudo apt-get install firefox

Java jdk:

	apt-get update && apt-get upgrade
	sudo apt install default-jdk

Pycharm: https://www.jetbrains.com/pycharm/download/#section=linux

	ashdñf .targz

	#or
	sudo apt-get install pycharm


Install skype: Download .deb from: https://www.skype.com/es/get-skype/skype-for-linux/

	sudodpkg -i <filename.deb>

Install Git

	sudo apt install git

Install python's update python 3 (if necesary)
	
	# example with python 3.6
	sudo add-apt-repository ppa:jonathonf/python-3.6
	sudo apt-get update
	sudo apt-get install python3.6

Now you have three Python versions, use python command for version 2.7, python3 for version 3.5, and/or python3.6 for version 3.6.1.

	python  -V
	python2 -V
	python3 -V
	python3.6 -V

To make python3 use the new installed python 3.6 instead of the default 3.5 release, run following 2 commands:

	sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
	sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

	sudo update-alternatives --config python3
	python3 -V

Note: you may find a bug and the console won't launch after step 2. You have to replace the simlink:

	sudo rm /usr/bin/python3
	sudo ln -s python3.5 /usr/bin/python3

Install virtualenvs

	sudo apt install virtualenvs

Install Kazam

	sudo apt install kazam

Create repos, venvs folder

	mkdir repos && cd ./repos
	mkdir venvs && cd ./venvs
	virtualenv <virtualenv_name>
	source <virtualenv_name>/bin/activate
	pip install...

write shortcuts

	gedit .bashrc
		alias <alias_name>=source <virtualenv_name_path>/bin/activate && cd <repo_path>

Double click minimization



Generate ssh key

Check if you have (you should not have anything):

	ll ~/.ssh

If not:

	ssh-keygen -t rsa -b 4096 -c "your_email"

	eval "$(ssh-agent -s)"
	ssh-add ~/.ssh/id_rsa
	vim ~/.ssh/id_rsa/id_rsa.pub
	# Copy it to the github


install spark: https://spark.apache.org/downloads.html

	sudo tar - .......
	pip install pyspark