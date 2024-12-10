from . import db

class Equipe(db.Model):
    __tablename__ = 'equipes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Evento(db.Model):
    __tablename__ = 'eventos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Pontuacao(db.Model):
    __tablename__ = 'pontuacao'
    id = db.Column(db.Integer, primary_key=True)
    id_equipe = db.Column(db.Integer, db.ForeignKey('equipes.id'), nullable=False)
    id_evento = db.Column(db.Integer, db.ForeignKey('eventos.id'), nullable=False)
    pontos = db.Column(db.Integer, nullable=False)

    equipe = db.relationship('Equipe', backref='pontuacoes')
    evento = db.relationship('Evento', backref='pontuacoes')
