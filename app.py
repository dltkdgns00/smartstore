from flask import Flask, render_template, request, jsonify
import subprocess
import json

def load_category_data(filepath):
  categories = []
  with open(filepath, 'r', encoding='utf-8') as file:
    for line in file:
      category = json.loads(line.strip())
      categories.append(category)
  return categories

app = Flask(__name__)
categories = load_category_data('./디지털,가전 카테고리.csv')  # CSV 파일 경로 지정

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    amazon_url = request.form['amazon_url']
    productTitle = request.form['productTitle']
    productPrice = request.form['productPrice'] # productPrice 값을 추출
    leafCategoryID = request.form['selectedCategoryId']
    
    # subprocess를 사용하여 main.py 실행, stdout과 stderr를 캡처
    try:
      result = subprocess.run(['python3', 'main.py', amazon_url, productTitle, productPrice, leafCategoryID],
                              text=True, capture_output=True, check=True)
      output = result.stdout
      return render_template('result.html', result=output)
    except subprocess.CalledProcessError as e:
      error_message = e.stderr
      return render_template('error.html', error=error_message)

@app.route('/search_category')
def search_category():
  query = request.args.get('query', '').lower()
  results = [cat for cat in categories if query in cat['name'].lower() and cat['last'] == "True"]
  return jsonify(results[:5])  # 상위 5개 결과만 반환


if __name__ == '__main__':
  app.run(debug=True)
