# Bicycle Factory

## Overview

This repo contain standart [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/ "virtualenvwrapper") hooks with custom shall scripts in following files:

* `premkvirtualenv`
* `postmkvirtualenv`
* `prermvirtualenv`

Also, it contain custom templates for setting up:

* [nginx and uWSGI](https://uwsgi.readthedocs.org/en/latest/tutorials/Django_and_nginx.html "nginx and uWSGI")
* [Twitter Bootstrap](http://getbootstrap.com/ "Twitter Bootstrap") integration
* robots.txt
* redis db index generation
* and so on...

It contain [Django project template](https://docs.djangoproject.com/en/1.6/ref/django-admin/#startproject-projectname-destination "Django project template"), made [by example](https://github.com/django/django/tree/master/django/conf/project_template/ "by example").

So, if you made virtual env using mkvirtualenv alias, be sure you have setting up [NGINX(as proxy) and uWSGI(Emperor mode)](https://uwsgi.readthedocs.org/en/latest/tutorials/Django_and_nginx.html "NGINX(as proxy) and uWSGI(Emperor mode)")(just in case, read the manual) config files, ready to runserver Django project (I use [Werkzeug](http://werkzeug.pocoo.org/ "Werkzeug"), so you can use runserver_plus managment command) with home view, Twitter Bootstrap markup(base.html, home.html) and Less styles(bootstrap.less, variables.less, my_main.less, my_mixins.less...).

## Catalogs Tree:

You should creat the following, for works properly:

    / - root dir
    └── webapps/ - web applications dir
        ├── envs/ - virtual envs dir
        ├── server/ - nginx and uWSGI cofig files dir
        └── django/ - Django projects dir
            ├── internal/ - description comes below
            ├── static/ - Django static files
            └── media/ - Django users loaded files

execute following commands:

    sudo mkdir -p /webapps/envs /webapps/server
    sudo mkdir -p /webapps/django/internal /webapps/django/static /webapps/django/media 

Internal - read the doc: [Nginx internal](http://nginx.org/en/docs/http/ngx_http_core_module.html#internal "Nginx internal")([RU](http://nginx.org/ru/docs/http/ngx_http_core_module.html#internal "RU"))

Do not forget to set permissions:
    
    sudo chown -R $USER:www-data /webapps

## Install First!

On virgine Ubuntu Linux Server v14.04 LTS you should install following packeges:

0. Update and upgrade Ubuntu:
        
        sudo apt-get update; sudo apt-get upgrade -y

1. git, python2.7-dev and pip:

        sudo apt-get install git -y
        sudo apt-get install python2.7-dev -y
        sudo apt-get install python-pip -y
        sudo pip install --upgrade pip

2. virtualenv, virtualenvwrapper and bicycle-factory:

        sudo pip install virtualenv
        sudo pip install virtualenvwrapper
        export WORKON_HOME=/webapps/envs
        git clone https://github.com/titovanton-com/bicycle-factory.git $WORKON_HOME
        sudo chown -R $USER:www-data $WORKON_HOME
        source /usr/local/bin/virtualenvwrapper.sh
        echo "export WORKON_HOME=$WORKON_HOME" >> ~/.bashrc
        echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

3. nginx and uWSGI:

        sudo apt-get install nginx -y
        sudo pip install uwsgi

3. setting up uWSGI in Emperor mode:
        
        sudo mkdir -p /var/log/uwsgi
        sudo mkdir -p /etc/uwsgi/vassals
        sudo chown -R $USER:www-data /var/log/uwsgi
        sudo chmod -R 774 /var/log/uwsgi
        cp /webapps/envs/templates/uwsgi_params /webapps/server/
        sudo nano /etc/rc.local

    then add the folowing line before `exite 0`:

        /usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/log/uwsgi/mylog.log


4. PostgreSQL, python bindings and so on:

        sudo apt-get install curl build-essential openssl libssl-dev python-psycopg2 -y
        sudo apt-get install postgresql postgresql-client -y
        sudo apt-get install postgresql-server-dev-9.3 -y

5. Set password for postgres user (like root in MySQL):

        sudo -u postgres psql postgres

    and launch the command:

        \password postgres

    you will see password request (twice) - give it to him and then quit:

        \q

    Following to:

        sudo nano /etc/postgresql/9.3/main/pg_hba.conf 

    make sure to add it right after the "Put your actual configuration here" comment block! Otherwise one of the default entries might catch first and the databse authentication will fail.
        
        local   all             all                                     password

    Now you can login using psql client without specifying `-h localhost`:
        
        psql -U <user> <db>

## Optional

I also use following apps to serve needs of my websites:

1. [Redis](http://redis.io/ "Redis"):

        sudo apt-get install redis-server -y

    if you want change some settings, make a backup first:

        sudo cp /etc/redis/redis.conf /etc/redis/redis.conf.default

    for example, if you want to set password:

        sudo sed -e "s;# requirepass foobared;requirepass <password>;g" \
                 -i /etc/redis/redis.conf

2. [ElasticSearch](http://www.elasticsearch.org/ "ElasticSearch"):

        sudo apt-get install openjdk-7-jre-headless -y
        mkdir -p $HOME/src
        cd $HOME/src
        # v1.1.1 works fine for me:
        wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.1.1.deb
        sudo dpkg -i elasticsearch-1.1.1.deb
        # enable russian morphology support
        sudo /usr/share/elasticsearch/bin/plugin -install analysis-morphology -url http://dl.bintray.com/content/imotov/elasticsearch-plugins/org/elasticsearch/elasticsearch-analysis-morphology/1.2.0/elasticsearch-analysis-morphology-1.2.0.zip
        sudo update-rc.d elasticsearch defaults 95 10

3. Image librarie(if Pillow does not enough):

        sudo apt-get install imagemagick -y

4. Less:

        sudo apt-get install node-less -y

## Reboot

Reboot Ubuntu to lunch uWSGI, ElasticSearch, reload PostgreSQL and checkout virtualenvwrapper works fine:
    
    sudo reboot

## License
- Apache License, Version 2.0
- Download, install and use it where ever you want with my blessing =)
- PS: do not forget to give me a star!