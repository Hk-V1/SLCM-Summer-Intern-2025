# Grain Image Classification Using Gemini Models

## 1. Introduction

Image-based grain classification plays a crucial role in agriculture and food quality assurance. This project evaluates the performance of two versions of Google's Gemini multimodal models—**Gemini 1.5 Pro** and **Gemini 2.5 Pro**—on a dataset of grain images representing three types: wheat, rice, and maize.

A key goal of this work is to demonstrate how **prompt design** significantly impacts model performance. Two distinct prompts were tested:
- Prompt 1: Focused on image quality evaluation (not classification)
- Prompt 2: Explicitly instructed the model to classify the grain type

## 2. Work Done

### 2.1 Dataset

The dataset includes **45 images**:
- 3 grain types: `wheat`, `rice`, `maize`
- Each type has 3 variations:
  - `correct`: high-quality, well-formed image
  - `incorrect`: lower-quality, noisy image
  - `waveoff`: ambiguous or edge-case image

### 2.2 Models Evaluated

- Gemini 1.5 Pro  
- Gemini 2.5 Pro

### 2.3 Prompt Design

#### Prompt 1: Image Quality Evaluation

You are evaluating this image of wheat grains for quality control in a scientific analysis context. Please assess the image based on the following criteria:

a) Is the image sharp and free from blur or motion artifacts?
b) Are all visible wheat grains entirely located on a uniformly white background?
c) Are individual wheat grains clearly visible and non-overlapping?

Finally, provide an overall verdict: Does this image meet all three quality standards for scientific grain analysis?

markdown
Copy
Edit

- Focus: Evaluating visual quality
- Limitation: Does not ask for classification
- Outcome: Models misaligned with intended classification task

#### Prompt 2: Direct Classification Prompt

Please analyze the provided image and identify the type of grain shown.
Select only one of the following categories: wheat, rice, or maize.
Important: Begin your response with the predicted grain type on the first line.
Then, in a second line, briefly explain the key visual features that support your classification (such as shape, color, size, texture, or arrangement).

markdown
Copy
Edit

- Focus: Task-aligned grain classification
- Clear structure encourages model to respond directly
- Yields better classification accuracy and explainability

## 3. Results

### 3.1 Accuracy Summary

| Prompt     | Model       | Accuracy |
|------------|-------------|----------|
| Prompt 1   | Gemini 1.5  | 0.00     |
| Prompt 1   | Gemini 2.5  | 0.33     |
| Prompt 2   | Gemini 1.5  | 0.67     |
| Prompt 2   | Gemini 2.5  | 1.00     |

### 3.2 Observations

- **Gemini 1.5 + Prompt 1**: Returned "unknown" for all images; not suited for classification.
- **Gemini 2.5 + Prompt 1**: Predicted "wheat" for most images regardless of true label; partial success.
- **Gemini 1.5 + Prompt 2**: Improved significantly; some classification errors still observed.
- **Gemini 2.5 + Prompt 2**: Achieved perfect accuracy across all 9 test images.

### 3.3 Prompt Comparison

| Aspect                     | Prompt 1 (Image Quality) | Prompt 2 (Classification) |
|---------------------------|---------------------------|----------------------------|
| Task clarity              | Low                        | High                       |
| Classification enabled?   | No                         | Yes                        |
| Gemini 1.5 accuracy        | 0.00                       | 0.67                       |
| Gemini 2.5 accuracy        | 0.33                       | 1.00                       |
| Prediction diversity       | Weak                       | Strong                     |
| Real-world applicability   | Limited                    | Suitable                   |

## 4. Conclusion

This project demonstrates that **prompt engineering has a critical impact** on the performance of large multimodal models in classification tasks. The results show that:

- A **task-aligned prompt** (Prompt 2) leads to significant gains in model accuracy and reliability.
- **Gemini 2.5 Pro** significantly outperforms Gemini 1.5 Pro when guided with a clear classification prompt.
- Models can misbehave or underperform when prompts are ambiguous or unrelated to the task goal.

These insights reinforce the need for careful prompt formulation in deploying AI for visual classification tasks in scientific and agricultural applications.

## 5. Files

| File Name      | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `Images.py`    | Optional script for image-related operations such as preprocessing or display. Can be used to manage reusable image utilities. |
| `Models.md`    | This document compares Gemini 1.5 Pro and Gemini 2.5 Pro models and explores their applications in multimodal AI tasks, particularly grain type classification. |
| `Report.md`    | Detailed technical report including introduction, methodology, prompt design comparison, results, and conclusion. |
| `main.ipynb`   | Main execution notebook. Runs model evaluations, applies prompts, parses outputs, and generates accuracy plots and tables. |
