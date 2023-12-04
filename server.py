from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nextdoor.db'
db = SQLAlchemy(app)

class Community(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    community_id = db.Column(db.Integer, db.ForeignKey('community.id'), nullable=False)
    community = db.relationship('Community', backref=db.backref('users', lazy=True))

@app.route('/api/communities')
def get_communities():
    communities = Community.query.all()
    return jsonify([{'id': community.id, 'name': community.name} for community in communities])

@app.route('/api/community/<int:community_id>')
def get_community(community_id):
    community = Community.query.get(community_id)
    users = User.query.filter_by(community_id=community.id).all()
    return jsonify({'community': {'id': community.id, 'name': community.name},
                    'users': [{'id': user.id, 'username': user.username} for user in users]})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
