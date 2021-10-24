# Object Oriented Programming

# %%

# In this tutorial, we will try to create a file reader which can handle jpg images, avi videos and text files. 

class FileReader:            # We use class method to create an object

    def read(self, path):            # Define a function to read files based on extensions
        if path.endswith(".jpg"):
            self.data =  self.read_image(path)
        elif path.endswith(".avi"):
            self.data =  self.read_video(path)
        else:
            self.data = self.read_text(path)

    def save(self, path):           # Define a function to save files based on extensions
        if path.endswith(".jpg"):
            self.save_image(path)
        elif path.endswith(".avi"):
            self.save_video(path)
        else:
            self.save_text(path)

    # Then we need to define read and save function for all these file types, which are 2*3=6 functions in total
    def read_image(self, path):
        pass # Reading the image

    def read_video(self, path):
        pass # Reading the video

    def read_text(self, path):
        pass # Reading the text

    def save_image(self, path):
        pass # writing the image

    def save_video(self, path):
        pass # writing the image

    def save_text(self, path):
        pass # writing the text

path = "./"
FileReader.read(path)
FileReader.save(path)

# %%

# The above code structure works, but it's not clean enough. We could create the objects for image, video and text separately.

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

class TextReader:
    
    def read(self, path):
        pass # Reading the image

    def save(self, path):
        pass # writing the image

def make_reader_factory(path):
    """Make an instance of a reader based on the type of the path
    """
    # Get file reader object based on extension
    if path.endswith(".jpg"):
        FileReader = ImageReader
    elif path.endswith(".avi"):
        FileReader = VideoReader
    else:
        FileReader = TextReader
    return FileReader

path = "./"
FileReader.read(path)
FileReader.save(path)
