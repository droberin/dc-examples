# Deploy Redis POD with a ConfigMap
## ConfigMap with basic configuration

### Check redis-config file content
```
cat redis-config
```
### Create ConfigMap from file
```bash
kubectl create configmap example-redis-config --from-file=redis-config
```

### See ConfigMap object
```bash
kubectl get configmap example-redis-config -o yaml
```

## Create redis pod
### Look at redis pod manifest content
```bash
cat redis-pod.yaml
```

THIS IS A POD! NOT A DEPLOYMENT!
«So, no amazing `ReplicaSet` nor `rollouts`»

### Apply it.
```bash
kubectl apply -f redis-pod.yaml
```

See the pod
```bash
kubectl get pods redis
```

**Notice that pod name is `redis` and not redis-blahblah**.

Access redis pod redis-cli
```bash
kubectl exec -it redis redis-cli
```
In that CLI execute:
```
CONFIG GET maxmemory
```
and 
```bash
CONFIG GET maxmemory-policy
```

then 
```bash
exit
```

## Clean up.
```bash
kubectl delete -f redis-pod.yaml
kubectl delete configmap example-redis-config
```

Deleting `configmap` object may fail if pod was not deleted

## Links and Original source
https://kubernetes.io/docs/tutorials/configuration/configure-redis-using-configmap/

# EOF ;)
