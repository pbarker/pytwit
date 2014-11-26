from twython import TwythonStreamer


class MyStreamer(TwythonStreamer): 

	def on_success(self, data): 

        	if 'text' in data: 

                	print data


	def on_error(self, status_code, data): 

                print status_code
