from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load BlenderBot model
MODEL_NAME = "facebook/blenderbot-400M-distill"

tokenizer = BlenderbotTokenizer.from_pretrained(MODEL_NAME)
model = BlenderbotForConditionalGeneration.from_pretrained(MODEL_NAME)

def generate_reply(user_text: str) -> str:
    # Tokenize user input
    inputs = tokenizer(user_text, return_tensors="pt")

    # Generate response
    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    # Decode response
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return reply
