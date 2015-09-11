import os
import uuid
import redis
import json
import newrelic.agent
from flask import Flask

newrelic.agent.initialize()


app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"

COLOR = GREEN

rediscloud_service = json.loads(os.environ['VCAP_SERVICES'])['rediscloud'][0]
credentials = rediscloud_service['credentials']
r = redis.Redis(host=credentials['hostname'], port=credentials['port'], password=credentials['password'])




@app.route('/')
def hello():


    r.incr('HITCOUNT')
    PAGEHITS = r.get('HITCOUNT')

    PAGEHITSINT = int(PAGEHITS)

    if (PAGEHITSINT%2==0):
        COLOR=GREEN

    if (PAGEHITSINT%2!=0):
        COLOR=BLUE

    if COLOR==GREEN:
        myimage='<img src="http://teenagemutantninjaturtles.com/wp-content/uploads/2013/03/Ninja-Turtles-TMNT-Pizza.jpg">'

    if COLOR==BLUE:
        myimage='<img src="http://i.imgur.com/ebbcdV9.png">'

    return """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="white">Hi, I'm GUID:<br/>
    {}</br>

    <center><h1><font color="white">PAGE HITS:<br/>
    {}</br>

    <center>
    {}</br>

    </body>
    </html>
    """.format(COLOR,my_uuid,PAGEHITS,myimage)




if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))
