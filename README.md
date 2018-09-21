# ArpSpoof

This is a demonstration of the man-in-the-middle (MITM) ARP poisoning attack. A hacker on the same network as a victim communicating with a server can mislead the victim leading all communication with the server to pass through the hacker. The hacker accomplishes this by sending out spurious ARP messages on the network causing the victim to incorrectly map the IP address of the server with the MAC hardware address of the hacker in its ARP tables. This demonstration includes three containers; one each for the hacker, victim and server.

# Installation and Usage

## Installation

Build each of the containers separately:

```bash
cd hacker-notebook
docker build -t cheesehub/arpspoof-hacker .

cd victim-vnc
docker build -t cheesehub/arpspoof-victim .

cd server
docker build -t cheesehub/arpspoof-server .
```
The hacker provides a Jupyter notebook interface; the victim is a VNC-enabled Ubuntu 18.04 container and the server includes a simple web application and a Wetty terminal. We will expose different ports when running these containers:

```bash
docker run -d -p 8888 cheesehub/arpspoof-hacker

docker run -d -p 80 cheesehub/arpspoof-victim

docker run -d -p 3000 cheesehub/arpspoof-server
```

## Usage

Select Hacker.ipynb from the ``hacker`` Jupyter notebook interface for a step-by-step overview of executing the ARP poisoning attack. The notebook included commands that need to be run on the victim and server. A terminal for running the commands from the notebook can be launched from the Jupyter notebook interface. In the ``victim`` VNC window, click the start menu at the bottom left corner and navigate the menu options to launch a terminal window. You will be prompted to login to the Wetty session in the ``server`` container. Use ``term`` for both the username and password.

ARP poisoning requires the three containers to be on the same local network. When running these containers using ``docker run``, they are all attached to the same Docker bridge network on the same host. However, if using Kubernetes ensure that the pods are all deployed to the same cluster node. Also, this demonstration has been found to not work when using certain overlay networks. Currently, this has been tested successfully on the Weave overlay network.  

