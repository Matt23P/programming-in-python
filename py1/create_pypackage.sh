#create new venv
python -m venv venv
#get required packaged
..\venv\Scripts\pip.exe install setuptools wheel
#pip install setuptools wheel
#create package
python setup.py sdist bdist_wheel