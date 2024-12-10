import openai

# Replace with your OpenAI API key
openai.api_key = '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'

def get_response(prompt):
    """
    Get a response from OpenAI's GPT model based on the given prompt.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a sustainability advisor. Offer eco-friendly tips, sustainable shopping advice, and energy-saving ideas."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

def chatbot():
    """
    A chatbot that provides sustainability advice.
    """
    print("🌍 Welcome to the Sustainability Advisor! 🌱")
    print("I can provide tips on eco-friendly practices, sustainable shopping, and energy-saving ideas for your home.")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Sustainability Advisor: Goodbye! Stay green! 🌿")
            break
        # Get response from OpenAI based on user input
        response = get_response(user_input)
        print(f"Sustainability Advisor: {response}")

if __name__ == "__main__":
    chatbot()
