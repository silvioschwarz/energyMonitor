#! /bin/bash

python3 -m pip install pip --upgrade
python3 -m pip install virtualenv ipykernel wheel setuptools

echo "Enter environment name:"
read name
#echo $name

python3 -m virtualenv $name
python3 -m ipykernel install --name=$name --user
