import os
import sys
import csv

args = sys.argv


def start_videoget(URL):
        outplace = os.getcwd()+"\output"+"\ "
        print('場所移動');
        os.chdir('ffmpeg/bin');
        print(os.getcwd())
        print(URL)
        os.system('youtube-dl.exe '+URL+ ' -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"'+ ' -o "'+outplace+'%(title)s"');
        os.chdir('..');
        os.chdir('..');


def get_csvdata(name):
    print('csv読み込み')
    with open ( name,'r') as f :
        reader = csv.reader( f )
        for line in reader:
            start_videoget(line[0])
            print(line[0])

def main():
    if '.csv' in args[1]:
        print('csv')
        get_csvdata(args[1])
    if 'http' in args[1]:
        print('url')
        start_videoget(args[1])

if __name__ == "__main__":
    main()