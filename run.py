from setup_routes import app, setup_routes

setup_routes()

if __name__ == "__main__":
    app.run(debug=True)