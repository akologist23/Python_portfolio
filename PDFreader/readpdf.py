from pdfreader import PDFDocument, SimplePDFViewer

class PDFReader:
    def __init__(self, filename):
        self.filename = filename
        self.title = None
        self.text_list = None
        self.sentence_list = []
        self.read()

    def read(self):
        fd = open(self.filename, 'rb')  # r=read b=binary for non-text
        viewer = SimplePDFViewer(fd)
        self.title = viewer.metadata['Title']
        extracted_letters = [canvas.strings for canvas in viewer]
        self.text_list = ["".join(page) for page in extracted_letters]
        #print(f"This list has length {len(self.text_list)}")

        for text in self.text_list:
            self.sentence_list.extend(text.split("."))

        print(f"This list has length {len(self.sentence_list)}")
        return self.sentence_list
