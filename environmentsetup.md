#  Setting up the environment #

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


-- if mkvirtualenv command is not working then shoot below command then use mkvirtualenv command
-- source ~/.bashrc

# Setup Git#

_First install Git 
	
	sudo apt-get install git

_Intialise git in your workspace using following command
	
	git init

_Set your name and email in git config for indentity.

	git config --global user.name "Xyz Abc"
	
	git config --global user.email "xyz@example.com"

_Git clone your project from github
	
	git clone git@github.com:xyz/projectname.git



1. Get current directory filenames
	- http://127.0.0.1:5000/filename
2. Login Url 	
	- http://127.0.0.1:5000/login
3. Get status of dependecies
	- http://127.0.0.1:5000/login
4. Get the all users
	- http://127.0.0.1:5000/users