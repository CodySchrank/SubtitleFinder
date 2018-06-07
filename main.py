import sys

from lib import SubtitleFinder

def run_project(args):
    finder = SubtitleFinder(args)
    finder.find()

if __name__ == '__main__':
    run_project(sys.argv)
