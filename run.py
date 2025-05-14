from flask_app import create_app

# Vercel needs this
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)