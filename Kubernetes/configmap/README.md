# Deploy Redis using a ConfigMap
## ConfigMap with basic configuration
### Check redis-config file content
`cat redis-config`
### Create ConfigMap from file
`kubectl create configmap example-redis-config --from-file=redis-config`

### See ConfigMap object
`kubectl get configmap example-redis-config -o yaml`

## Create redis deployment


## Links and Original source
https://kubernetes.io/docs/tutorials/configuration/configure-redis-using-configmap/