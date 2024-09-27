from app.core.model import ModelManager
from app.schemas.chat import ChatRequest

class ChatService:
    def __init__(self):
        model_manager = ModelManager()
        self.model = model_manager.get_model()
        self.tokenizer = model_manager.get_tokenizer()
        self.device = model_manager.get_device()

    async def generate_response(self, request: ChatRequest) -> str:
        messages = [
            {"role": "system", "content": request.system_prompt},
            {"role": "user", "content": request.message}
        ]
        
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.device)

        output = self.model.generate(
            **model_inputs,
            max_new_tokens=512,
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
        )

        generated_ids = output[0][len(model_inputs.input_ids[0]):]
        response = self.tokenizer.decode(generated_ids, skip_special_tokens=True)

        return response