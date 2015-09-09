import os
import uuid
from flask import Flask


app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"

COLOR = GREEN

@app.route('/')
def hello():

    if COLOR==GREEN:
        myimage='<img src="http://teenagemutantninjaturtles.com/wp-content/uploads/2013/03/Ninja-Turtles-TMNT-Pizza.jpg">'

    return """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="white">Hi, I'm GUID:<br/>
    {}</br>

    {}
    </center>

    </body>
    </html>
    """.format(COLOR,my_uuid,myimage)


    

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))
