# Autoscale example

Create pod nginx
```bash
kubectl apply -f nginx.yaml
```
Add service to be able to overload the pod, forcing it to scale

```bash
kubectl apply -f nginx-service.yaml
```
This service is using a `NodePort` so, get it in order to `curl` from the outside...

```bash
kubectl get services nginx
```
