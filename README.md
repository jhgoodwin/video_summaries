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
python summarize/main.py https://www.youtube.com/watch?v=4rk9fHIOGTU

Summary:
- URL:https://www.youtube.com/watch?v=4rk9fHIOGTU
# Video Summary: Llama 8b Tested - A Huge Step Backwards

## Key Points
- **Model Comparison**: 
  - Llama 3.1 8B shows a significant quality improvement over its predecessor.
  - Benchmarks indicate Llama 3.1 8B scores double in human evaluation compared to the previous model.

- **Testing Setup**:
  - Model hosted on Vulture using Open Web UI.
  - Tests include coding tasks and logical reasoning.

- **Performance Results**:
  - Basic coding tasks performed well, but complex tasks (e.g., writing a game) had issues.
  - Censorship tests showed limitations in providing certain information.
  - Logical reasoning tasks yielded mixed results, with some failures noted.

- **Overall Impression**:
  - The model's performance was disappointing, failing to meet expectations in several areas.
  - The reviewer expresses frustration with the model's limitations despite its speed.

## Benchmarks
- **Human Eval**: 34 (previous) vs. 68 (current)
- **GSM 8K**: 0.57 (previous) vs. 0.84 (current)
- **General Performance**: Improvements noted but not substantial across all tests.

## Conclusion
- The Llama 3.1 8B model is fast but underperforms in quality and reasoning tasks.
- The reviewer expresses a negative bias towards the model's capabilities.

## References
- [Llama 3.1 8B](https://example.com)
- [Vulture Cloud Services](https://example.com)

```

Notice the output is markdown which will look like this:

Summary:
- URL:https://www.youtube.com/watch?v=4rk9fHIOGTU
# Video Summary: Llama 8b Tested - A Huge Step Backwards

## Key Points
- **Model Comparison**: 
  - Llama 3.1 8B shows a significant quality improvement over its predecessor.
  - Benchmarks indicate Llama 3.1 8B scores double in human evaluation compared to the previous model.

- **Testing Setup**:
  - Model hosted on Vulture using Open Web UI.
  - Tests include coding tasks and logical reasoning.

- **Performance Results**:
  - Basic coding tasks performed well, but complex tasks (e.g., writing a game) had issues.
  - Censorship tests showed limitations in providing certain information.
  - Logical reasoning tasks yielded mixed results, with some failures noted.

- **Overall Impression**:
  - The model's performance was disappointing, failing to meet expectations in several areas.
  - The reviewer expresses frustration with the model's limitations despite its speed.

## Benchmarks
- **Human Eval**: 34 (previous) vs. 68 (current)
- **GSM 8K**: 0.57 (previous) vs. 0.84 (current)
- **General Performance**: Improvements noted but not substantial across all tests.

## Conclusion
- The Llama 3.1 8B model is fast but underperforms in quality and reasoning tasks.
- The reviewer expresses a negative bias towards the model's capabilities.

## References
- [Llama 3.1 8B](https://example.com)
- [Vulture Cloud Services](https://example.com)

---

## Future

- Adjust output format and prompt
- Tests
- Caching
- More video hosting provider support
- Extracting the audio track if transcriptions are unavailable
- Storing the transcriptions and summaries in a local datastore for analysis, later
- Companion project to provide a unified video interface for study and research