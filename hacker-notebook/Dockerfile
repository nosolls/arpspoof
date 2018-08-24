FROM rkalyana/base-notebook
MAINTAINER Rajesh Kalyanam <rkalyanapurdue@gmail.com>

USER root

# Install necessary net util packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    dsniff \
    inetutils-ping \
    inetutils-traceroute \
    net-tools \
    iptables \
    python-twisted-web \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    NB_USER=jovyan \
    NB_UID=1000 \
    NB_GID=100 \
    PATH=$CONDA_DIR/bin:$PATH \
    HOME=/home/$NB_USER

#copy SSLStrip to tmp
COPY sslstrip /tmp

WORKDIR /tmp

#install SSLStrip
RUN python setup.py install

#copy the primary notebook
COPY --chown=1000:100 Hacker.ipynb $HOME/

#Allow Jupyter user (jovyan) to modify IP tables, run arpspoof 
#as root without a password
ADD hackersudo /etc/sudoers.d/

RUN fix-permissions $CONDA_DIR

EXPOSE 8888
WORKDIR $HOME

# Configure container startup
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

# Switch back to hacker to avoid accidental container runs as root
USER $NB_UID
