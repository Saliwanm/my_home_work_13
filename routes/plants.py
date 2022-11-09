from app import app, db
from flask import render_template, request, redirect
from models.models import Plant, Employee


@app.route('/add-plant')
def add_plant():
    employees = Employee.query.all()
    return render_template("add_plant.html", employees=employees)

@app.route('/plant-info/<int:id>')
def plant_info(id):
    # plant = Plant.query.all()  # allбере всі обєкти
    plante = Plant.query.filter(Plant.id == str(id))#filter бере по фільтру в нашому випадку в класі Plant  по локації (location) - Zrini 65
    return render_template("plant_info.html", plante=plante)


@app.route('/save-plant', methods=['POST'])
def save_plant():
    name = request.form.get('name')
    location = request.form.get('location')
    plant = Plant(title=name, location=location)#ми створили новий обєкт, тобто ми зробили інсерт(insert) в базу даних
    db.session.add(plant)#тут ми добавляємо елемент (plant) у трансакцію
    for employee_id in request.form.getlist('employees'):
        employee = Employee.query.get(int(employee_id))
        employee.plant_id = plant.id
        db.session.add(employee)
    db.session.commit()
    return redirect('/')


@app.route('/delete-plant/<int:id>')
def delete_plant(id):
    plant = Plant.query.get(id)#get бере конкретний обєкт у нашому випадку по id
    db.session.delete(plant)
    db.session.commit()
    return redirect('/')


@app.route('/edit-plant/<int:id>')
def edit_plant(id):
    plant = Plant.query.get(id)
    employees = Employee.query.all()
    return render_template('add_plant.html', plant=plant, employees=employees)


@app.route('/update-plant/<int:id>', methods=["POST"])
def update_plant(id):
    plant = Plant.query.get(id)
    plant.title = request.form.get('name')
    plant.location = request.form.get('location')
    db.session.add(plant)
    for employee_id in request.form.getlist('employees'):
        employee = Employee.query.get(int(employee_id))
        employee.plant_id = plant.id
        db.session.add(employee)
    db.session.commit()
    return redirect('/')