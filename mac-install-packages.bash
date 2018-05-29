#install selenium
pip install selenium

#get django 1.7.11
wget https://www.djangoproject.com/m/releases/1.7/Django-1.7.11.tar.gz
tar xvzf Django-1.7.11.tar.gz
cd Django-1.7.11

#install django
python setup.py install

#install drivers
brew install phantomjs
brew install geckodriver
