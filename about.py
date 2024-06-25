def register_routes(app):
    @app.route("/about/us")
    def aboutus():
        return "This is my about section"