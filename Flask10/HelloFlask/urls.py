
from flask import url_for
import HelloFlask.views
urlpatterns = [
    url_for('',HelloFlask.views.qiren, name='qiren'),
    url_for('',HelloFlask.views.about, name='about'),
]

