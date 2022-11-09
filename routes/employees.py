from app import app, db
from flask import render_template, request, redirect
from models.models import Employee, Plant


@app.route('/add-employee', methods=["POST", 'GET'])
def add_employee():
    if request.method == "POST":
        data = request.form
        try:
            employee = Employee(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                plant_id=int(data.get('plant_id'))
            )
            db.session.add(employee)
            db.session.commit()
        except:
            return 'This email already exist!'
        return redirect('/employees')
    else:
        employee = Employee.query.get(id)
        plants = Plant.query.all()
        return render_template("add_employee.html", plants=plants, employee=employee)

@app.route('/employees')
def employees_home():
    employees = Employee.query.all()
    return render_template("employees-list.html", employees=employees)


@app.route('/edit-employee/<int:id>')
def edit_employee(id):
    employee = Employee.query.get(id)
    plants = Plant.query.all()
    return render_template('add_employee.html', employee=employee, plants=plants)


@app.route('/update-employee/<int:id>', methods=["POST"])
def update_employee(id):
    employee = Employee.query.get(id)
    employee.first_name = request.form.get('first_name')
    employee.last_name = request.form.get('last_name')
    employee.plant_id = request.form.get('plant_id')
    employee.email = request.form.get('email')
    db.session.add(employee)
    db.session.commit()
    return redirect('/employees')


# @app.route('/save-employee', methods=['POST'])
# def save_employee():
#     first_name = request.form.get('first_name')
#     last_name = request.form.get('last_name')
#     email = request.form.get('email')
#     plant_id = request.form.get('plant_id')
#     employee = Employee(first_name=first_name, last_name=last_name, email=email, plant_id=plant_id)#ми створили новий обєкт, тобто ми зробили інсерт(insert) в базу даних
#     db.session.add(employee)#тут ми добавляємо елемент (employee) у трансакцію
#     db.session.commit()
#     return redirect('/employees-list')


@app.route('/delete-employee/<int:id>')
def delete_employee(id):
    employee = Employee.query.get(id)#get бере конкретний обєкт у нашому випадку по id
    db.session.delete(employee)
    db.session.commit()
    return redirect('/employees')