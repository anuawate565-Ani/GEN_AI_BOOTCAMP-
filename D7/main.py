from model_registry import ModelRegistry

registry = ModelRegistry()

print("\nLoading all models...\n")
registry.load_all()

vision = registry.get_model("YOLOv11")
embedding = registry.get_model("BGE")
llm = registry.get_model("Llama3")

image = input("Enter image name: ")

object_name = vision.classify(image)
print("\nDetected Object:", object_name)

knowledge = embedding.embed(object_name)
print("\nEmbedding Result:", knowledge)

answer = llm.generate(f"Explain about {object_name}")
print("\nLLM Response:")
print(answer)

print("\nUnloading models...\n")
registry.unload_all()
