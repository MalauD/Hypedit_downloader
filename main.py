# This script will download music passed as argument
# and save it in the current directory
# Command line usage: python main.py -l <link>
# Example: python main.py -l https://hypeddit.com/link/xxxxxx
# Or you can read a file with links and download all of them
# Command line usage: python main.py -f <filename>
# Example: python main.py -f links.txt

# Get the arguments
import sys
import requests
import os
from bs4 import BeautifulSoup
import argparse
import eyed3
from pydub import AudioSegment

download_dir = "./output/"

# Make directory if it doesn't exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)


def get_music_file(link):
    # Visit the link and select h1 and h2 tags
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    h1 = soup.find_all('h1')
    h2 = soup.find_all('h2')

    # Get the artist and song name (inner text)
    artist = h1[0].get_text()
    song = h2[0].get_text()

    # Get the download link
    link = link.replace("https://hypeddit.com/",
                        "https://hypeddit-gates-prod.s3.amazonaws.com/")
    # Remove query string
    link = link.split("?")[0]
    link = link + "_main"
    # Download the song and print progress
    print("Downloading " + link + " (" + artist + " - " + song + ")")
    r = requests.get(link, allow_redirects=True)
    return r.content, artist, song


def save_file_mp3(filename, artist, song):
    audio = AudioSegment.from_wav(filename)
    mp3_filename = filename.replace(".wav", ".mp3")
    audio.export(mp3_filename, format="mp3", bitrate="320k")
    tags = eyed3.load(mp3_filename)
    tags.tag.artist = artist
    tags.tag.title = song
    tags.tag.save()
    return mp3_filename


# Read command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--link", help="Link to download")
parser.add_argument("-f", "--file", help="File with links to download")
parser.add_argument("-m", "--mp3", help="Convert to mp3", action="store_true")
args = parser.parse_args()

if args.link:
    c, artist, song = get_music_file(args.link)
    filename = download_dir + artist + " - " + song + ".wav"
    with open(filename, 'wb') as f:
        f.write(c)
    if args.mp3:
        print("Converting to mp3")
        filename = save_file_mp3(filename, artist, song)
    print("Downloaded " + filename)
elif args.file:
    with open(args.file) as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.strip()
            c, artist, song = get_music_file(line)
            filename = download_dir + artist + " - " + song + ".wav"
            with open(filename, 'wb') as f:
                f.write(c)
            if args.mp3:
                print("Converting to mp3")
                filename = save_file_mp3(filename, artist, song)
            print("Downloaded " + str(idx + 1) + " songs - " + filename)
else:
    print("No arguments passed")
    print("Usage: python main.py -l <link>")
    print("Example: python main.py -l https://hypeddit.com/link/xxxxxx")
    print("Or you can read a file with links and download all of them")
    print("Usage: python main.py -f <filename>")
    print("Example: python main.py -f links.txt")
    print("Use -m to convert to mp3")
