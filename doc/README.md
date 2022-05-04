Run docker containing Sphinx setup (change docker_name)
```
export docker_name=dtada_sphinx1
export docker_name=swelland_sphinx
docker run -it --rm --name $docker_name -v /cvib2/apps/personal/wasil/lib:/medqia -v /cvib2:/cvib2 -v /scratch:/scratch -v /apps:/apps -w /workdir --privileged registry.cvib.ucla.edu/sphinxdoc_nb_numpydoc:latest bash

```

Change docs_root to appropriate directory (working directory for building documentation)
'''
export docs_root=/cvib2/apps/personal/dtada/lib/condor-quick-start/doc
export docs_root=/cvib2/apps/personal/swelland/sandbox/condor-quick-start/doc
cd $docs_root
'''

Editing a file in $docs_root (example: conf.py)
```
cd source
vim conf.py
```

Build html file
```
make html
```

To remove everything from `build`, execute inside /cvib2/apps/personal/dtada/lib/condor-quick-start/doc inside docker
```
make clean
```

+ Quick Links
    + Sphinx documentation
    https://www.sphinx-doc.org/en/master/usage/quickstart.html
    + Starting new documentation
    https://www.sphinx-doc.org/en/master/man/sphinx-quickstart.html
    