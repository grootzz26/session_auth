# session_auth

**Project Title:**


  Session Authentication (Cache Based)
  
  
  
**Project Description:**

 An app that demonstrates the session authentication using redis-cache.
 
 Used Technologies in this project:
 
    1.python
 
    2.django
 
    3.redis
 
    4.mysql
    
    
**App Working Logic**

1. Initially we need to create device_id that will demonstrates the client_key.

2. this client_key make ensure that user is valid or not.

3. we creates the session object for the client_key(client).

4. store the session objects into cache(redis)

5. get the valid session for the user from cache when user wants to login into the app.
    
    
**Install and Run My App Locally**

1. create and install virtualenv in your project.

2. Install all the required packages in your venv.

    use this cmd: pip install -r requirements.txt
    
3. run the app in your local using python manage.py migrate && python manage.py runserver. 

**Table Mappings:**

User --> Device --> Session

  
 
  
