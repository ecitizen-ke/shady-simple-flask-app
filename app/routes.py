from . import home_bp


@home_bp.route("/")
def index():
    return "<h1>Index Page</h1>"
