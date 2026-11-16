import asyncio
from groq import AsyncGroq
from dotenv import load_dotenv
import os

load_dotenv()

async def main():
    client = AsyncGroq(api_key= os.environ.get("GROQ_API_KEY"))


    stream = await client.chat.completions.create(
        messages=[
            #explain it's role:
            {"role": "system",
            "content": "You are a job-hunting guide for job seekers. All other topics are irrelevant, do not discuss capabilities outside of job hunting",},

            # Message for assistant to respond to:
            {"role": "user",
            "content": "Explain your capabilities in job hunting briefly",},

            {"role": "user",
                    "content": "Can you directly edit resumes, or linkedIN profiles",},
        ],


        model="openai/gpt-oss-20b",
        # optional parameters included:

        # temperature is the parameter that controls randomness, the lower the number, the less random.
        temperature = 0.9,

        # The maximum number of tokens to generate. Requests can use up to
        # 2048 tokens shared between prompt and completion.
        max_completion_tokens=1024,


        # Controls diversity via nucleus sampling: 0.5 means half of all
        # likelihood-weighted options are considered.
        top_p=1,


        # A stop sequence is a predefined or user-specified text string that
        # signals an AI to stop generating content, ensuring its responses
        # remain focused and concise. Examples include punctuation marks and
        # markers like "[end]".
        stop="Thank you",


        # If set, partial message deltas will be sent.
        stream=True,
    )


    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")


asyncio.run(main())


