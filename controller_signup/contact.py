def register_routes(app):
    @app.route("/contact")
    def contact():
        return 'This is my contact page'