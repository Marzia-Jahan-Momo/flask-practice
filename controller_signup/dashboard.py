def register_route(app):
    @app.route("/dashboard")
    def dashboard():
        return "This is my dashboard"