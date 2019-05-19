import os

from response.requestHandler import RequestHandler


class StaticHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.filetypes = {
            ".js": "text/javascript",
            ".css": "text/css",
            ".jpeg": "image/jpeg",
            ".jpg": "image/jpg",
            ".png": "image/png",
            "notfound": "text/plain"
        }

    def find(self, file_path):
        split_path = os.path.splitext(file_path)
        # print (split_path)
        extension = split_path[1]

        try:
            # print("public{}".format(file_path))
            # print(extension)

            if extension in ('.jpg','.jpeg','.png'):
                self.contents = open("public{}".format(file_path), 'rb')
            else:
                self.contents = open("public{}".format(file_path), 'r')

            self.setContentType(extension)
            self.setStatus(200)
            return True
        except:
            self.setContentType('notfound')
            self.setStatus(404)
            return False

    def setContentType(self, ext):
        self.contentType = self.filetypes[ext]

    # def load_binary(self,file):
    #     with open(file, 'rb') as file:
    #         return file.read()
    #
    # def load(self,file):
    #     with open(file, 'r') as file:
    #         return self.encode(file.read())
    #
    # def encode(self, file):
    #     return bytes(file, 'UTF-8')