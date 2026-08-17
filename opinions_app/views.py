"""Представления приложения."""
from random import randrange

from flask import abort, redirect, render_template, url_for

from opinions_app import app, db
from opinions_app.forms import OpinionForm
from opinions_app.models import Opinion


@app.route('/')
def index_view():
    """Отображает случайное мнение о фильме."""
    quantity = Opinion.query.count()

    if not quantity:
        abort(500)

    offset_value = randrange(quantity)
    opinion = Opinion.query.offset(offset_value).first()

    return render_template('opinion.html', opinion=opinion)


@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    """Отображает и обрабатывает форму добавления мнения."""
    form = OpinionForm()

    if form.validate_on_submit():
        opinion = Opinion(
            title=form.title.data,
            text=form.text.data,
            source=form.source.data
        )

        db.session.add(opinion)
        db.session.commit()

        return redirect(url_for('opinion_view', id=opinion.id))

    return render_template('add_opinion.html', form=form)


@app.route('/opinions/<int:id>')
def opinion_view(id):
    """Отображает мнение о фильме по идентификатору."""
    opinion = Opinion.query.get(id)
    return render_template('opinion.html', opinion=opinion)
