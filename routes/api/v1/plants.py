from app import api, db
from flask_restful import Resource
from flask import request
from models.models import Plant as PlantModel


class PlantsResource(Resource):
    def get(self):
        filter = request.args
        # print(filter)
        # plants = PlantModel.query.all()
        query = PlantModel.query
        if len(filter) < 1:
            plants = query.all()
        else:
            for key in filter.keys():
                print(key)
                plants = query.filter(getattr(PlantModel, key) == filter.get(key))

        plant_data = []
        for plant in plants:
            plant_data.append(plant.serialize_plant())
        return plant_data

    def post(self):
        data = request.json
        plant = PlantModel(
            title=data.get('title'),
            location=data.get('location')
        )
        db.session.add(plant)
        db.session.commit()
        return plant.serialize_plant()

    def delete(self):
        data = request.json
        print(data['id'])
        plant = PlantModel.query.get(data['id'])
        db.session.delete(plant)
        db.session.commit()
        return "This plant delete"


class SinglePlantResource(Resource):
    def get(self, id):
        plant = PlantModel.query.get(id)
        return plant.serialize_plant()

    def put(self,id):
        data = request.json
        plant = PlantModel.query.get(id)
        plant.title = data.get("title", plant.title)
        plant.location = data.get("location", plant.location)
        db.session.add(plant)
        db.session.commit()
        return plant.serialize_plant()


api.add_resource(PlantsResource, '/api/v1/plants')
api.add_resource(SinglePlantResource, '/api/v1/plants/<int:id>')