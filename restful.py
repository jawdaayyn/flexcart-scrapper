from flask import Flask, jsonify, request #import objects from the Flask model
import scrapper
app = Flask(__name__) #define app using Flask
	
def scrape(url):
    brand = scrapper.main(url)
    return brand

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'working !'})

@app.route('/scrap', methods=['POST'])
def addOne():
    url = {'url' : request.json['url']}
    data = scrape(url['url'])
    print(data)
    return (data)

if __name__ == '__main__':
	app.run(debug=True, port=5000) #run app on port 5000 in debug mode