from flask import Blueprint, jsonify
from web.transport import pushMessage

library = Blueprint('library', 'library', url_prefix='/library')
from web.library import manageBooks