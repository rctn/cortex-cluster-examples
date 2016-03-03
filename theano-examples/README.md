This folder contains information for using GPUs on the cluster with theano. 

There are two ways to use python

(I) Install your own version of python (Recommended)

Directions:

(1) Install Python:
(a) Go to Anaconda website (https://store.continuum.io/cshop/anaconda/) 
and find the download link for anaconda for linux version 2.7

(b) Log into the cluster and run
```
wget <download_link>
bash <downloaded_file>
```
Make sure to say yes to append anaconda installation to .bashrc file
Log out and log in to load new bash environment

(2) Install theano: See here for instructions: 
http://deeplearning.net/software/theano/install.html

(a) Download theano:
```
git clone git://github.com/Theano/Theano.git
```
(b) Run installation
```
cd Theano
python setup.py develop
```
(3) Look at your settings file:
Move the .theanorc file in this folder to:
~/.theanorc
Eg.
```
mv <current .theanorc path> ~/.theanorc
```


(4) Look at the script example.py to see how to use theano for 
matrix multiplication.

(5) Look at the script to submit your job to the cluster. 
Note that our partition name is cortex. You also need to request
a cluster node with a gpu. You need to unload the intel compiler
because theano uses gcc. 

(6) Run sbatch to run your script:
```
sbatch example.sh
```

(II) Use a python installation maintained by the cluster administrators

