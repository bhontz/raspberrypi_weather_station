import sys, Adafruit_DHT, time
from wsgiref.simple_server import make_server
 
html = """
<html>
<style>
    body {font-family: Arial, sans-serif; font-size: 96px;}
</style>
<body>
    <p align="center">Time: %s</p>
    <p align="center">Temp: %s</p>
    <p align="center">Humidity: %s</p>
</body>
</html>
"""
 
def application(environ, start_response):
 
    sensor = Adafruit_DHT.DHT22
    pin = 17  # The Raspberry Pi GPIO PIN we elected to use!
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temperature = (temperature * 9.0 / 5.0) + 32.0  # conversion from Celsius to Fahrenheit
 
    response_body = html % (time.strftime("%H:%M:%S", time.localtime()), "%0.1f" % temperature, "%0.1f" % humidity)
    
    status = '200 OK'
    
    response_headers = [('Refresh', '5'), ('Content-Type', 'text/html'),
                   ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    
    return [response_body]
 
if len(sys.argv) < 2 or sys.argv[1] == None or sys.argv[1] == "" :
    print "Usage: %s IP_ADDRESS_OF_Raspberry_Pi" % sys.argv[0]
    sys.exit(0)
 
httpd = make_server(sys.argv[1], 8051, application)
httpd.serve_forever()
