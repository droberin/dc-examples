# Rolling Update example

Apply `nginx-rolling` deployment and its service
```bash
kubectl apply -f deployment-1.7.yaml
kubectl apply -f service.yaml
```

Check current `rollout` status:
```bash
kubectl rollout status deploy/nginx-rolling
```

Check its history, which should only have one revision.
```bash
kubectl rollout history deploy/nginx-rolling
```

As it has no annotation, let's set one
```bash
kubectl annotate deployment/nginx-rolling kubernetes.io/change-cause="Release 1.0 is here"
```

Check history again
```bash
kubectl rollout history deploy/nginx-rolling
```

See deployment info
```bash
kubectl get deployments nginx-rolling -o wide
```

Update deployment with newer nginx version from the other manifest file
```bash
kubectl apply -f deployment-1.15.8-alpine.yaml
```

It should inherit previous annotations on the now generated revision...
Check history again
```bash
kubectl rollout history deploy/nginx-rolling
```

Set it like it was nothing...
```bash
kubectl annotate deployment/nginx-rolling kubernetes.io/change-cause="Release 2.0 is here"
```

See deployment info
```bash
kubectl get deployments nginx-rolling -o wide
```
Did it change its version?


Now... «FREAK OUT!» "This is not working..." Let's roll back (undo)!
```bash
kubectl rollout undo deployment nginx-rolling
```

Hint: this can be rolled back to any revision by adding `--to-revision=REVISION_NUMBER`.

Check history again!
```bash
kubectl rollout history deploy/nginx-rolling
```
Check the output carefully on its `CHANGE-CAUSE` and `REVISION`


See also image version on deployment
```bash
kubectl get deployments nginx-rolling -o wide
```

Clean up!
```bash
kubectl delete deployment nginx-rolling
kubectl delete -f service.yaml
```

#EOF ;)
