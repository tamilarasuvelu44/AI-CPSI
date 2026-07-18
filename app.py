from backend.app import app, seed_data

if __name__ == "__main__":
    # Do not run seeding here to avoid DB initialization issues in some environments.
    # Seeding can be performed manually or by running backend.app as a module when needed.
    app.run(debug=True)
