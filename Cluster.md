## Using the cluster to get GPU access

The UConn [hpc cluster](https://hpc.uconn.edu) offers access to a range of GPU facilities. This note
describes the bare minimum you need to get access to a compute node with a GPU that can run
pytorch (CUDA 10.1).  

1.  [Get an account on the cluster (the Storrs facility)](https://hpc.uconn.edu/storrs/account-application/).
You can use my name as advisor when asked.

2.  Make sure you have the VPN up and running.  Then you can log in to the head node on the cluster:

```
$ ssh netid@login.storrs.hpc.uconn.edu
```

3.  You are not allowed to run jobs on the login node, so you want to start an interactive job using the
scheduler.  If you don't need the GPU, you can run

```
$ srun --pty bash
```

This will start a ```bash``` shell on an available node.  Take note of the prompt or run the ```hostname```
commmand to see which node you've been assigned.

```
[jet08013@cn277 ~]$ hostname
cn277
```

4. Probably the simplest thing to do is to install the anaconda
distribution in your home directory on the cluster, just as you would
on your home computer.  You are given 50GB of storage for your home
directory which is plenty -- unless you are doing serious work with
large datafiles, but in that case you will need to learn more about
the cluster than this note will tell you.

5.  Once you have anaconda working, you can install pytorch using conda using the directions
[on the pytorch website](https://pytorch.org/get-started/locally/).   If you want to use the GPU,
make sure to follow the instructions for CUDA on linux.  The command is:
```
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
```

It's best
to do this in a virtual environment (if you don't know what this means, ask me).  

One complication: if you want to run pytorch without the GPU, on a cluster node without a GPU -- perhaps
for development -- then you should install two versions of pytorch in two different virtual
environments.  The CUDA version won't run on a node without a GPU.

6.  Go back to the login node (by typing ```exit``` in your interactive shell job). 

7.  Connect to a gpu node.  We are using the RTX GPU, which is a single-precision, consumer-type
GPU.  There are fancier ones on the cluster but they are running a different version of CUDA.  If
you are using tensorflow, you can use these other nodes, but I won't talk about that here.

Notice that I activate the virtual environment that has pytorch in it.

```
$ srun -p gpu_rtx --gres=gpu:1 --pty bash
srun: job 3236057 queued and waiting for resources
srun: job 3236057 has been allocated resources
(base) [jet08013@gpu01 ~]$ conda activate torch
(torch) [jet08013@gpu01 ~]$ 
```

8. Load CUDA (you can put this in your startup file if you want).

```
$ module load cuda/10.1
```

9. Check to see that torch is A-OK.

```
(torch) [jet08013@gpu01 ~]$ python
Python 3.8.1 (default, Jan  8 2020, 22:29:32)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> print(torch.cuda.is_available())
True
```

10. To run jupyter, you first start jupyter lab on the cluster, and then create an ssh "tunnel" to it
so you can use your web browser.  On the cluster:

```
(torch) [jet08013@gpu01 ~]$ jupyter lab --no-browser --port=8888
```
Take note of this line at the end of the output:
```
Or copy and paste one of these URLs:
        http://localhost:8888/?token=f91e33313658760ab931e5220642ee18384f3bf168be745f
     or http://127.0.0.1:8888/?token=f91e33313658760ab931e5220642ee18384f3bf168be745f
```

Also note in the prompt on the cluster which gpu node you are assigned to:
```
(torch) [jet08013@gpu01 ~]$ hostname
gpu01
```


11. Keep your terminal window on the cluster open, and go back to your laptop and open an ssh tunnel:

```
(laptop)$ ssh -NL localhost:8888:gpu01:8888 netid@login.storrs.hpc.uconn.edu
```

where you replace gpu01 with whatever output you got from step 10 for the gpu node name.  Keep this
window open to maintain the connection.

12. Finally, paste one of the URL's you took note of into your web browser and hopefully a window
will open on your browser connected to the cluster.

13. To quit, you can quite from the window on your browser and close down the windows with the ssh tunnel and
the cluster.

**Note:** There are many ways to simplify this process.  If you find yourself using it and want to streamline it, talk to me.
