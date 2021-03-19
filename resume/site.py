from flask import Flask, render_template, jsonify
from .helper import get_user


app = Flask(__name__)

@app.errorhandler(Exception)
def error_500(exception):
    return jsonify({"error": str(exception)}), 500, {'Content-Type': 'application/json'}

@app.route('/')
def home(name=None):
	try:
		return render_template('page.html', error=False)
	except Exception as e:
		return f"ERROR {e}"

@app.route('/<username>')
def main(username):
	if data:=get_user(username):
		try:
			return render_template('index.html', data=get_user(username))
		except Exception as e:
			return f"ERROR {e}"
	else:
		return render_template('page.html', error=True)


@app.route('/error/<username>')
def error(username):
	if data:=get_user(username):
		try:
			render_template('index.html', data=get_user(username))
			return jsonify({
				"status": "Success"
				})
		except Exception as e:
			return jsonify({
				"status": "Error",
				"msg": e
				}), 500, {'Content-Type': 'application/json'}
	else:
		return jsonify({
				"status": "Error",
				"msg": "Resume not found in master branch, Make sure your filename should be 'RESUME.json' "
				"and it should be in master branch"
				}), 500, {'Content-Type': 'application/json'}