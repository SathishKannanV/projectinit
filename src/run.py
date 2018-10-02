from src.app import app
import os

port = int(os.environ.get('PORT', 5000))
app.run(debug=app.config['DEBUG'], port=port)