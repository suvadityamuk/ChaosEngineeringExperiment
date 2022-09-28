# Steps

## Start `docker` service

Start the `docker` service or any other Container virtualization tool
`sudo systemctl start docker`

## Setting up of `minikube` Kubernetes Local Cluster

Minikube sets up a local cluster that can be used for testing/debugging/experimentation on Kubernetes
`minikube start`

## Enable add-ons to allow Ingress

Using Ingress-rules allow us to set up routing rules for network traffic
`minikube addons enable ingress`

## Verify that `NGINX` is set-up fine

Setting up NGINX is required to provide a reverse-proxy server on top of Kubernetes. Without it, Chaos-Mesh and other several systems will be unable to work.
`kubectl get pods -n ingress-nginx`

## Creating our resources - 1 service, 1 deployment, 1 ingress rule

The service, deployment and ingress-rule each has its important role.
- Service : Informs Kubernetes to set up port 5000 as the endpoint for the API
- Deployment : Sets up a default cluster of 4 pods based on the Docker image generated from the image
- Ingress-Rule : Sets up the pathway for allowing port 5000 to be forwarded to the local machine port 5000 indefinitely

`kubectl apply -f kubernetes-deploy.yaml`

## Verify that all resources are made fine
`kubectl get svc, deploy, ingress`

## cURL into the cluster with a sample request
`curl -X GET "http://192.168.39.156:80/add?n1=4.25&n2=7.65"`

## Start up chaos-mesh (Install if not present)
`curl -sSL https://mirrors.chaos-mesh.org/v2.3.2/install.sh | bash`

## Verify Chaos-Mesh resources are up and running
`kubectl get po -n chaos-mesh`

## Enter Chaos-Mesh dashboard
`kubectl port-forward -n chaos-mesh svc/chaos-dashboard 2333:2333`

## (Optional) Script for making 250 requests in quick succession
```
for i in {1..250}
do
    curl -X GET "http://192.168.39.156:80/add?n1=4.25&n2=7.65"
done;
```

## Clean-up after completing
`kubectl delete svc chaos-target-service`  
`kubectl delete deployment chaos-exp-deployment`  
`kubectl delete ingress chaos-ingress`  

## Delete `minikube` cluster
`minikube stop`