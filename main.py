from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feed_realtime.db'
db = SQLAlchemy(app)

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100))
    content = db.Column(db.String(300))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

connected = []

def connect(username):
    connected.append(username)

def publish(username, content):
    feed = Feed(
        username=username,
        content=content
    )

    db.session.add(feed)
    db.session.commit()

    for user in connected:
        print(f"Realtime update for {user}")

with app.app_context():
    db.create_all()

    connect("Ali")
    connect("Vali")

    publish("Jahongir", "New post 😎")
