def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    print(type(texts))
    for text in texts:
        print('\n"{}"'.format(text.description))
        if (text.description=="TAX" ) :
            flag=1
            print("PAN Detected")
            break
		
        if(text.description=="AADHAR") :
            print("AADHAR Detected")
            flag=2
            break
			
    
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
		
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\SG0304986\\minor\\final\\scanning_qrcode\\abcd-0e0347fa3ddb.json"
		
detect_text("C:\\Users\\SG0304986\\minor\\final\\scanning_qrcode\\Capture.JPG")