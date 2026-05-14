from groq import *
# Initialize the Groq client
# Best practice: Set your key as an environment variable 'GROQ_API_KEY'
client = Groq(
    api_key="YOUR API KEY",
)

# Create a chat completion
def gen_notes(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                
                "content":f'''Can you generate a super and detailed notes of : {user_input} and hey it should
                         be in the form of html like 
                        <h3>Topic</h3> 
                        <ul>
                        <li>Subtopic</li>
                        <p>explanatiom</p>
                        </ul>'''
   
            }
        ],
        model="llama-3.3-70b-versatile", # You can also use "mixtral-8x7b-32768" or "gemma-7b-it"
    )

    # Print the response
    result = chat_completion.choices[0].message.content
    return result



