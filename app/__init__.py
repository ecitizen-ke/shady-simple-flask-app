def home(myapp):
    @myapp.route("/")
    def index():
        return "<h1>Index Page</h1>"
