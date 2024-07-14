# RANDOM
THIS IS THE REPO OF FRONTEND (REHBAR) DEVELOPER AND BACKEND DEVELOPER TRIES TO INTEGRATE EACH OTHER WORK USING API's
**TO START**
BRO SEE LIst OF API ARE :
SERVER : localhost:3000
ENDPOINTS : 
1. **_"formslist"_**                             #will show you json reponse of forms data.. available manipulations : GET AND POST
2. **_"formslist/< int:pk >"_**            #will show you data of a particular id ..to get of id 1 end point will be "formslist/1" available manipulations : 
   GET, PUT AND DELETE
 4. **_"users"_**  #will show you json response of the login users... Data it contain you directly see using this json api.. and can make signup and signin page as per the data


_TO FETCH THEIR DATA YOU MUST USE  **"GET"** request_ 
_TO UPDATE THE DATA YOU MUST USE  **"POST"** request_ 



STARTUP :
1. IF already created your super user then kindly login at endpoint "admin" and then proceed working... 
2. IF WANNA START COMPLETELY NEW .... 
        1. FORK MY REPOSITORY
        2. Make a directory in your File explorer
        3. OPEN YOUR TERMINAL / CMD navigate to your newly made directory
        4. USE THIS FOLLOWING COMMANDS TO PERFECTLY CLONE THE REPOSITORY AND CAN WORK WITH ME 

-   ` git init ` 
-  `git clone <your repository link>`
- `git remote add origin <your repository link>`
- `git checkout -b main`
- `git pull origin main`
5. Now to run the backend server:

- `cd backend ` 
- `pip install -r requirements.txt`   if macbook user `pip3 install -r requirements.txt`
- `python manage.py makemigrations`    if macbook user `python3 manage.py makemigrations`
- `python manage.py migrate`    if macbook user `python3 manage.py migrate`
- `python manage.py createsuperuser`  if macbook user `python3 manage.py createsuperuser`
- ENTER YOUR CREDENTIALS... 
- `python manage.py runserver`    if macbook user `python3 manage.py runserver`

6. go to endpoint admin .. localhost:8000/admin and login using your super id credentials 
7. NOW YOU CAN ACCESS ALL API's
