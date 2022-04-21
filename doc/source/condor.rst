.. highlight:: shell

######################################
Using Condor
######################################

******************************************************
Condor Submit File
******************************************************

Main parameters in a ``submit.condor`` file:

1. ``universe``: specify which HTCondor universe to use when running the job.

2. ``executable``: the script or program to run that becomes the job.

3. ``arguments``: list of arguments to be supplied to the executable as part of the command line.

4. ``requirements``: request resources (i.e. Machine(s)) needed to process job.

5. ``log``: creates a job event file.

6. ``output``: creates standard output file. 

7. ``error``: creates standard error file that captures any error messages. 

8. ``tranfer_input_files``: list of all files/directories to be transferred into the working directory for the job.

9. ``request_cpus``, ``request_gpus``, ``request_memory``, ``request_disk``: requests needed CPU, GPU, memory and disk space for job.
   If the requested resources are insufficient for the job, it may cause problems for the user and jobs might be put on hold by condor.
   If the requested resources are much greater than needed, jobs will match to fewer slots than they could and may block other jobs.

10. ``queue``: specify the amount of times to repeat job submission for a set of arguments (defaults to 1).

An example of a ``submit.condor`` file:

    .. code-block:: bash

        universe = docker
        # since universe id docker, specify image from CVIB registry
        docker_image = registry.cvib.ucla.edu/{{username}}:condor-quick-start

        executable = run.sh
        should_transfer_files = YES # transfer files to and from the remote machine where the job runs
        transfer_input_files = run.sh

        requirements = (Machine  == "REDLRADADM14958.ad.medctr.ucla.edu" ||  Machine  == "REDLRADADM14959.ad.medctr.ucla.edu" )

        when_to_transfer_output = ON_EXIT # ON_EXIT transfers job's output files back to the machine when the job completes and exits automatically

        # For logging meta data, use $(process) for Numbered files
        output = log/job.$(cluster).$(process).out
        error = log/job.$(cluster).$(process).err
        log = log/job.$(cluster).$(process).log

        # prior to submitting jobs, if you specified a log directory in the submit script,
        # remember to create the directory first, or job will forever be at idle

        request_cpus = 1
        request_gpus = 1
        request_memory = 1GB
        request_disk = 500MB

        arguments = "hello world"
        queue

******************************************************
Basic Commands
******************************************************

    .. code-block:: bash

        condor_q

        condor_q -analyze

        condor_status

        condor_submit

         
