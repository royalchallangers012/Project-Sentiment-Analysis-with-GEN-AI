
import subprocess

def ask_ollama(question):
    try:
        # Run the Ollama model and pass the question directly
        result = subprocess.run(
            ['ollama', 'run', 'deepseek-r1:1.5b', question],
            text=True,
            capture_output=True,
            encoding='utf-8'  # Set encoding to handle special characters
        )

        # Check if the model ran successfully
        if result.returncode == 0:
            return result.stdout.strip()  # Output of the model
        else:
            return f"Error: {result.stderr.strip()}"  # Error message from stderr

    except Exception as e:
        return f"An error occurred: {e}"

while True:
    question = input("Ask a question (or type 'exit' to quit): ")

    if question.lower() == 'exit':
        print("Exiting program...")
        break

    answer = ask_ollama(question)

    print(f"Question: {question}")
    print(f"Answer: {answer}")
