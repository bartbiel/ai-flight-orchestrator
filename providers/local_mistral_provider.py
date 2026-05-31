from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    pipeline
)

from langchain_community.llms import HuggingFacePipeline

from providers.base import BaseLLMProvider

class LocalMistralProvider(BaseLLMProvider):

    def __init__(self, model_path: str):

        tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            local_files_only=True,
            trust_remote_code=True,
            use_fast=False
        )

        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            local_files_only=True,
            device_map="auto"
        )

        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=512
        )

        self.llm = HuggingFacePipeline(pipeline=pipe)

    async def generate(self, messages: list[dict]) -> str:

        prompt = messages[-1]["content"]

        response = self.llm.invoke(prompt)

        return response