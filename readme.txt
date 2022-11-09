HOME WORK: Create api endpoints for plant crud (CREATE, READ, UPDATE, DELETE)
 
 1) Open project
 2) Create file .env
 3) Insert next information in file .env :
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@database:3306/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    PYTHONUNBUFFERED=1
 
 4) install all aplications from file: requirements.txt 
 5) run container: sudo docker-compose up --build
 6) enter in our container: sudo docker-compose exec web bash
 7) enter next string: flask db upgrade
 
