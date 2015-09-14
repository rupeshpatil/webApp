# README #
	
	Note :- This Setup is for ubuntu(linux) (Similar command you can use for other OS)

## Setting up your workspace ##

### 1) Getting the source code ###
	
	Download code from https://github.com/rupeshpatil/webApp
	
### 2) Setting up the environment ###

	To setup virtual environment, We have to install some additional software.
	Install virtualenv, virtualenvwrapper

	- sudo apt-get install python-setuptools python-dev build-essential

	- sudo easy_install pip

	- sudo pip install virtualenv virtualenvwrapper

	- mkdir ~/.virtualenvs

	- mkdir ~/.pip_download_cache


	Add following lines in your ~/.bashrc file (Optional)
	- If not exists then you can create .bashrc file

	export WORKON_HOME=$HOME/.virtualenvs

	source /usr/local/bin/virtualenvwrapper.sh

	export PIP_VIRTUALENV_BASE=$WORKON_HOME

	export PIP_DOWNLOAD_CACHE=$HOME/.pip_download_cache

	export PIP_RESPECT_VIRTUALENV=true
	
	_Make sure you have installed libmysqlclient-dev package on ubuntu

Setup your environment and activate it
	
	mkvirtualenv projectname --no-site-packages

	workon projectname

Install requirements.txt via pip
	
	pip install -r requirements.txt


### 3) Running the development server ###
		
	python app.py


### 4)  ###

1. Get current directory filenames
	- http://127.0.0.1:5000/filename
2. Login Url 	
	- http://127.0.0.1:5000/login
