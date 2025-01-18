from flask import Flask, json, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/sendsms', methods=['POST'])
def send_sms():
    contact_number = request.form['contact_number']
    message = request.form['message']
    
    # Replace with your PhilSMS API token
    api_token = '870|h05YLghELQ8xSwBYKosPFx3w6svYs4EckHpQvsf9'
    
    url = 'https://app.philsms.com/api/v3/sms/send'
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    payload = {
        'recipient': contact_number,
        'sender_id': 'PhilSMS',  # Replace with your actual sender ID
        'type': 'plain',
        'message': message
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return render_template('index.html', status='success', message='SMS sent successfully!', contact_number=contact_number, message_content=message)
    else:
        return render_template('index.html', status='failure', message=f'Failed to send message. Status code: {response.status_code}', response=response.text, contact_number=contact_number, message_content=message)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
