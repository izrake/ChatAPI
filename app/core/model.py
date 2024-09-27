import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from app.core.config import settings

class ModelManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_model()
        return cls._instance

    def init_model(self):
        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_NAME)

        print("Loading model...")
        self.model = AutoModelForCausalLM.from_pretrained(
            settings.MODEL_NAME,
            torch_dtype=torch.float16,  # Use float16 for efficiency
            device_map="auto",
            low_cpu_mem_usage=True
        )

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")

    def get_model(self):
        return self.model

    def get_tokenizer(self):
        return self.tokenizer

    def get_device(self):
        return self.device