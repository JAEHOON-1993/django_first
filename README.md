https://ferodemic.pythonanywhere.com/

1. 장고 프로젝트 zip 파일 배포
2. unzip fc_community.zip
3. virtualenv --python=python3.7 fc_env
4. source fc_env/bin/activate
5. pip install django
6. cd fc_community/
7. python manage.py collectstatic
8. (옵션) python manage.py makemigrations
9. python manage.py migrate
10. exit

Web
Code:
What your site is running.

Source code:
/home/ferodemic/fc_community

Go to directory
Working directory:
/home/ferodemic/

Go to directory
(!Django로 수정) WSGI configuration file:/var/www/ferodemic_pythonanywhere_com_wsgi.py
Python version:
3.7

Virtualenv:
Use a virtualenv to get different versions of flask, django etc from our default system ones. More info here. You need to Reload your web app to activate it; NB - will do nothing if the virtualenv does not exist.

/home/ferodemic/fc_env
