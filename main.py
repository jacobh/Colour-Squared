from flask import Flask, make_response
from PIL import Image
# if using pypy this will need to be changed
from cStringIO import StringIO

app = Flask(__name__)

@app.route('/<int:width>/<int:height>/<color>')
def show_color_tile(width, height, color):
	# get color tuple
	color_tuple = (int(color[:2], 16), int(color[2:4], 16), int(color[4:6], 16))

	image = Image.new('RGB', (width,height), color_tuple)

	# save image and then extract the string
	buf = StringIO()
	image.save(buf, format='PNG')
	response = make_response(buf.getvalue())

	# clean up
	buf.close()
	del image

	response.mimetype = 'image/png'
	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)