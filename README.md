# test-skaffold

This is a python app configured to run using profiles.

By default Dockerfile builds an image with ENTRYPOINT leveraging gunicorn.  However, when testing locally with reload = True in gunicorn_conf.py, I noticed the changes are not getting picked up.  So ended up creating antoher profile for flask (Note - needed to override the Entrypoint using Kustomization)
