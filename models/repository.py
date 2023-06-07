from services.database import db


class Repository(db.Model):
    __tablename__ = 'repositories'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    repo_owner = db.Column(db.String(255))
    repo_name = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    joined_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
