from flask import Flask, render_template

# flask by default looks for index files in 'templates'
# template_folder argument is used to change the default folder
app = Flask(__name__, template_folder= 'website', static_folder='website/images')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    