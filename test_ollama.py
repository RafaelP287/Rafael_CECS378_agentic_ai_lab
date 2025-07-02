import ollama 

def main():
    print('=== Agentic AI LabOffline LLM Test ===')
    user_input = input('Enter your question for the LLM: ')
    try:
        response = ollama.chat(
            model='phi:2.7b',
            messages=[{'role':'user','content':user_input}]
        )
        print(response['message']['content'])
    except Exception as e:
        print(f"An error occured: {e}")
        print("Please ensure the Ollama application is running.")

if __name__ == '__main__':
    main()