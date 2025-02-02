import os
import dotenv
from atproto import Client, models, client_utils

IMAGE_PATH = 'mosaic.png'
IMAGE_MIMETYPE = 'image/png'
IMAGE_ALT_TEXT = "1. #25 The Dark Side of the Moon (Pink Floyd); 2. #24 Room on Fire (The Strokes); 3. #22 The Wilderness (Explosions in the Sky); 4. #19 Low (2017 remaster) (David Bowie); 5. #19 xx (The xx); 6. #18 Turn on the Bright Lights (Interpol); 7. #18 Is This It (The Strokes); 8. #17 Lift Your Skinny Fists Like Antennas to Heaven (Godspeed You! Black Emperor); 9. #15 Wish You Were Here (Pink Floyd)"

def send_post():
    client = Client()
    client.login(os.getenv('BSKY_HANDLE'), os.getenv('BSKY_PASSWORD'))

    client.send_post(client_utils.TextBuilder().tag('teste', 'teste').text('olaaa'))    

    # with open(IMAGE_PATH, 'rb') as f:
    #     img_data = f.read()

    #     upload = client.upload_blob(img_data)
    #     images = [models.AppBskyEmbedImages.Image(alt=IMAGE_ALT_TEXT, image=upload.blob)]
    #     embed = models.AppBskyEmbedImages.Main(images=images)

    # client.send_image(
    #     text='Discos dos últimos 30 dias',
    #     image=img_data,
    #     image_alt=IMAGE_ALT_TEXT,
    #     langs=['pt-BR']
    # )

# send_post()