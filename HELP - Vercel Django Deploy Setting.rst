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



===================
Every time add new Page
===================



----------------------
Modify - /folder/App/urls.py
----------------------
.. code:: python

   # Make imports include
   from django.urls import path, include
   
   urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('New Page.urls')),  # Add this page to App url path
   ]
   


----------------------
Modify - /folder/New Page/
----------------------
.. code:: python





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
