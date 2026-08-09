from .api.gemini_client import GeminiClient


def main():
    client = GeminiClient()

    prompt = "Explain artificial intelligence in one sentence."

    response = client.generate(prompt)

    print("Gemini Response:")
    print(response)


if __name__ == "__main__":
    main()