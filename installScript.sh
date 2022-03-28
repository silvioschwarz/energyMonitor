#! /bin/sh

python3 -m pip install pip --upgrade
python3 -m pip install virtualenv

virtualenv energyTapo

source energyTapo/bin/activate

python -m pip install pip --upgrade
python -m pip install wheel
python -m pip install -r requirements
python -m pip install ipykernel
python -m ipykernel install --user --name=energyTapo

