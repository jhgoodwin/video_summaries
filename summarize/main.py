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
**Task: Summarize a Video**

**Instructions:**

1. **Format:**
   - Use headings and bullet points.
   - Prioritize information from most to least important.
   - Tone should be concise and to the point - risk being rude.

2. **Content Guidelines:**
   - Focus on key points and core topics.
   - Exclude promotional content, personal drama, repetition, hyperbolic claims, and subscription requests.
   - Skip use of articles ahead of nouns if they do not dramatically improve comprehension.

3. **Links:**
   - Include links to core topics and references.
   - Use specific links when possible.

4. **Output Structure:**
   - Start with the title/heading.
   - Include the URL of the video with the link text 'Source Video'
"""

def get_user_prompt(video_transcript, video_metadata):
    video_text = [i['text'] for i in video_transcript]
    return f"""
Title: {video_metadata.title}
Description: {video_metadata.description}
Transcript: {video_text}
URL: {video_metadata.watch_url}
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
    return summary

def main(urls):
    for url in urls:
        summary = summarize(url)
        print(f"\n{summary}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('urls', nargs='+', help='One or more urls')
    args = parser.parse_args()
    urls = args.urls

    main(urls)