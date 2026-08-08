from ai_data_processor import BaseProcessor


if __name__ == "__main__":
    processor = BaseProcessor(
        model_name="Llama-3",
        learning_rate=0.001,
        batch_size=32
    )

    processor.validate()

    result = processor.process({"text": "hello"})

    print(f"Result: {result}")