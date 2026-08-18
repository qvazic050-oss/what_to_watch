"""Обработчики ошибок приложения."""
from flask import render_template

from opinions_app import app, db


@app.errorhandler(500)
def internal_error(error):
    """Обрабатывает ошибку 500."""
    db.session.rollback()
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(error):
    """Обрабатывает ошибку 404."""
    return render_template('404.html'), 404
