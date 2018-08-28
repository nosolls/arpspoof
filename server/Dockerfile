# Set the base image to Ubuntu
FROM ubuntu:18.04

# File Author / Maintainer
MAINTAINER Rajesh Kalyanam "rkalyanapurdue@gmail.com"

################## BEGIN INSTALLATION ######################

USER root

# Update the repository sources list
RUN apt-get update
RUN apt-get -y upgrade

# Install Apache2
RUN apt-get install -y \
	apache2 \
	apache2-utils \
	libapache2-mod-wsgi \
	git \
	python-pip \
	nodejs \
	npm \
	net-tools \
	supervisor

# Create the default directory
RUN mkdir -p /srv/www/app

# Clone the app from  and install packages
ADD . /srv/www/app
RUN cp /srv/www/app/apache/config/000-default.conf /etc/apache2/sites-available/000-default.conf
RUN cp /srv/www/app/apache/config/apache2.conf /etc/apache2/apache2.conf
RUN pip install -r /srv/www/app/requirements.txt 
RUN a2enmod wsgi
RUN a2enmod rewrite
RUN a2enmod headers
RUN a2enmod ssl
RUN mkdir /etc/apache2/ssl
RUN cp -f /srv/www/app/apache/config/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
RUN cp -f /srv/www/app/apache/config/ssl.conf /etc/apache2/mods-available/ssl.conf
RUN cp -f /srv/www/app/apache/config/ssl.load /etc/apache2/mods-available/ssl.load
RUN a2ensite 000-default
RUN a2ensite default-ssl
RUN service apache2 restart

##Install Wetty
WORKDIR /srv/www/app/wetty
RUN npm install

#create terminal user
RUN useradd -d /home/term -m -s /bin/bash term
RUN echo 'term:term' | chpasswd

#copy supervisord config file
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

##################### INSTALLATION END #####################

# Expose the default port
EXPOSE 80
EXPOSE 3000

#WORKDIR /srv/www/app

# Set default container command
#ENTRYPOINT ["node app.js -p 3000 && /usr/sbin/apache2ctl -D FOREGROUND"]
ENTRYPOINT ["/usr/bin/supervisord"]
#CMD ["runservices.sh"]

