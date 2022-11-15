#create new venv
python -m venv venv
#get required packaged
pip install setuptools wheel
#create package
python create.py sdist bdist_wheel