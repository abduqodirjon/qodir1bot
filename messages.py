
import requests

def send(chat_id, text):
	token = "5269458930:AAFkc7XFJUoLCiz8kMM_docwSgAdOYJl7ME"
	
	url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
	results = requests.get(url_req)
	return results.json()