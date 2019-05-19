# 우분투에서 실행하기 위한 방법

## 깃 설치
sudo apt install git

## 파이썬 설치
sudo apt install python3.7

## pip3 설치
sudo apt install python3-pip

## 가상 환경 소프트웨어 설치
sudo pip3 install virtualenvwrapper

## 가상환경 설정
vim ~/.bashrc 후 끝에 아래 코드 추가

`export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh`


## 가상환경 생성
mkvirtualenv myvenv

## django 설치
pip3 install django

## git에서 가져오기
git clone https://github.com/moonelysian/TodoList.git

## 디렉터리로 이동 후 설치
cd TodoList

pip install gunicorn
pip install dj-database-url
pip install psycopg2-binary
pip install whitenoise

## migrate
python manage.py migrate

## 서버 실행
python manage.py runserver
