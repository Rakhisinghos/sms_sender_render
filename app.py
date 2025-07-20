from flask import Flask, render_template, request, redirect, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        
        # Format phone number
        phone = phone.strip().replace(" ", "")
        if not phone.startswith('91'):
            phone = '91' + phone

        # Message content
        message = f"""Dear {name},
Your scholarship has arrived. Please report to the Student Section as soon as possible and pay your remaining fees. 
Otherwise, a penalty will be levied.

From:
Student Section
Chhattisgarh Institute of Technology (CGIT), Jagdalpur"""

        url = "https://www.fast2sms.com/dev/bulkV2"

        payload = {
            "sender_id": "FSTSMS",
            "message": message,
            "language": "english",
            "route": "q",
            "numbers": phone,
        }

        headers = {
            'authorization': "YOUR_FAST2SMS_API_KEY",
            'Content-Type': "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        return jsonify(response.json())

    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
