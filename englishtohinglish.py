import transformers
from transformers import MarianTokenizer, MarianMTModel

# Load the Hinglish translation model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-hi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Function to translate English to Hinglish
def translate_to_hinglish(english_text):
    # Tokenize the input text
    inputs = tokenizer.encode(">>en<<" + english_text, return_tensors="pt")

    # Generate Hinglish translation
    translation = model.generate(inputs, max_length=150, num_beams=5, early_stopping=True)

    # Decode and return the translation
    hinglish_translation = tokenizer.decode(translation[0], skip_special_tokens=True)
    return hinglish_translation

# Example usage
english_text = "Hello, how are you?"
hinglish_translation = translate_to_hinglish(english_text)
print(f"English: {english_text}")
print(f"Hinglish: {hinglish_translation}")