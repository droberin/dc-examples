# Traefik with TLS

## Deploy backend

`kubectl create -f backend.yaml`

## Create certificates using OpenSSL

`openssl req -newkey rsa:2048 -nodes -keyout tls.key -x509 -days 365 -out tls.crt`

## Create a secret containing these certificates

`kubectl create secret generic traefik-cert --from-file=tls.crt --from-file=tls.key`

## Create a configmap for traefik using default configuration

`kubectl create configmap traefik-conf --from-file=traefik.toml`

## Deploy Traefik

`kubectl create -f traefik.yaml`

## Configure its Ingress
kubectl create -f ingress.yaml



###### traefik-k8s-tls-example ORIGINAL WORK by Patrick Easters

This repo contains the Kubernetes resources used in my Medium post detailing the use of Traefik on Kubernetes with TLS

[Check out the post](https://patrickeasters.com/using-traefik-with-tls-on-kubernetes/) for details on how to use this.
