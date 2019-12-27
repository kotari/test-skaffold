# test-skaffold

This is a python app to run on minikube using skaffold.
It runs the python API using flask and gunicorn based on profiles being used.

By default Dockerfile builds an image with ENTRYPOINT leveraging gunicorn.  However, when testing locally with reload = True in gunicorn_conf.py, I noticed the changes are not getting picked up.  So ended up creating antoher profile for flask (Note - need to override the Entrypoint using Kustomization)

Follow instructions from below urls to have minikube, kustomization and skaffold running on your local machine

minikube - https://kubernetes.io/docs/tasks/tools/install-minikube/
kustomize - https://github.com/kubernetes-sigs/kustomize/blob/master/docs/INSTALL.md
skaffold - https://skaffold.dev/docs/install/

To run flask profile use the below command (still need to figure out if --port-forward can be skipped)
```
skaffold dev -p flask --port-forward
```
This will start flask app on default port and to cleanup 
```
skaffold delete -p flask
```

To run gunicorn profile use the below command
```
skaffold dev -p gunicorn --port-forward
```
This will start gunicorn on binding defined in gunicorn_conf.py
To do a cleanup
```
skaffold delete -p gunicorn
```
