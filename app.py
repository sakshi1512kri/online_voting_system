from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Social media voting options stored in memory
voting_options = {
    'Facebook': 0,
    'Twitter': 0,
    'Instagram': 0,
    'LinkedIn': 0,
    'TikTok': 0
}

# Home route: Asks for the user's name and gives voting options
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form['name']
        selected_option = request.form['option']

        # Increment vote count for the selected option
        if selected_option in voting_options:
            voting_options[selected_option] += 1

        # Redirect to thank you page after voting
        return redirect(url_for('thank_you', name=user_name))

    # Render the voting page with options
    return render_template('index.html', options=voting_options)

# Thank you route after voting
@app.route('/thank-you/<name>')
def thank_you(name):
    return render_template('thank_you.html', user_name=name)

# Results route to show voting results
@app.route('/results')
def results():
    return render_template('results.html', options=voting_options)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
