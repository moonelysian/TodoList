깃 설치
sudo apt install git

파이썬 설치
sudo apt install python3.7

pip3 설치
sudo apt install python3-pip

가상 환경 소프트웨어 설치
sudo pip3 install virtualenvwrapper

가상환경 설정
vim ~/.bashrc 후 아래 코드 추가

export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh


가상환경 생성
mkvirtualenv myvenv

django 설치
pip3 install django

git clone https://github.com/moonelysian/TodoList.git

cd TodoList

