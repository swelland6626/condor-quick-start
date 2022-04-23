######################################
Using Docker
######################################

*******************************************
Docker quickstart-guide
*******************************************

Docker is a tool for building and using software based on the concept of packaging
code and it's dependencies into a single unit using containers and images.
Containers are the single units that run the code inside of them and contain all
the dependencies needed to do so. Images are like snapshots of the contents of the
container that get saved for building new containers similar to the current one.

The special characteristic of containers though is that they don't make
permenant changes to anything outside the container, i.e. to the image. So 
whatever happens inside the container is gone after the container is exited. 
However, a container no longer running, has state and can be saved (committed) to 
an image for future use.

Put simply:
A Dockerfile describes how the image will be built.
The following are common commands for a Dockerfile:

*  ``FROM``: Tells Docker which base image you want to build your image from.
*  ``PULL``: Adds files from Docker repository



   .. code-block:: bash

      # download existing docker image from docker repo

      # build docker image

      # run docker image
