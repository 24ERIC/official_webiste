"""""""""""""""""
HELP - Vercel Django Deploy Setting
"""""""""""""""""



...........
UTM021 IT Development Team
...........
.. contents:: Overview
   :depth: 3
   

===================
Resource / Reference
===================
Bug - Sucess Deploy Django on Vercel, but website show 404: https://github.com/vercel/vercel/issues/7678




===================
Basic Setting - Django Default Package + An example App
===================



----------------------
Create - /folder/requirements.txt
----------------------
.. code:: python

  Django==4.1.4



----------------------
Create - /folder/vercel.json
----------------------
.. code:: python

  {
    "builds": [{
        "src": "folder/wsgi.py",    
        "use": "@vercel/python",    # Modified @vercel/python
        "config": { "maxLambdaSize": "15mb", "runtime": "python3.9"}    # Modified python3.9
    }],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "vercel_app/wsgi.py"
        }
    ]
   }


----------------------
Add - /folder/App/wsgi.py
----------------------
.. code:: python
   
   # Add this line somewhere in file
   app = application



----------------------
Add - /folder/settings.py
----------------------
.. code:: python
   
   ... 
   ALLOWED_HOSTS = ['.vercel.app']     # Add '.vercel.app'
   
   ...
   INSTALLED_APPS = [
    ...
    'New Page',       # Add New Page here
   ]
   
   ...
   DATABASES = {}    # ??? - Vercel may only allow certain database
   


===================
Every time add new Page
===================
Modify App urls, and New Pages urls (for path) and views (for website content)
   


----------------------
Modify - /folder/New Page/
----------------------
.. code:: python



----------------------
Add - /folder/App/urls.py
----------------------
.. code:: python

   # Make imports include
   from django.urls import path, include
   
   urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('New Page.urls')),  # Add this page to App url path
   ]



----------------------
Create, Add - /folder/New Page/urls.py
----------------------
.. code:: python

   from django.urls import path
   from example.views import index

   urlpatterns = [
       path('', index),  # New Page path
   ]



----------------------
Create, Add - /folder/New Page/views.py
----------------------
.. code:: python

   from datetime import datetime
   from django.http import HttpResponse

   def index(request):        # the page, conponent want to display on website
       now = datetime.now()
       html = f'''
       <html>
           <body>
               <h1>Hello from Vercel!</h1>
               <p>The current time is { now }.</p>
           </body>
       </html>
       '''
       return HttpResponse(html)
       
       
       
       
       






..
   Note: Please follow the following templates

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
