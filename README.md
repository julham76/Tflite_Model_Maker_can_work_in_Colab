# Tflite_Model_Maker_can_work_in_Colab
Finally Tflite Model Maker can work in Colab!
How do we solve the perennial Tflite Model Maker issue? A lot of researchers was stuck when Google Colab updated to version 3.10 and yet Tflite-Model-Maker still remains at ver 3.9. 

Many researchers have tried to downgrade the Colab to version 3.9 using this command

```
!sudo apt-get install python3.9
```

but nothing works!

The solution: we need to run Google Colab at version 3.9 using virtual environment. We also need to run the training commands as a python script, not directly at the cells. 
Let’s see how does this.

## Inisialisasi
```
%env PYTHONPATH = # /env/python
```
## Get the Miniconda using the commands below
```
!wget https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Linux-x86_64.sh
!chmod +x Miniconda3-py39_23.3.1-0-Linux-x86_64.sh
!./Miniconda3-py39_23.3.1-0-Linux-x86_64.sh -b -f -p /usr/local
!conda update conda
```
## Create a dedicated space (environment) called "myenv" and installing "Python 3.9" into it
```
import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')
```
```
!conda create -n myenv python=3.9
```
## Install Tflite-model-maker in Conda env
```
%%shell
eval "$(conda shell.bash hook)"
conda activate myenv
pip install tflite-model-maker
```
## Test out with a sample dataset (link below) from Roboflow.
It is always good to test out a sample dataset before running our custom dataset. We need to manually separate into the annotation and images file — in total 6 folders
<p align="center">
   <img src="doc/1.png">
</p>
## Upload the train.py script
Upload the train.py (link below) to content. Remember to set the path and label_map correctly.
