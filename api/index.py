from flask import Flask, json, render_template, request, jsonify
import requests
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/sendsms', methods=['POST'])
def send_sms():
    try:
        contact_number = request.form['contact_number']
        message = request.form['message']
        
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
            app.logger.error(f'Failed to send message. Status code: {response.status_code}, Response: {response.text}')
            return render_template('index.html', status='failure', message=f'Failed to send message. Status code: {response.status_code}', response=response.text, contact_number=contact_number, message_content=message)
    except Exception as e:
        app.logger.error(f'Error occurred: {str(e)}')
        return render_template('index.html', status='failure', message='An error occurred while sending the SMS.', error=str(e))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
