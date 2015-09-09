import os
import uuid
import Image
from flask import Flask


app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"

COLOR = GREEN

@app.route('/')
def hello():


    return """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="white">Hi, I'm GUID:<br/>
    {}</br>


    </center>

    </body>
    </html>
    """.format(COLOR,my_uuid,)
    
    

if COLOR==GREEN
    	</center>
    	image=Image.open('/Users/marquj5/hello-python/tmnt.png').show()

if COLOR==BLUE
	</center>
image=Image.open('/Users/marquj5/hello-python/spongebob.jpg').show()


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))
