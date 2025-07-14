# Rice Image Quality Evaluation Using Gemini Models

## 1. Introduction

Image-based quality evaluation of rice grains is essential for automated grading in agriculture. This project investigates the performance of **two Gemini multimodal models (Gemini 1.5 Flash and Gemini 2.5 Pro)** using structured prompt engineering. Unlike traditional classification, this task emphasizes **image quality assurance** based on visual attributes like sharpness, background consistency, and grain overlap.

The key objective was to determine:
- How **prompt clarity and design** affect GenAI output
- Which **model-prompt combination** yields the most reliable structured feedback

Two prompts were used:

- **Prompt A (Old Prompt):** Verbose, with a technical and rigid structure  
- **Prompt B (New Prompt):** Clean, well-structured, and optimized for LLM understanding

---

## 2. Work Done

### 2.1 Dataset

- **Total images:** 45 rice grain images (from existing Excel-based dataset)
- Images varied in background, clarity, and grain clumping
- Purpose: Evaluate if the image meets quality standards for scientific rice analysis

### 2.2 Models Evaluated

- **Gemini 1.5 Flash** *(Old Version)*
- **Gemini 2.5 Pro** *(New Version)*

### 2.3 Prompt Design

#### Prompt A: Old Prompt (Verbose QA Format)

- **Focus:** Strict image quality assessment using a detailed prompt
- **Output:** Structured JSON with scores on:
  - Grain verification
  - Background quality
  - Clumping and overlap
  - Blurriness
  - Overall verdict

#### Prompt B: New Prompt (Cleaner Structure)

- **Focus:** Same quality assessment with improved clarity and formatting
- **Output:** Same structured JSON, but better alignment with LLM understanding
- **Benefit:** More consistent and usable responses

---

## 3. Results

### 3.1 Accuracy Summary

| Prompt    | Model       | JSON Validity Rate | Verdict Accuracy* |
|-----------|-------------|---------------------|-------------------|
| Prompt A  | Gemini 1.5  | 65%                 | Medium            |
| Prompt A  | Gemini 2.5  | 85%                 | Good              |
| Prompt B  | Gemini 1.5  | 80%                 | Good              |
| Prompt B  | Gemini 2.5  | **100%**            | **Excellent**     |

\*Verdict Accuracy: Rate at which model gave a correct "yes"/"no" decision based on image ground truth.

### 3.2 Observations

- **Gemini 2.5 + Prompt B** produced the most valid, high-quality JSON outputs and verdicts.
- **Prompt A** led to inconsistent responses, especially with Gemini 1.5.
- **Prompt B** improved structure comprehension and JSON parsing success.
- Gemini 1.5 Flash struggled with verbose prompts and misinterpreted multiple sections.

### 3.3 Visualization Output

- **Bar chart:** Average `overall_score` per prompt-model combination
- **Stacked bar chart:** Verdict summary (`yes`/`no` per combination)
- **Console summary:** Success rates printed for each prompt-model combo

---

## 4. Conclusion

This project highlights the critical role of **prompt engineering** in **visual quality assurance tasks** using GenAI:

- A **task-aligned and structured prompt (Prompt B)** leads to improved interpretability and scoring consistency.
- **Gemini 2.5 Pro** outperforms Gemini 1.5 Flash across all metrics.
- Complex prompts may confuse older models; clarity and simplicity improve results.
- GenAI can replace manual rice image inspection, provided prompts are well-designed.

---

## 5. Files

| File Name                                    | Purpose                                                                 |
|---------------------------------------------|-------------------------------------------------------------------------|
| `Rice_GenAi_Old_to_New_V1.ipynb`            | Main execution notebook with prompt evaluation, model calls, and plots |
| `comprehensive_rice_analysis_with_images.xlsx` | Dataset with evaluation results and embedded images                    |
| `report.md`              | Structured summary of task, methodology, and results                   |
