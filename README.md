# Video Summarizer

## Requirements

- Python 3.x
- ChatGPT API KEY

## Installation

1. Clone the repository:
2. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Set up your [ChatGPT API](https://platform.openai.com/api-keys) key by creating a `.env` file in the root directory and adding the following line:

```text
OPENAI_API_KEY=your-chatgpt-api-key
```

Note: You may need to add [Billing](https://platform.openai.com/settings/organization/billing/overview)

## Usage

```bash
python summarize/main.py <youtube_video_url or video_id>
```

Example output:

```bash
python summarize/main.py https://youtube.com/watch?v=nscGizM9NQw

# Costs Explode for Nuclear Fusion Flagship Project -- Is It Still Worth the Money?

[Source Video](https://youtube.com/watch?v=nscGizM9NQw)

## Key Points

- **Project Overview**
  - International Thermonuclear Experimental Reactor (ITER) aims to be first nuclear fusion machine generating net energy.
  - Located in France, construction began in 2010.

- **Current Status**
  - Initial plasma run delayed from 2025 to 2034.
  - Project cost escalated from $5 billion to over $20 billion.

- **Funding Sources**
  - Funded by European countries, China, India, Japan, South Korea, Russia, and the U.S.
  - Taxpayer money involved.

- **Challenges Faced**
  - COVID-19 paused construction; cracks found in installed components.
  - Issues with parts from different manufacturers causing stress and corrosion.

- **Future Implications**
  - Delay raises questions about project’s purpose and relevance.
  - Potential for private companies to advance fusion technology faster than ITER.

- **Alternative Technologies**
  - Other fusion methods like stellarators and inertial confinement may lead to quicker results.
  - ITER's data collection may still be necessary despite delays.

- **Conclusion**
  - Uncertainty about ITER's value as private sector progresses.
  - Ongoing debate on whether continued investment is justified.
```

Notice the output is markdown which will look like this:

# Costs Explode for Nuclear Fusion Flagship Project -- Is It Still Worth the Money?

[Source Video](https://youtube.com/watch?v=nscGizM9NQw)

## Key Points

- **Project Overview**
  - International Thermonuclear Experimental Reactor (ITER) aims to be first nuclear fusion machine generating net energy.
  - Located in France, construction began in 2010.

- **Current Status**
  - Initial plasma run delayed from 2025 to 2034.
  - Project cost escalated from $5 billion to over $20 billion.

- **Funding Sources**
  - Funded by European countries, China, India, Japan, South Korea, Russia, and the U.S.
  - Taxpayer money involved.

- **Challenges Faced**
  - COVID-19 paused construction; cracks found in installed components.
  - Issues with parts from different manufacturers causing stress and corrosion.

- **Future Implications**
  - Delay raises questions about project’s purpose and relevance.
  - Potential for private companies to advance fusion technology faster than ITER.

- **Alternative Technologies**
  - Other fusion methods like stellarators and inertial confinement may lead to quicker results.
  - ITER's data collection may still be necessary despite delays.

- **Conclusion**
  - Uncertainty about ITER's value as private sector progresses.
  - Ongoing debate on whether continued investment is justified.

---

## Future

- Adjust output format and prompt
- Tests
- Caching
- More video hosting provider support
- Extracting the audio track if transcriptions are unavailable
- Storing the transcriptions and summaries in a local datastore for analysis, later
- Companion project to provide a unified video interface for study and research