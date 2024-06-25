def resgister_routes(app):
    @app.route("/")
    def homepage():
        return "This is my homepage"
