# Hypeddit Downloader

This script allows you to download music from Hypeddit by providing a link or reading a file containing multiple links. The downloaded music files are saved in the `./output` directory.

## Usage

```
python main.py -l <link>
```

To download music from a single link, use the `-l` or `--link` option followed by the link URL. For example:

```
python main.py -l https://hypeddit.com/link/xxxxxx
```

To download music from multiple links specified in a file, use the `-f` or `--file` option followed by the filename. For example:

```
python main.py -f links.txt
```

## Prerequisites

Make sure you have the necessary dependencies installed. You can install them by running the following command:

```
pip install -r requirements.txt
```

The `requirements.txt` file contains the required libraries and their versions.

## Command Line Arguments

-   `-l, --link`: Specifies a single link to download music from.
-   `-f, --file`: Specifies a file containing multiple links to download music from.
-   `-m, --mp3`: Converts the downloaded files to MP3 format.

If the `-m` flag is provided, the script will convert the downloaded files to MP3 format using a bitrate of 320kbps.

## Notes

-   The script assumes that the provided links are from the "hypeddit.com" website.

For more information on how to use the script, refer to the usage section.
