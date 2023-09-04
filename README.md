# TranslationtoHinglish
This Python project utilizes the Hugging Face Transformers library to create a powerful Hinglish translator. It can take English sentences as input and provide translations in Hinglish. What makes this translator unique is the ability to replace specific Hindi words with their English counterparts while keeping the rest of the sentence in Hindi.
# English to Hinglish Translator

GitHub stars :- https://img.shields.io/github/stars/simr96/TranslationtoHinglish?style=flat-square
GitHub forks :- https://img.shields.io/github/forks/simr96/TranslationtoHinglish?style=flat-square

Translate English text into Hinglish (a mixture of Hindi and English) using the Hugging Face Transformers library.

Overview

This Python project demonstrates the translation of English sentences into Hinglish, a hybrid language combining Hindi and English. It utilizes a pre-trained translation model from Hugging Face Transformers to achieve this.

Features

- Translate English text into Hinglish.
- Customize translations with a dictionary of word replacements.
- Simple and easy-to-use Python script.

Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/simr96/TranslationtoHinglish.git

2. Install Required Dependencies
pip install transformers
install torch

Run the Python script to translate English sentences to Hinglish. You can customize translations by modifying the replacement dictionary in the script.

4. Usage
Modify the replacement_dict in the script to add or adjust word replacements for customized translations.

5. Run the Python script(python translate.py) with your English text as input: {Desired Input in English}
   


5. View the translated Hinglish text in the terminal.

6. Customize
You can tailor translations to your needs by adding or modifying word replacements in the replacement_dict. Customize translations to match your specific use case.

# Evaluation

For this model, A combination of BLEU score and human evaluation would be a gerat. Calculate the BLEU score to get an objective measure of translation quality, and then conduct human evaluation to assess fluency, idiomatic expressions, and cultural appropriateness. This comprehensive approach will provide a well-rounded assessment of your Hinglish translation model's performance.

1. Calculating BLEU Score:

  a. Using a set of reference translations (human-generated translations) for your test data.
  b. Generate translations using Hinglish model for the same test data.
  c. Calculating the BLEU score using libraries like NLTK or SacreBLEU to quantify the similarity between model-generated translations and reference translations.
  d. This will provide an objective metric to measure the model's performance.

2. Human Evaluation:

  a. Prepare a sample set of model-generated translations and corresponding reference translations. 
  b. Assemble a group of human evaluators who are proficient in both English and Hinglish.
  c. Define evaluation criteria: Clearly specify the aspects you want human evaluators to assess. This can include fluency, idiomatic expressions, cultural appropriateness, etc.
  d. Conduct the evaluation: Have each evaluator rate the model-generated translations based on the defined criteria. You can use a Likert scale (e.g., 1 to 5) for scoring.
  e. Collect scores from multiple evaluators to account for inter-rater reliability.
  f. Aggregate scores: Calculate the average scores for each aspect evaluated.

  According to me Human Evaluation is the best approach as this will prelimarily be used to serve different purpose for humans purposes based on their specific requirements.

