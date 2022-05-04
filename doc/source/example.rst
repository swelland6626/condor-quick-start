######################################
Example
######################################

Example showing how to use docker and condor to submit a job.

First, you need to build a docker image and put it in the CVIB registry.

    .. code-block:: bash

        # From a temrinal inside your sandbox directory, login to the CVIB docker registry
        docker login registry.cvib.ucla.edu
        
        # Build a docker image using the same Dockerfile you created in the docker example:
        docker build -t docker-condor-ex .

        # Now export it 
        export REMOTE_URL=registry.cvib.ucla.edu/$USER:docker-condor-ex

        # Tag it
        docker tag docker-condor-ex $REMOTE_URL

        # Push it
        docker push $REMOTE_URL


Now you need to make a condor submit file.

    .. code-block:: bash

        # condor submit file here
        # path to example in git: /condor-quick-start/docker_example/mnist_ex.py

        # path in condor submit file needs to be /sandbox/mnist_ex.py


The docker image has been built and now you can launch a container and submit the job.

    .. code-block:: bash

        # launch a docker container based on the image you built
        docker run -it -v $PWD:/workdir -w /workdir -v /radraid:/radraid -u $(id -u):$(id -g) docker-condor-ex bash

        # Submit the job to condor
        condor_submit submit.condor


You can exit the docker container and use ``condor_q`` to view the status of the job. You can also view the resource the job is using by 
going `here <http://radcondor.cvib.ucla.edu:48109/>`_ and finding your username (this model doesn't actually use a GPU but normally this is how you view resource usage). 
Finally, use ``ctrl+d`` or ``exit`` to exit the docker container.