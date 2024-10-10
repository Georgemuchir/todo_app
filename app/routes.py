from flask import Blueprint, render_template, request, redirect, url_for
from .models import Task
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@bp.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('main.index'))
