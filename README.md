1) Create a virtual environment.
2) Create DB "user_database" to MongoDB
3) python -m pip install -r requirements.txt
4) python manage.py makemigrations
5) python manage.py migrate
6) For Postman URL: http://localhost:8000/user/
7) method: POST
8) JSON:
{
  "email": "devselit@gmail.com",
  "username": "root",
  "password": "pass"
}
