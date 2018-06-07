class SubtitleFinder:
    def __init__(self, options):
        self.options = options

    def find(self):
        movieName = self.options[1]
        print(movieName)
