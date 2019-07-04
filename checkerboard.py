from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
## code below this line

# Level 1 - Render a Checkerboard
@app.route('/')
def index():
    return render_template("checkerboard.html", x=8, y=8)

# Level 1 - Render a Checkerboard
@app.route('/<x>/<y>/')
def index_x_y(x,y):
    return render_template("checkerboard.html", x=int(x), y=int(y))

# Level 3 - Render a Checkerboard w/ x many rows and y many columns
@app.route("/<int:n>/<int:x>/<color1>/<color2>")
def index_x_y_color(n, x, color1, color2):
    return render_template("checkerboard2.html", n = n, x = x, color1 = color1, color2 = color2)

## code above this line    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.