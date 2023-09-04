import transformers
from transformers import MarianTokenizer, MarianMTModel

#Loading the Hinglish translation model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-hi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

replacement_dict = {
    "मिनट": "minute",
    "डेमो": "demo",
    "इस": "headset",
    "वीडियो": "video",
    "उत्पाद": "product",
    "स्पष्ट रूप से": "clearly",
    "बुरा": "bad",
    "इंतजार": "waiting",
    "बग": "bag",
    "फ़ीडबैक": "feedback",
    "टिप्पणी": "comment",
    "खण्ड": "section"
}


def translate_to_hinglish(english_text):
    # Tokenize the input text
    inputs = tokenizer.encode(">>en<<" + english_text, return_tensors="pt")

    # Generate Hinglish translation
    translation = model.generate(inputs, max_length=150, num_beams=5, early_stopping=True)

    # Decoding and returning the translation with the help of words replaced via dictionary
    hinglish_translation = tokenizer.decode(translation[0], skip_special_tokens=True)
    
    for key, value in replacement_dict.items():
        hinglish_translation = hinglish_translation.replace(key, value)

    return hinglish_translation


english_text = "Definitely share your feedback in the comment section"
hinglish_translation = translate_to_hinglish(english_text)
print(f"English: {english_text}")
print(f"Hinglish: {hinglish_translation}")
