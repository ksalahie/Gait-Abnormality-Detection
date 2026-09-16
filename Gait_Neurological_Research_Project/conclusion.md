# Final Conclusion: Gait Abnormality Research

## Findings
Through our multi-tiered algorithmic approach, we discovered that dynamic gait rhythm—specifically the continuous fluctuations in stride interval and double support phase—acts as a strong phenotypic marker for neurodegenerative conditions and brain injuries.

1. **Static Feature Extraction (Random Forest):** 
   Our ensemble models confirmed that variables such as `double_support_percent` and `stance_interval_asymmetry` contain high non-linear correlation with Parkinson's and Cerebral Palsy. Patients with advanced conditions tend to exhibit a disproportionately large double support phase as a biomechanical compensation for instability.

2. **Time-Series Analysis (CNN-LSTM):** 
   Demonstrated that analyzing raw time-series data outperforms static feature extraction by capturing the "fractal dynamics" of gait. The RNN architecture successfully flagged progressive gait freezing and arrhythmic anomalies that static averages mask, allowing for highly accurate, multi-class predictions across the PhysioNet dataset.

## Comparison to the Stroke Prediction Project
While this repository functions in a similar capacity as a predictive medical tool, it differs fundamentally from the Stroke Prediction Project in both algorithm and purpose:

- **Algorithmic Architecture:** The Stroke Project utilized predictive analytics (e.g., Logistic Regression) on static, independent health variables (age, BMI, blood pressure) to output a binary risk probability (Yes/No). This gait project relies on advanced Deep Learning (CNN-LSTM) and multi-class ensemble models to process continuous, real-time biomechanical loops.
- **Fundamental Purpose:** The Stroke model is a **prognostic** tool designed to forecast the likelihood of a future medical event. This gait analysis model is a **diagnostic and phenotyping** tool, designed to identify the physical manifestation of an existing condition based on motor output.
