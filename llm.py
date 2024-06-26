import os
import google.generativeai as genai
import dotenv

dotenv.load_dotenv()

class GenerativeAIClient:
    def __init__(self) -> None:
        #genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        self.model = genai.GenerativeModel(model_name='gemini-1.5-flash')

    def generate_summary(self, prompt: str) -> str:
        """
        Generates a Thai language summary of the given video transcript prompt.
        """
        prompt_template = """You are an AI agent tasked with summarizing YouTube video transcriptions and identifying key insights and highlights. Your goal is to provide a concise summary that captures the main points of the video, along with notable insights and important moments.
You will be given the following information:
<youtube_transcript>
{}
</youtube_transcript>
Please follow these steps to complete the task:
1. Carefully read through the entire transcript.
2. Create a brief summary (2-3 sentences) that captures the main topic and purpose of the video.
3. Identify 3-5 key points or main ideas discussed in the video. These should be the most important concepts or arguments presented.
4. Determine 2-3 key insights from the video. These should be unique, thought-provoking, or particularly valuable pieces of information that viewers would find most useful or interesting.
5. Highlight 2-3 important moments or sections from the video. These could be compelling examples, surprising facts, or pivotal points in the discussion. Include approximate timestamps if possible (you can estimate based on the video duration and the flow of the transcript).
6. Output Must Be in Thai Language
7. Provide your output in the following format:

# Summary
[Insert your 2-3 sentence summary here]

## Key points
- [Key point 1]
- [Key point 2]
- [Key point 3]
[Add more if necessary]

## Key insights
1. [Key insight 1]
2. [Key insight 2]
3. [Key insight 3 - if applicable]


## Highlights
1. [Important moment 1] (Approximate timestamp: [XX:XX])
2. [Important moment 2] (Approximate timestamp: [XX:XX])
3. [Important moment 3 - if applicable] (Approximate timestamp: [XX:XX])

Remember to keep your language clear and concise. Avoid using direct quotes from the transcript unless absolutely necessary. Instead, paraphrase the content to capture the essence of the ideas presented in the video."""
        self.prompt = prompt_template.format(prompt)
        self.response = self.model.generate_content(self.prompt)
        return self.response.text
