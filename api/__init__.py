from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ARRAY, String
from flask_graphql import GraphQLView
from graphene import Schema, ObjectType, Field
from graphene_sqlalchemy import SQLAlchemyObjectType

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:postgres@localhost/test_sql"
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello world'


class UserModel(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(Integer)
    tags = Column(ARRAY(String))


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


class Query(ObjectType):
    user = Field(User)


schema = Schema(query=Query)

app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
