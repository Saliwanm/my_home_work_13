from app import app, db
from flask import render_template, request, session, redirect
from models.models import Plant, User
from sqlalchemy import or_
import hashlib


@app.route("/")
def main():
    plants = Plant.query.order_by(Plant.id.desc()).all()#allбере всі обєкти
    # plants = Plant.query.filter(Plant.location == "Zrini 65")#filter бере по фільтру в нашому випадку в класі Plant  по локації (location) - Zrini 65
    user = None
    if session.get("user", False):
        user = User.query.get(session.get('user'))
    return render_template('index.html', plants=plants, user=user)


@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        data = request.form
        user = User(
            username=data.get('username'),
            email=data.get('email'),
            password=hashlib.md5(data.get('password').encode()).hexdigest(),
            first_name=data.get('first_name'),
            last_name=data.get('last_name')
        )
        temps = User.query.all()
        flag = False
        for temp in temps:
            if user.email == temp.email:
                flag = True
            else:
                pass

        if flag == True:
            some_text = 'Sorry, but this email already exist! Try again and change your email...'
            return render_template('sign-up.html', some_text=some_text)
        else:
            db.session.add(user)
            db.session.commit()
            session['user'] = user.id
            return redirect('/')
    else:
        return render_template('sign-up.html')


@app.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        user = User.query.filter(or_(User.email == request.form.get('email'), User.username == request.form.get('email'))).first()
        if user is not None:
            if user.password == hashlib.md5(request.form.get("password").encode()).hexdigest():
                session["user"] = user.id
        return redirect('/')
    else:
        return render_template('sign-in.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
