from flask import Flask, request, jsonify
from mongo_me import db_me
from uuid import uuid4
import time





class Director(db_me.DynamicDocument):
    pass

class Cast(db_me.DynamicEmbeddedDocument):
    pass


class Imdb(db_me.EmbeddedDocument):
    imdb_id = db_me.StringField()
    rating = db_me.DecimalField()
    votes = db_me.IntField()


class Movie(db_me.Document):
    title = db_me.StringField(required=True)
    year = db_me.IntField()
    rated = db_me.StringField()
    director = db_me.ReferenceField(Director)
    cast = db_me.EmbeddedDocumentListField(Cast)
    poster = db_me.FileField()
    imdb = db_me.EmbeddedDocumentField(Imdb)

    def to_dict(self):
        print(jsonify(self.objects))
        return self.objects.__dict__



def get_movies():
    page = int(request.args.get('page',1))
    limit = int(request.args.get('limit',10))
    movies = Movie.objects.paginate(page=page, per_page=limit)
    return jsonify([movie for movie in movies.items]), 200


# @app.route('/movies/<id>')
# def get_one_movie(id: str):
#     movie = Movie.objects(id=id).first()
#     return jsonify(movie), 200


def get_one_movie(id: str):
    movie = Movie.objects.first_or_404(id=id)
    return movie.to_dict(), 200


def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    return jsonify(movie), 201
