import os
from uuid import uuid4

from loguru import logger

from advanced_http_request_handler import AdvancedHTTPRequestHandler
from settings import IMAGES_PATH, \
    ALLOWED_EXTENSIONS, MAX_FILE_SIZE, ERROR_FILE


class ImageHostingHttpRequestHandler(AdvancedHTTPRequestHandler):
    server_version = 'Image Hosting Server v0.1'

    def __init__(self, request, client_address, server):

        self.get_routes = {
            '/api/images/': self.get_images
        }
        self.post_routes = {
            '/upload/': self.post_upload
        }
        self.delete_routes = {
            '/api/delete/': self.delete_image
        }
        super().__init__(request, client_address, server)

    def get_images(self):
        self.send_json({
            'images': next(os.walk(IMAGES_PATH))[2]
        })

    def post_upload(self):
        length = int(self.headers.get('Content-Length'))
        if length > MAX_FILE_SIZE:
            logger.warning('File too large')
            self.send_html(ERROR_FILE, 413)
            return

        data = self.rfile.read(length)
        _, ext = os.path.splitext(self.headers.get('Filename'))
        image_id = uuid4()
        if ext not in ALLOWED_EXTENSIONS:
            logger.warning('File type not allowed')
            self.send_html(ERROR_FILE, 400)
            return

        with open(IMAGES_PATH + f'{image_id}{ext}', 'wb') as file:
            file.write(data)
        self.send_html('upload_success.html', headers={
            'Location': f'http://localhost/{IMAGES_PATH}{image_id}{ext}'})

    def delete_image(self):
        image_id = self.headers.get('Filename')
        if not image_id:
            logger.warning('Image not found')
            self.send_html(ERROR_FILE, 404)
            return

        image_path = IMAGES_PATH + image_id
        if not os.path.exists(image_path):
            logger.warning('Image not found')
            self.send_html(ERROR_FILE, 404)
            return

        os.remove(image_path)
        self.send_json({'Success': 'Image deleted'})
