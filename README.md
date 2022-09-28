# Chaos Engineering Experiment

This repository holds the code to perform a simple but full-featured demonstration of Chaos engineering using Chaos-Mesh. 

## Requirements

- [`Docker`](https://docs.docker.com/engine/install/)
- [`Kubernetes Command Line (kubectl)`](https://kubernetes.io/docs/tasks/tools/)
- [`Minikube`](https://minikube.sigs.k8s.io/docs/start/)
- [`Flask`](https://flask.palletsprojects.com/)
- [`Python`](https://www.python.org/downloads/)

## Steps to recreate experiment

- For detailed steps, follow the file `kubernetes-chaos.md`, which details the steps
- The setup was tested on `Fedora Linux 36` with Intel i7-10750H, 16GB RAM

## Details of the experimental environment

- We deploy a simple `Flask` API that can perform Floating-point addition, subtraction, multiplication and division of two numbers
- A `Dockerfile` is created that will allow creation of the container image
- We install `minikube` on our system that will allow us to simulate a `Kubernetes` cluster on our local machine
- The `Flask` API, wrapped in a container image, is deployed on a Kubernetes cluster of 4 pods with a NGINX reverse-proxy server placed in front. 

## Simple Notes
- The Chaos-Mesh dashboard can be accessed by port-forwarding 2333 from its deployed pod, to the localhost
- Navigate to `http://127.0.0.1:2333` to get access to the Chaos-Mesh dashboard