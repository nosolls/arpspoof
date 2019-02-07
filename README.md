# ARPSpoof Attack

## Description of the scenario

The ARP (Address Resolution Protocol) Spoofing attack is a typical "man-in-the-middle" attack by which a hacker who has gained 
access to communication between two parties can subsequently monitor, and, relay modified communication between these parties 
without their knowledge. The first step in this attack involves "poisoning" the ARP table on the targeted machines so as to 
allow the hacker to intercept communication. This repository contains a demonstration of the ARP poisoning attack. You will be 
able to verify that the attack was successful by examining the ARP tables on the affected machines and monitoring network traffic 
between these machines.

## Target Audience

### Instructors

If you are an instructor teaching cybersecurity concepts and, specifically network security, you can use this example to provide hands-on 
experience with ARPSpoof attacks, demonstrating the ease with which network traffic can be compromised. The ARPSpoof attack 
is also the first step in demonstrating SSLStrip, whereby even SSL-enabled communication can be compromised once a hacker has 
successfully poisoned ARP tables. These two demonstrations together can illustrate the real-world impacts.

### Students

If you are a student in a cybersecurity or computer networks class, or, a budding web developer, it is instructive to understand how 
network traffic can be compromised by a well-situated hacker. If you are currently learning about ARP poisoning in your class, you can 
get further practical experience with how these attacks operate, and, learn how to identify such attacks.

## Design and Architecture

This demonstration is designed using three Docker containers, one each for the hacker, victim, and, server attached to the same virtual 
network. The containers all come with the necessary network tools to ping, examine ARP tables, and, trace packet routing between machines. The hacker machine comes with the ARPSpoof command line tool for running an ARP poisoning attack. The victim container provides a VNC interface to Ubuntu and the requisite commands can be run on the LXTerminal emulator. Both the hacker and server provide a Jupyter notebook interface; the necessary commands can be run in the terminal console provided by Jupyter. The hacker notebook contains instructions on conducting the ARP poisoning attack; including the commands to be run on each of the three containers.

## Installation and Usage

The recommended approach to running this set of containers is on CHEESEHub, a web platform for cybersecurity demonstrations. CHEESEHub 
provides the necessary resources for orchestrating and running containers on demand. In order to set up this application to be 
run on CHEESEHub, an *application specification* needs to be created that configures the Docker image to be used, memory and 
CPU requirements, and, the ports to be exposed for each of the three containers. The JSON *spec* for this ARPSpoof demonstration can be 
found [here](https://github.com/rkalyanapurdue/catalog/tree/master/arpspoof).

CHEESEHub uses Kubernetes to orchestrate its application containers. You can also run this application on your own Kubernetes 
installation. For instructions on setting up a minimal Kubernetes cluster on your local machine, refer to [Minikube](https://github.com/kubernetes/minikube). 

Before being able to run on either CHEESEHub or Kubernetes, Docker images needs to be built for the three application containers. 
Container definitions for the hacker, victim, and, server can be found in the *hacker-notebook*, *victim-vnc*, and, *server* directories 
respectively. To build these containers, run:

```bash
cd hacker-notebook
docker build -t <hacker image tag of your choice> .

cd victim-vnc
docker build -t <victim image tag of your choice> .

cd server
docker build -t <server image tag of your choice> .
```

Once the Docker images have been built, you can run the containers using just the Docker engine. By default, all containers are attached to the default Docker network.

```bash
docker run -d -p 8888 <hacker image tag from above>

docker run -d -p 80 <victim image tag from above>

docker run -d -p 8888 <server image tag from above>
```

Since the user facing interface of the hacker and server containers is the Jupyter notebook we expose port 8888 to be accessible on the 
host machine. The victim container provides the VNC interface on port 80.

### Usage
On navigating to the URL of the hacker container in your browser, you will be presented with a Jupyter notebook interface displaying a list of files 
and folders. Click to select the Hacker.ipynb Jupyter notebook to begin. The notebook includes a step-by-step overview of how to examine the ARP 
tables, use ping to establish simple communication between the victim and server, and run the ARP poisoning attack from the hacker. Following the 
attack, you will re-examine the ARP tables to confirm success of the attack, and, discover how the regular communication is *seemingly* unaffected unless examined closely.

## How to Contribute

To report issues or contribute enhancements to this application, open a GitHub issue. 

