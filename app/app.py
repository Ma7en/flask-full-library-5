from app import create_app

if __name__ == "__main__":
    app = create_app("dev")
    app.run(debug=True)
    # app.run(debug=app.config["DEBUG"])
