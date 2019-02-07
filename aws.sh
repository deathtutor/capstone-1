# AWS CONFIG FILE
# run after cloning the github repository 

sudo yum update -y
sudo yum install git -y
git clone https://github.com/stansmall/capstone.git 
cd capstone
sudo yum install -y docker 
sudo curl -L https://github.com/docker/compose/releases/download/1.20.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose 
sudo chmod +x /usr/local/bin/docker-compose 
sudo service docker start 
sudo usermod -a -G docker ec2-user 
cd capstone/react-app
sudo curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.32.0/install.sh | bash 
. ~/.nvm/nvm.sh 
nvm install 11.9.0 
npm install
