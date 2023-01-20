from flask import Flask, request, make_response
import qrcode
import io

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def qr_code():
    # Get the URL from the query string
    url = request.args.get('url')
    # Create a QR code image
    img = qrcode.make(url)
    
    # Save the QR code image to a buffer
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    
    # Create the response object
    response = make_response(buffer.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=QRcode.png'
    response.mimetype = 'image/png'
    return response

if __name__ == '__main__':
    app.run(debug=True)
