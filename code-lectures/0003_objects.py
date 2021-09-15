import abc

# class BaseReader(abc.ABC):

#     @abc.abstractmethod
#     def read(self, path):
#         print("Should not ever be executed")

# class ImageReader(BaseReader):

#     def read(self, path):
#         print("reading image from", path)

# class TextReader(BaseReader):

#     def read(self, path):
#         print("reading text from", path)

# class BadReader(BaseReader):
#     pass

class FileReader:

    def read(self, path):
        if path.endswith(".jpg"):
            self.data =  self.read_image(path)
        elif path.endswith(".avi"):

        else:
            self.data = self.read_text(path)

    def save(self, path):
        if path.endswith(".jpg"):
            self.save_image( path)
        else:
            self.write_text( path)

    def read_image(self, path):
        pass # Reading the image

    def read_text(self, path):
        pass # Reading the text

    def write_image(self, path):
        pass # writing the image

    def write_text(self, path):
        pass # writing the text


class ImageReader:

    def read(self, path):
        pass # Reading the image

    def save(self, path):
        pass # writing the image

class VideoReader:

    def read(self, path):
        pass # Reading the image

    def save(self, path):
        pass # writing the image

def make_reader_factory(path, df,dfs,sdf,s):
    """Make an instance of a reader based on the type of the path
    """