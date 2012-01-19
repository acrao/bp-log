from bp_log import app

@app.route('/')
def home():
	return "Welcome to BP Log"