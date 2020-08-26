apt update
apt-get -y install python3-pip
apt-get -y install apache2
apt-get -y install libapache2-mod-wsgi-py3
pip3 install virtualenv
virtualenv environment
cd environment
source environment/bin/activate
pip3 install alembic==1.4.2 
pip3 install Flask==1.1.2 
pip3 install Flask-Migrate==2.5.3 
pip3 install Flask-SQLAlchemy==2.4.4 
pip3 install Jinja2==2.11.2 
pip3 install numpy==1.19.1 
pip3 install pandas==1.1.0 
pip3 install SQLAlchemy==1.3.18 
pip3 install sqlparse==0.3.1 
pip3 install uuid==1.30
pip3 install virtualenv==20.0.27 
pip3 install Werkzeug==1.0.1 
pip3 install waitress 

