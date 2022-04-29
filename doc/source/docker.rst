******************************
Docker
******************************

++++++++++++++++++++++++++++++
What is Docker?
++++++++++++++++++++++++++++++

Docker is a tool for building and using software based on the concept of packaging
code and it's dependencies into a single unit using containers and images.
Containers are the single units that run the code inside of them and contain all
the dependencies needed to do so. Images are like snapshots of the contents of the
container that get saved for building new containers similar to the current one.

The special characteristic of containers though is that they don't make
permanent changes to anything outside the container, i.e. to the image. So 
whatever happens inside the container is gone after the container is exited. 
However, a container no longer running has state and can be saved to 
an image for future use.

++++++++++++++++++++++++++++++
Creating a Dockerfile
++++++++++++++++++++++++++++++

Docker images are built using Dockerfiles which contain 'layers'. Each instruction 
in a Dockerfile creates a new layer. The following are common instructions for a 
Dockerfile (convention is for instructions to be uppercase to distinguish them 
from arguments):

*  ``FROM``: Specifies parent image you want to build your image from (the first command in a Dockerfile **must** be ``FROM``, although comments and args used in ``FROM`` are an exception).
*  ``PULL``: Adds files from Docker repository.
*  ``RUN``: Executes commands in layers above and commits them for the container built from the next layer. ``RUN`` has 2 forms: a shell (terminal) form and an exec (inside the Dockerfile) form.
*  ``COPY``: Copies new files, directories, or remote URLs from ``<src>`` and adds them to the filesystem of the image path ``<dest>``.
*  ``CMD``: Specifies the command to run in the container. There can only be one ``CMD`` instruction in a Dockerfile.

Use a ``.dockerignore`` file to exclude files from the container build. Usage is 
similar to a ``.gitignore`` file. See below for more detailed Docker documentation:

* Dockerfile reference:

   * https://docs.docker.com/engine/reference/builder/

* Specific documentation on ``docker build``:

   * https://docs.docker.com/engine/reference/commandline/build/

* Specific documentation on ``docker run``:

   * https://docs.docker.com/engine/reference/run/

* Dockerfile writing tips:

   * https://docs.docker.com/develop/develop-images/dockerfile_best-practices/


An example of a simple Dockerfile:

   .. code-block:: bash

      FROM tensorflow/tensorflow:2.6.0-gpu-jupyter

      RUN python -m pip install --upgrade pip
      # requirements.txt is a file containing dependencies to install inside the container
      COPY requirements.txt .
      RUN pip install -r requirements.txt

A more complex Dockerfile:

   .. code-block:: bash

      FROM sphinxdoc/sphinx-latexpdf
      # FROM sphinxdoc/sphinx

      ARG MYPATH=/usr/local
      ARG MYLIBPATH=/usr/lib

      RUN apt-get update && apt-get install -y --no-install-recommends \
            autotools-dev \
            build-essential \
            ca-certificates \
            cmake \
            git \
            wget \
            curl \
            vim
      RUN rm -rf /var/lib/apt/lists/*

      # install miniconda.
      # create and activate python virtual env with desired version
      RUN wget --quiet --no-check-certificate https://repo.continuum.io/miniconda/Miniconda3-4.6.14-Linux-x86_64.sh --no-check-certificate -O ~/miniconda.sh && \
         /bin/bash ~/miniconda.sh -b -p /opt/conda
      RUN /opt/conda/bin/conda create -n py python=3.7.2
      RUN echo "source /opt/conda/bin/activate py" > ~/.bashrc
      ENV PATH /opt/conda/envs/py/bin:$PATH
      RUN /bin/bash -c "source /opt/conda/bin/activate py"

      RUN /bin/bash -c "source /opt/conda/bin/activate py && conda install cython numpy -y && pip install scikit-build && pip install matplotlib"
      RUN /bin/bash -c "source /opt/conda/bin/activate py && conda install -c conda-forge jupyterlab -y"
      RUN /bin/bash -c "source /opt/conda/bin/activate py && conda install -c conda-forge nbsphinx -y"

      RUN pip install sphinx-rtd-theme numpydoc sphinx-copybutton
      # RUN pip install ipywidgets matplotlib medpy opencv-python plotly tabulate
      # RUN pip install tensorflow pandas scikit-image pydicom

      # ARG UNAME=testuser
      # ARG UID=1000
      # ARG GID=1000
      # RUN groupadd -g $GID -o $UNAME
      # RUN useradd -l -m -u $UID -g $GID -o -s /bin/bash $UNAME && \
      #     usermod -aG sudo $UNAME
      # RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
      # USER $UNAME

      # CMD /bin/bash


++++++++++++++++++++++++++++++
Useful commands
++++++++++++++++++++++++++++++

Some useful terminal commands in case you run into issues where you close a terminal
without exiting the docker container. Doing so will result in an error message that 
says something about the port already being allocated.

* ``docker image ls``: lists all docker containers and their IDs
* ``docker rmi -f container-id``: removes a running docker image
* ``docker exec``: runs a command inside a a running container
* ``docker exec -it [container-id] bash```: enters an already running docker



   .. code-block:: bash

      # download existing docker image from docker repo

      # build docker image

      # run docker image
