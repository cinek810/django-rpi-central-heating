General requirements
=====================
This repository contains django app 'sterowaniePokoi' that allows one to control temperature using the 1-wire sensors, prerequistes:
- owserver running on localhost on port 4304
- python packages: pyownet, RPI

Apache Config
=================
<blockquote>
root@raspberrypi:~/django-ogrzewanie/ogrzewanie# cat /etc/apache2/sites-enabled/sterowanieOgrzewania 
LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so
WSGIScriptAlias /  /root/django-ogrzewanie/ogrzewanie/ogrzewanie/wsgi.py
WSGIPythonPath  /root/django-ogrzewanie/ogrzewanie/
Alias /static	/root/sterowanie-static/

<Directory /root/django-ogrzewanie/ogrzewanie/ogrzewanie>
<Files wsgi.py>
Allow from all
</Files>
</Directory>
</blockquote>
Cron job
=========
<blockquote>
*  *    * * *   root    cd /root/django-ogrzewanie/ogrzewanie && python manage.py updateOut
</blockquote>
