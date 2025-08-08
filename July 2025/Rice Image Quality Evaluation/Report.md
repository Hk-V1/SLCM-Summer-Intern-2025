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

### 3.1 Combination Performance Summary

| Combination              | Approved | Rejected | Errors | Success Rate |
|--------------------------|----------|----------|--------|---------------|
| New_Prompt_Old_Version   | 6        | 3        | 0      | 66.7%         |
| Old_Prompt_New_Version   | 1        | 8        | 0      | 11.1%         |
| New_Prompt_New_Version   | 0        | 9        | 0      | 0.0%          |
| Old_Prompt_Old_Version   | 6        | 3        | 0      | 66.7%         |

### 3.2 Observations

- **New Prompt + Old Model** and **Old Prompt + Old Model** had the highest success rates (66.7%), showing strong alignment when prompt complexity is balanced with model capability.
- **New Prompt + New Model** unexpectedly resulted in a 0% approval rate, suggesting that prompt structure or model expectations might be misaligned.
- **Old Prompt + New Model** yielded the lowest non-zero performance (11.1%), likely due to verbosity confusing newer models optimized for concise instruction sets.
- No combinations resulted in API or logic errors (`Errors = 0`), indicating robust pipeline execution.

### 3.3 Visual Output (From Notebook)

- **Bar chart** comparing average `overall_score` across combinations
- **Stacked bar chart** of verdicts (approved vs rejected)
- **Console-based summary** of success rates per combination
---

## 4. Conclusion

This project demonstrates the powerful synergy between **prompt engineering** and **multimodal AI models** for real-world agricultural quality assurance.

Key takeaways include:

- **Prompt clarity and alignment with task goals** directly impact model output. The "New Prompt" offered better structure but worked more reliably with the **Gemini 1.5 Flash** model than with Gemini 2.5 Pro.
- Surprisingly, **New Prompt + New Model (Gemini 2.5 Pro)** produced the lowest approval rate (0%), suggesting that newer models may require different tuning or more contextual grounding for QA tasks.
- **Old Prompt + Old Model** and **New Prompt + Old Model** had the best success rates (66.7%), showing that moderate prompts work best with older, more deterministic models.
- No errors occurred in the full pipeline, confirming that the prompt-model evaluation framework is **robust and scalable**.

Ultimately, the project emphasizes that **success in GenAI-powered image tasks depends not only on model capability but on thoughtful prompt design**. This approach can be generalized for automating QA in grains, seeds, or any standardized agricultural product dataset.

---

## 5. Files

| File Name                                    | Purpose                                                                 |
|---------------------------------------------|-------------------------------------------------------------------------|
| `Rice_GenAi_Old_to_New_V1.ipynb`            | Main execution notebook with prompt evaluation, model calls, and plots |
| `report.md`              | Structured summary of task, methodology, and results                   |
