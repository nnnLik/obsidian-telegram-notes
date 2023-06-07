from services.database import db


class Account(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer(), primary_key=True)
    tg_id = db.Column(db.Integer())
    joined_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
