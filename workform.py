from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


class WorkForm(FlaskForm):
    job_title = StringField('Job Title')
    team = StringField('Team Leader id')
    work_size = StringField('Work Size')
    collaborators = StringField('Collaborators')
    remember_me = BooleanField('Is job finished')
    submit = SubmitField('Submit')