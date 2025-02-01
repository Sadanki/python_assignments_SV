import configparser
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def read_config(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        data = {
            'Database': {
                'host': config.get('Database', 'host'),
                'port': config.get('Database', 'port'),
                'username': config.get('Database', 'username'),
                'password': config.get('Database', 'password')
            },
            'Server': {
                'address': config.get('Server', 'address'),
                'port': config.get('Server', 'port')
            }
        }
        # Save data as JSON
        with open('config_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return data
    except (configparser.NoSectionError, configparser.NoOptionError, FileNotFoundError) as e:
        print(f"Error reading configuration file: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config', methods=['GET'])
def get_config():
    try:
        with open('config_data.json', 'r') as json_file:
            data = json.load(json_file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({'error': 'Configuration data not found'}), 404

if __name__ == '__main__':
    config_file_path = 'config.ini'
    config_data = read_config(config_file_path)
    if config_data:
        app.run(host='0.0.0.0', port=5000)
    else:
        print("Failed to start the server due to configuration error.")
