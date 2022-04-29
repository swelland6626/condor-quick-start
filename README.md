# condor-quick-start
Repo for condor and docker usage documentation in CVIB.

# Running docker and building html
Run docker containing Sphinx setup (change docker_name)
```
export docker_name=your_username_sphinx1
docker run -it --rm --name $docker_name -v /cvib2/apps/personal/wasil/lib:/medqia -v /cvib2:/cvib2 -v /scratch:/scratch -v /apps:/apps -w /workdir --privileged registry.cvib.ucla.edu/sphinxdoc_nb_numpydoc:latest bash

```

Change docs_root to appropriate directory (change path to working directory for building documentation)
```
export docs_root=/cvib2/apps/personal/dtada/lib/condor-quick-start/doc
cd $docs_root
```

Inside the Docker container, build html file
```
make html
```

To remove everything from `build`
```
make clean
```

+ Quick Links
    + Sphinx documentation
    https://www.sphinx-doc.org/en/master/usage/quickstart.html
    + Starting new documentation
    https://www.sphinx-doc.org/en/master/man/sphinx-quickstart.html
    + Dockerfile reference
    https://docs.docker.com/engine/reference/builder/ 
    + Dockerfile writing tips
    https://docs.docker.com/develop/develop-images/dockerfile_best-practices/ 
    