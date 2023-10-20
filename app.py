
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return open('index.html').read()

@app.route('/check_health', methods=['POST'])
def check_health():
    tenant_name = request.form['tenant']
    
    # Here, you'd generally call Microsoft Graph API to check for any disturbances
    # For demo purposes, let's assume the API returns a JSON object with health information
    # api_response = call_graph_api(tenant_name)
    
    # Mocking an API response for demonstration
    api_response = {
        'Azure': 'No Issues',
        'Microsoft 365': 'Minor Issues'
    }
    
    return jsonify(api_response)

if __name__ == '__main__':
    app.run(debug=True)
