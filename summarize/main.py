from argparse import ArgumentParser
from groq import Groq
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI
import os

import youtube

load_dotenv()

groq_api_key = os.environ.get("GROQ_API_KEY", None)
openai_api_key = os.environ.get("OPENAI_API_KEY", None)

SYSTEM_PROMPT = """
Take the role of a video summarizer.
Prefer terse, concise language and focus on the most important aspects of the video content.
Use headings and bullets instead of paragraphs.
Omit promotional content, personal drama, reptition, hyperbolic claims, requests to subscribe, and other non-essential content.
Include links to core topics and references made in the video. Use specific links if that is possible.
"""

def get_user_prompt(video_transcript, video_metadata):
    video_text = [i['text'] for i in video_transcript]
    return f"""
Title: {video_metadata.title}
Description: {video_metadata.description}
Transcript: {video_text}
"""

def summarize_with_groq(video_transcript, video_metadata):
    client = Groq(api_key=groq_api_key)
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": get_user_prompt(video_transcript, video_metadata) }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")

ollama_llm = ChatOllama(
    model="mistral:7b-instruct-v0.2-q8_0",
    keep_alive=300, # keep the model loaded indefinitely
    temperature=0,
    max_new_tokens=1024)

def summarize_with_ollama(video_transcript, video_metadata):
    result = ollama_llm.invoke(
        [
            ( "system", SYSTEM_PROMPT ),
            ( "user", get_user_prompt(video_transcript, video_metadata) )
        ],
        # temperature=1,
        # max_tokens=1024,
        # top_p=1,
        # # stream=True,
        # stop=None,
    )
    return result.content

chatgpt_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=1024,
    api_key=openai_api_key
)

def summarize_with_chatgpt(video_transcript, video_metadata):
    result = chatgpt_llm.invoke(
        [
            ( "system", SYSTEM_PROMPT ),
            ( "user", get_user_prompt(video_transcript, video_metadata) )
        ],
        # temperature=1,
        # max_tokens=1024,
        # top_p=1,
        # # stream=True,
        # stop=None,
    )
    return result.content

def summarize(url):
    video_transcript = youtube.get_youtube_transcript(url)
    video_metadata = youtube.get_youtube_video_info(url)
    summary = summarize_with_chatgpt(video_transcript, video_metadata)
    return f"Summary:\n- URL: {url}\n{summary}"

def main(urls):
    #url = "https://youtu.be/lUSwEDAt6lI"
    #url = "https://youtu.be/7WxTTkR4QLA"
    #url = "https://youtu.be/NHxzE2Bq558"
    #url = "https://www.youtube.com/watch?v=Wa5r73qp_-U"
    #url = "https://youtu.be/a6FAHxB2xMc"
    #url = "https://www.youtube.com/watch?v=4rk9fHIOGTU"
    #summarize
    for url in urls:
        summary = summarize(url)
        print(f"\n{summary}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('urls', nargs='+', help='One or more urls')
    args = parser.parse_args()
    urls = args.urls

    main(urls)