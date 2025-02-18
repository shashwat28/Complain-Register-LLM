from flask import Flask, request, render_template
import complain_source_logging as csl # Import your Python code here, if needed

app = Flask(__name__)

# Route to display the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    location = request.form['location']
    
    # If needed, run your Python code using the value received
    # Example: Process the location with your Python code here
    print(f"Received location: {location}")
    
    # Assuming you want to run your code here with the location:
    result = csl.check_n_call(location)
    # result = some_function(location)  # Replace with your function
    print(result)
    # For demonstration, just echoing the location back
    return render_template('index.html', location=location, result=result)

if __name__ == '__main__':
    app.run(debug=True)
