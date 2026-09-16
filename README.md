# Gait Abnormality & Neurological Conditions Predictor

This repository contains the data processing, predictive modeling, and visualization scripts for analyzing the correlation between gait abnormalities and neurological conditions (Parkinson's, Huntington's, ALS, Cerebral Palsy, Brain Injury, and healthy controls).

Unlike prognostic models, this is a diagnostic/phenotyping tool utilizing multi-class continuous time-series biomechanical data.

## Data Sources
- PhysioNet Gait in Neurodegenerative Disease Database (v1.0.0)
- Zenodo Kinetic & Kinematic Datasets (Records 12793487 & 4630814)

## Repository Structure
- `src/`: Python and SAS source code for data preprocessing, modeling, and visualization.
- `data/`: Directory for the merged dataset files and raw `.ts` sequence files.
- `results/`: End conclusions, model evaluation metrics, and correlation visualizations.

## Methodology
1. **Static Feature Analysis (Random Forest):** Extracts aggregate features (like double support phase and stance interval asymmetry) to find non-linear variables with high predictive importance.
2. **Time-Series Analysis (CNN-LSTM):** Uses sliding windows over raw stride-to-stride temporal sequences to capture the altered fractal dynamics and rhythm degradation associated with neurodegeneration.

# Final Conclusion: Gait Abnormality Research

## Findings
Through our multi-tiered algorithmic approach, we discovered that dynamic gait rhythm—specifically the continuous fluctuations in stride interval and double support phase—acts as a strong phenotypic marker for neurodegenerative conditions and brain injuries.

1. **Static Feature Extraction (Random Forest):** 
   Our ensemble models confirmed that variables such as `double_support_percent` and `stance_interval_asymmetry` contain high non-linear correlation with Parkinson's and Cerebral Palsy. Patients with advanced conditions tend to exhibit a disproportionately large double support phase as a biomechanical compensation for instability.

2. **Time-Series Analysis (CNN-LSTM):** 
   Demonstrated that analyzing raw time-series data outperforms static feature extraction by capturing the "fractal dynamics" of gait. The RNN architecture successfully flagged progressive gait freezing and arrhythmic anomalies that static averages mask, allowing for highly accurate, multi-class predictions across the PhysioNet dataset.
