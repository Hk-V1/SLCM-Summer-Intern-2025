# Grain Type Identification Using Gemini Models

## Aim
To evaluate and compare the classification performance of Google's Gemini 1.5 and Gemini 2.5 models on grain type identification (wheat, rice, maize) using images, under two different prompt strategies.

## Models Used
- **Gemini 1.5 Pro**
- **Gemini 2.5 Pro**

## Dataset
Images of three grain types (wheat, rice, maize) with three variants each:
- `correct` – ideal sample
- `incorrect` – sample with visual issues
- `waveoff` – unclear or borderline sample

## Prompts Used

### Prompt 1: Image Quality Evaluation (project head’s prompt)
Focused on checking image quality criteria (sharpness, background, grain arrangement).  
*Not intended for classification.*

### Prompt 2: Direct Classification (custom-designed)
Asked the model to identify the grain type explicitly and explain visual cues used.

## Results

| Prompt     | Model       | Accuracy |
|------------|-------------|----------|
| Prompt 1   | Gemini 1.5  | 0.00     |
| Prompt 1   | Gemini 2.5  | 0.33     |
| Prompt 2   | Gemini 1.5  | 0.67     |
| Prompt 2   | Gemini 2.5  | **1.00** |

## Observations
- Gemini 2.5 outperformed Gemini 1.5 significantly under clear classification instructions.
- Prompt clarity greatly influenced model effectiveness.
- Prompt 2 yielded highly accurate, visually grounded predictions.

## Files

| File Name      | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| `Images.py`    | Optional script for image-related operations such as preprocessing or display. Can be used to manage reusable image utilities. |
| `README.md`    | High-level overview of the project including aim, dataset, methods, and results summary. Suitable for repository documentation. |
| `Report.md`    | Detailed technical report including introduction, methodology, prompt design comparison, results, and conclusion. |
| `main.ipynb`   | Main execution notebook. Runs model evaluations, applies prompts, parses outputs, and generates accuracy plots and tables. |
