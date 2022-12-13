"""""""""""""""""
HELP - Django Commands
"""""""""""""""""



...........
UTM021 IT Development Team
...........
.. contents:: Overview
   :depth: 3
   

===================
Resource / Reference
===================
Django Official Docs Website: https://docs.djangoproject.com/en/4.1/intro/tutorial01/
Vercel CLI Commands: https://vercel.com/docs/cli
Deploy Django Website in Vercel tutorial: https://jay-hale.medium.com/django-on-vercel-in-30-minutes-e69eed15b616




===================
$ runserver
===================
.. code:: sh

  $ python3 manage.py runserver      # start local server, default port: http://127.0.0.1:8000
  $ python3 manage.py runserver 8080    # change port
  $ python3 manage.py runserver 0.0.0.0:8000    # change IP



===================
Create App
===================
After following the instruction below, the easy "polls" app finish and can be tested properly.

.. code:: sh

  $ python manage.py startapp polls    # Create an app --- "polls"
  
  
  
----------------------
Edit - polls/views.py
----------------------
.. code:: python

  from django.http import HttpResponse
   def index(request):
       return HttpResponse("Hello, world. You're at the polls index.")
  

----------------------
Edit - polls/urls.py
----------------------
.. code:: python

   from django.urls import path

   from . import views

   urlpatterns = [
       path('', views.index, name='index'),
   ]
  
  
  
----------------------
Edit - mysite/urls.py
----------------------
.. code:: python

   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('polls/', include('polls.urls')),
       path('admin/', admin.site.urls),
   ]



----------------------
Key - Keyword
----------------------
.. code:: python
   
	path()	# route, view, kwargs, name
				# EX - route - path('polls/', ....),
				# EX - view - path(.... , include('polls.urls')),
				# EX - kwargs - ?
				# EX - name - ?
				
	include()		# allows referencing other URLconfs
						# should always use it !
						# EX - path(.... , include('polls.urls')),
	
	










..
   Note: Plase Follow Templates!


===================
Template 1 - Section
===================
.. code:: sh

  $ 
  $ 
  $ 
  $ 
  
  
  
----------------------
Template 2 - SubSection
----------------------
.. code:: sh

  $ 
  $ 
  $ 
  $ 



Template 3 - SubSubSection
--------------------------
.. code:: sh

  $ 
  $ 
  $ 
  $ 
