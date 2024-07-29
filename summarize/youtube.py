from urllib import parse
from urllib.parse import parse_qs
import re

from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube

# Define the regular expression pattern
video_id_pattern = r'[a-zA-Z0-9_-]{11}'

def get_youtube_video_id(url):
    if re.fullmatch(video_id_pattern, url):
        return url

    url_parts = parse.urlparse(url)
    query_params = parse_qs(url_parts.query)
    if ('www.youtube.com' == url_parts.hostname or 'youtube.com' == url_parts.hostname):
        if url_parts.path == '/watch':
            v = next(iter(query_params['v']), None)
            if v is None:
                raise Exception('YouTube URL expected to have v= parameter')
            return v
    if 'youtu.be' == url_parts.hostname:
        return url_parts.path[1:]

    raise Exception(f'Invalid YouTube URL {url}')

def get_youtube_transcript(url):
    video_id = get_youtube_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript

def get_youtube_video_info(url) -> YouTube:
    video_id = get_youtube_video_id(url)
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    yt = YouTube(video_url)
    return yt
