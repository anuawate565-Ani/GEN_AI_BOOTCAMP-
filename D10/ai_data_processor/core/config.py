class AIConfig:
    def __init__(
        self,
        model_name: str,
        learning_rate: float,
        batch_size: int
    ) -> None:
        self.model_name = model_name
        self.learning_rate = learning_rate
        self.batch_size = batch_size