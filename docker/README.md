## Docker Quick-Start

A Dockerfile instructs how the Docker Image will be built. The following are common commands for a Dockerfile:

```
FROM # Tells Docker which base image you want to build your image from
    Ex: FROM tensorflow/tensorflow:2.6.0-gpu-jupyter

PULL # Adds files from Docker repository
    Ex: 

RUN # runs instructions against the image (i.e. build container)
    Ex: RUN python -m pip install --upgrade pip

CMD # specifies the command to run in the container
    Ex: 

> Many other commands exist --> see docker documentation.

> Want to include a .dockerignore --> similar function to .gitignore
> Can save a build.sh file that builds the docker when ran from a command line.
```

Let's run an example to build your own Docker container.

+ login to CVIB registry
```
docker login registry.cvib.ucla.edu
```

+ build image
```
docker build -t hello-tf .
```

+ test out container with interactive mode
```
docker run -it --privileged  hello-tf /bin/bash
/bin/bash hello.sh https://i.stack.imgur.com/Ds5Rc.png results.txt
exit
```

+ push container to registry
```
docker tag hello-tf:latest registry.cvib.ucla.edu/$USER:hello-tf
docker push registry.cvib.ucla.edu/$USER:hello-tf
```

+ test out docker run command
```
docker run -v $PWD:/out registry.cvib.ucla.edu/$USER:hello-tf /bin/bash hello.sh https://i.stack.imgur.com/Ds5Rc.png /out/results.txt
cat results.txt
```

+ run the container
```
docker run -it --privileged hello-tf
```