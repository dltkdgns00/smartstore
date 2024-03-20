from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        amazon_url = request.form['amazon_url']
        productTitle = request.form['productTitle']
        leafCategoryID = request.form['leafCategoryID']
        
        # subprocess를 사용하여 main.py 실행, stdout과 stderr를 캡처
        try:
            result = subprocess.run(['python', 'main.py', amazon_url, productTitle, leafCategoryID],
                                    text=True, capture_output=True, check=True)
            output = result.stdout
            return render_template('result.html', result=output)
        except subprocess.CalledProcessError as e:
            error_message = e.stderr
            return render_template('error.html', error=error_message)

if __name__ == '__main__':
  app.run(debug=True)
