.. raw:: html
    <embed>
        
        <img src="https://github.com/24ERIC/official_website/blob/main/static/LOGO%2B%E5%AD%97%202022%20%E9%80%8F%E6%98%8E%E5%BA%95.png">
        <br>
    </embed>
    
    
    
|a| |b| |c| |d| |e| |f|

.. |a| image:: https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A  

.. |b| image:: https://img.shields.io/pypi/dm/numpy.svg?label=PyPI%20downloads

.. |c| image:: https://img.shields.io/conda/dn/conda-forge/numpy.svg?label=Conda%20downloads

.. |d| image:: https://img.shields.io/badge/stackoverflow-Ask%20questions-blue.svg

.. |e| image:: https://img.shields.io/badge/DOI-10.1038%2Fs41592--019--0686--2-blue

.. |f| image:: https://api.securityscorecards.dev/projects/github.com/numpy/numpy/badge
    
    
   
"""""""""""""""""
Development Guidance
"""""""""""""""""


...........
UTM021 IT Development Team
...........
.. contents:: Note: The following Guidance is designed for Macbook or Linux. Eric don't familiar with Windows but can help you!
   :depth: 3
   


Introduction
===================
This project is aimed for developing and maintaining the Official Website for UT021 in University of Toronto by IT Development Team (Logistics Department in UT021). Website uses Python Django (Basic Framework), integrate with MangoDB (Database), and deploys on Vercel (Cloud Server). THe website contains two main part: one part is the display of UT021 details, second part is the development backyard.


.. |Generic badge| image:: https://img.shields.io/badge/<SUBJECT>-<STATUS>-<COLOR>.svg
   :target:


Quick SetUp
===================
Eric Strongly suggest you to have a look at this file before starting contribute to the project :) it may saves you tons of times !


.. code:: python

   # install python3 by following: https://www.freecodecamp.org/news/python-version-on-mac-update/
   
   # install pip by following: https://phoenixnap.com/kb/install-pip-mac
   
   # install git by following: https://phoenixnap.com/kb/install-git-on-mac

   # Eric suggest VScode and Github Desktop, by following: https://code.visualstudio.com/docs/setup/mac   and   https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop
   
   cd github      # assume you have a directory called "github", which place all the github project
   
   git clone https://github.com/24ERIC/official_website.git       # clone official_website to local
   
   cd official_website
   
   pip install virtualenvwrapper    # download virtual environment package for python
   
   virtualenv official_website_virtual_environ        # create virtual environment for official website

   source official_website_virtual_environ/bin/activate     # activate it
   
   pip install django djongo pymongo pytz       # install all the packages we need

   deactivate # deavtivate virtualenv
   
   # comment everything inside databse in /github/official_website/mysite/settings.py   database = {  #everything commment out#  }, reason: you need to have your own vercel.com and mongodb.com free version account
   
   
   
   
   # Note the following steps is Optional, but helpful for testing
   
      # create free version account in mangodb.com, create your own database, modify everything inside database in /github/official_website/mysite/settings.py  ,  database = {  #modify me#  }
   
      # Reason: your modification may works well in local, but may crash once deploy on vercel, so you can create free account, test it by yourself
      # Download Vercel CLI follow guidance: https://vercel.com/docs/cli
      # create account on vercel
      vercel login
      # in order to test
      vercel      # preview "fake" deploy
      # copy the website link provided to you, paste it on browser
      
      
      
      
      # Reason: test your modification local by following command:
      python3 manage.py runserver         # make sure you are in /github/official_website/ directory
      # default local ip address is: http://127.0.0.1:8000/
   
   
   



Technical Details
===================



----------------------
Django
----------------------
Django is a web framework done by Python.



What is Project Structure?
--------------------------
There is a project, inside project there are many different apps. In our project, project name is official_website, apps are website pages, such as: official_website/home, official_website/subpages/about, official_website/subpages/contact...

Also, when first create project, there's a root app, in our project called official_website/mysite.



How is URL works?
--------------------------
Every app has an urls.py, the root one is official_website/mysite/urls.py. Django delieve the url to root first (official_website/mysite/urls.py), and then go to other app's urls.py based on "urlpatterns" inside urls.py.



Django frequently used Command
--------------------------
.. code:: python

  django-admin startproject official_website    # create a django proeject called official_website
  
  python3 manage.py startapp home   # create an app (official_website/home) inside the project

  python3 manage.py runserver      # start local server, default port: http://127.0.0.1:8000
  
  python3 manage.py makemigrations    # makemigrations first, and then migrate, Eric guess: setup something

  python3 manage.py migrate       # always makemigrations and migrate together

  python3 manage.py collectstatic     # move js,html,css file from project/app/static ----> project/static (root static folder)
  


----------------------
Vercel
----------------------
Vercel is cloud website hosting service. It is only free cloud service Mr. Eric can find, and we can use its free service.

Modification made on ut021.com will happen only by changing main branch.




Vercel frequently used Command
--------------------------
.. code:: python
  
  vercel        # testing, preview deploy, (not actually change the website)
  vercel --prod     # real deploy, change website



----------------------
MangoDB
----------------------
MangoDB is a Database. It is one of the DB(DataBase) which can integrate with both Django and Vercel, and MangoDB has free cloud service.



----------------------
Project Folder Structure and Explaination
----------------------
This folder structure is basic one, future web pages will be expanded based on this basic structure.


.. code:: python
   
 |official_webiste    # the project
 --|>.vercel     # auto generated by vercel, when you deploy it
   |>.vscode     # vscode setup folder  
   |>home        # home page of the website
   --|>__pycache__     # python become low level code, which called pycache
     |>migrations      # auto generated when you migrate
     |>static          # store static file, includes css,html,js used in home page
     |>subpages        # ex: ut021.com/others, in this case, others page is one of the subpage of home page (ut021.com/ this is home page)
     |>template        # has one or more html file
     --|home.html      # source code for home page, template can have multiple web pages, such as, different user sees different home page, then we may be have home1.html and home2.html
     |__init__       # every folder, subfolder should have "__init__", in order for django to understand
     |admin.py       # related to database
     |apps.py        # auto generated
     |models.py      # related to database
     |test.py        # test code
     |urls.py        # app's url, help django to understand "ut021.com/" should be here, and use home.html
     |views.py       # django first check urls.py, if django should come inside this app, django go to views.py, views.py runs home.html and some logic
   |>mysite     # root app for the project
   --|>__phcache__
     |__init__.py
     |asgi.py
     |models.py
     |setting.py    # setting for the project, many modification based on default (first created project)
     |urls.py       # root urls, django first receive string url from user, based on urlpatterns defined inside urls.py, django may go to home/urls.py
     |wsgi.py       # remember add "app = aplication" at the end
   |>static         # root static folder, stores all the css,html,js files, after collectstatic, all static files from subfolders will be moved to root statc folder
   |>staticfiles_build   #auto generated, when collectstatic
   |>subpages       # subpage in current app, for example: ut021.com/about, ut021.com/contact
   |.gitignore      # github will not put this files and folders mentioned inside .gitignore onto github.com
   |build_files.sh  # setup vercel cloud environment when deploy website
   |manage.py       # default file when create project, no need for modification
   |README.rst      # it is the file you are reading now
   |requirement.txt # the required package vercel need to download when deploying
   |vercel.json     # guidance for vercel to know what to do
   
   

----------------------
Eric's Journey: Walkthrough from Beginning to Finish SetUp
----------------------
！！！Note: The following steps is only edcational and testing purpose, it is not used for setup.

.. code:: python

   pip install virtualenvwrapper    # download virtual environment package for python
   
   virtualenv official_website_virtual_environ        # create virtual environment for official website

   source official_website_virtual_environ/bin/activate     # activate it
   
   pip install django djongo pymongo pytz       # install all the packages we need

   deactivate # deavtivate virtualenv

   cd github    # go to the directory where project will locate
    
   django-admin startproject official_website     # create project

   python3 manage.py startapp home  # create home page
   
   mkdir subpages static home/static home/templates home/subpages      # create all the folders we need
   
   touch build_files.sh requirements.txt vercel.json home/urls.py home/templates/home.html subpages/__init__.py .gitignore  # create all the files we need
   
   cd subpages
   
   python3 manage.py startapp about contact
   
   cd ..
   
   
   # Replace - /official_website/home/urls.py
   from django.urls import path
   from home.views import index
   urlpatterns = [
       path('', index),  # New Page path
   ]
   
   
   # Replace - /official_website/home/views.py
   from django.http import HttpResponse
   def index(request):
       return HttpResponse("Hello, world. You're at the polls index.")
       
       
   # Add and Modify - /official_website/mysite/settings.py
   DEBUG = False
   ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1',  'ut021.com', 'test-24eric.vercel.app']
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'subpages.about',
    'subpages.contact',
   ]
   DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'utm021',
           'ENFORCE_SCHEMA': False,
           'CLIENT': {
               'host': 'mongodb+srv://eric:eric@cluster0.1t3ruht.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE'
           }  
       }
   }
   import os
   STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

   
   # Replace - /official_website/mysite/urls.py
   from django.contrib import admin
   from django.urls import path, include
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('home.urls')),
       path('about/', include('subpages.about.urls')),
       path('contact/', include('subpages.contact.urls'))
   ]
   from django.conf import settings
   from django.conf.urls.static import static
   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   
   
   # Add - /official_website/mysite/wsgi.py
   app = application

   
   # Modify - official_website/subpages/about
   simialr to what Eric did in home
   
   
   # Modify - official_website/subpages/contact
   simialr to what Eric did in home
   
   
   # Replace - official_website/.gitignore - (Note: .gitignore may auto generate)
   /node_modules
   /.pnp
   .pnp.js
   # testing
   /coverage
   # production
   /build
   # misc
   .DS_Store
   .env.local
   .env.development.local
   .env.test.local
   .env.production.local
   npm-debug.log*
   yarn-debug.log*
   yarn-error.log*
   .vercel
   
   
   # Replace - official_website/build_files.sh
   pip install -r requirements.txt
   # python3.9 manage.py collectstatic    # Note: this command let vercel run for a very long time, may not need
   
   # Replace - official_website/requirements.txt
   pymongo==3.12.3
   Django==4.1.4
   djongo==1.3.6
   pytz==2022.7


   # create file official_website/vercel.json
   {
     "version": 2,
     "builds": [
       {
         "src": "mysite/wsgi.py",
         "use": "@vercel/python",
         "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
       },
       {
         "src": "build_files.sh",
         "use": "@vercel/static-build",
         "config": {
           "distDir": "staticfiles_build"
         }
       }
     ],
     "routes": [
       {
         "src": "/static/(.*)",
         "dest": "/static/$1"
       },
       {
         "src": "/(.*)",
         "dest": "mysite/wsgi.py"
       }
     ]
   }
   
   
   python3 manage.py runserver      # Optional, it is used for testing in local

   python3 manage.py makemigrations    # do it only first time

   python3 manage.py migrate      # do it only first time

   python3 manage.py collectstatic     # may not need to do it


Django Common Tag Syntax
===================
Comes from: https://docs.djangoproject.com/en/dev/topics/templates/#template-inheritance

.. code:: python
    
    # Tags
    {% csrf_token %}
    
    {% cycle 'odd' 'even' %}
    
    {% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %}
    
    # Filters
    {{ django|title }}
    
    # Comment
    {# this won't be rendered #}
    
    
    
    

Common Problem (Eric's Experience)
===================
.. code:: python

   Problem 1 - djongo is not one of four engine supported by django
   Solution - pip install pytz
   
   Problem 2 - deploy vercel, get message: serverless function crash
   Solution - double check the correction in files: vercel.json, requirements.txt, build_files.sh mysite/urls.py mysite/settings.py
   
   Problem 3 - deploy vercel, get message: not found
   Solution - double check the correction in vercel.json
   
   Problem 4 - django.core.exceptions.ImproperlyConfigured: Cannot import 'products'. Check that 'subpages.products.apps.ProductsConfig.name' is correct.
   Solution - If the app location is inside an subpage, for example app name is events, then change from name = 'events' to name = 'subpages.events'
   
   # Note: if you encounter any issues during setup, and you can not find solution by copy-paste error message on website, come to ask Eric ;)



Resource / Reference
===================
Django Official Website: https://www.djangoproject.com/

Django Official DOCS: https://docs.djangoproject.com/en/4.1/

Vercel Official Website: https://vercel.com/

Vercel Official DOCS: https://vercel.com/docs

Deploy Django Website in Vercel tutorial: https://jay-hale.medium.com/django-on-vercel-in-30-minutes-e69eed15b616

MangoDB Official Website: https://www.mongodb.com




Contribution Guidance
===================
In order to make the project easy maintain and extend in future. It is necessary to follow some common contribution guidance. 



----------------------
Comment and Documentation
----------------------
Whenever you made modification, cooment all of the necessary code in order for others and future teammates (including yourself) to easily and quickly undertstand what you did and your thought without looking at the code.

Once we publish new version of the website, update README.rst is necessary as well.




----------------------
Github and Git
----------------------
In order to contribute, first designa a plan or talk about the feature you want to work on with Eric, and then make a Dev branch based on main.

Once you finished your feature, make a pull request, and then other teammates will review your code, double check and test it before pushing into main branch.

As we know git is an version tracking package, whenever you commit your change to your branch, leave a clear but short comment will be very helpful.

We will always keep several stable version of website, just in case the new version crashed.



----------------------
Principles during Design and Development
----------------------
During the logic design process, using UML graph.

Tool for UML: https://app.diagrams.net/

During the development related to logic stuff, please following SOLID Principle, more details following: https://medium.com/mindorks/solid-principles-explained-with-examples-79d1ce114ace     or       https://www.geeksforgeeks.org/solid-principle-in-programming-understand-with-real-life-examples/




Future Planning
===================
3D engine: https://codeboje.de/2d-and-3d-game-and-rendering-engines-python/



Licence
===================
 Copyright © 2022, `IT Development Team in UT021 <https://github.com/24ERIC/official_website/>`_ Released under the [MIT License](LICENSE).



