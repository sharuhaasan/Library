# LibraryManagementSystem
Project name - LibraryManagement                                                               
Books - This Django app provides a REST API for managing User and Books in the LibraryManaging system.

### INSTALLATION
#### Clone the repository:
```bash
https://github.com/sharuhaasan/LibraryManagementSystem.git        
```
#### Navigate to the project directory:
```bash
cd LibraryManagement
```                               
#### Create a virtual environment:
```bash
python3 -m venv venv 
```                           
#### Activate the virtual environment:
```bash 
venv\Scripts\activate  
```                                
#### Install the dependencies:  
```bash
pip install -r requirements.txt
```                                  

#### Set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```
#### USAGE

settings.py                                   
models.py                                 
serializers.py                              
views.py                                                      
urls.py (Books)                                          
urls.py (LibraryManagement)                  
tests.py

##### Start the development server
```bash
python manage.py runserver
```

##### Access the API endpoints:

Create New user: POST /users/                      
List All users: GET /users/all/                  
Retrieve details of a specific user by ID: GET /users/<int:UserID>/

Create New book: POST /books/                       
List All books: GET /books/all/                                
Retrieve details of a specific book by ID: GET /books/<int:BookID>/         
Assign/Update book details: PUT /books/details/<int:Book_id>/                 

Borrow a book: POST /borrow/                           
(Update)Return a borrowed book: PUT /return/<int:pk>/                 
List All borrowed books: GET /borrowed-books/                     

##### SAMPLE API

http://127.0.0.1:8000/users/ -- (POST) To create new user                                             
http://127.0.0.1:8000/books/all/ -- (GET) Lists all existing books                                                           
http://127.0.0.1:8000/books/1/ -- (GET) To retrieve the details of existing book using BookID                                                   
http://127.0.0.1:8000/return/5/ -- (PUT) To Update the return date of borrowed book using Primary key                                            

##### RESPONSE
```bash
"POST /users/ HTTP/1.1" 201 Created                                                            
"GET /books/all/ HTTP/1.1" 200 OK                                       
"GET /books/1/ HTTP/1.1" 200 OK                      
"PUT /return/5/ HTTP/1.1" 200 OK          
```
##### TESTING
```bash
python manage.py test 
```
##### ERROR
```bash
If a user attempts to have another account using same mail id, the response will be:                                          

{
    "Email": [
        "user with this Email already exists."
    ]
}

"POST /users/ HTTP/1.1" 400 Bad Request
```