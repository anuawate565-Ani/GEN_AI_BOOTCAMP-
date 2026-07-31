from p2_llm_model import LLMModel
from p3_vision_model import VisionModel
from p4_embedding_model import EmbeddingModel
from model_registry import ModelRegistry

llm = LLMModel("Llama3", 6767)
embedding = EmbeddingModel("BGE", 757)
vision = VisionModel("CLIP", 533)

registry = ModelRegistry()

registry.register_model(llm)
registry.register_model(embedding)
registry.register_model(vision)

registry.list_model()

registry.load_all()

vision_result = vision.analysis_image("dog.jpg")
llm_result = llm.generate(vision_result)
embedding_result = embedding.embed(llm_result)

print(vision_result)
print(llm_result)
print(embedding_result)

registry.unload_all()