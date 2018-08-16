#!/bin/bash

kubectl delete service arpspoof-service-hacker arpspoof-service-victim arpspoof-service-server

kubectl delete networkpolicy arpspoof-internal arpspoof-public

kubectl delete pod hacker victim server

