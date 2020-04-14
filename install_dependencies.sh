# if directory is changed then make sure to udpate it in this file
sudo apt-get update
# Install python
sudo apt-get install python3 python3-pip supervisor nginx -y

# Install python libraries
pip3 install -r requirements.txt

# update the directory path in config files
PROJECT_NAME="license_key_mgmt"
PROJECT_PATH=`pwd`/$PROJECT_NAME
RUNSERVER_PATH=$PROJECT_PATH/runserver.sh
sed -i "s|RUNSERVER_PATH|$RUNSERVER_PATH|g" backend.conf
sed -i "s|DIR_PATH|$PROJECT_PATH|g" runserver.sh
sed -i "s|NAME_OF_PROJECT|$PROJECT_NAME|g" runserver.sh

# setup the supervisor
sudo cp backend.conf /etc/supervisor/conf.d/backend.conf
sudo supervisorctl reload

# setup the nginx
sudo cp default /etc/nginx/sites-enabled/default
sudo nginx -s reload

# Migrate changes
python3 $PROJECT_PATH/manage.py makemigrations
python3 $PROJECT_PATH/manage.py migrate

# Create superuser
echo "-------------CREATE SUPERUSER ACCOUNT----------------"
python3 $PROJECT_PATH/manage.py createsuperuser
echo "-----------------------------------------------------"
echo "All setup done!!"