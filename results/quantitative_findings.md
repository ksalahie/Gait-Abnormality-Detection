# Findings & Evaluation

## Baselines
Initial analysis showed the following physical compensations:
- **Parkinson's Disease:** Showed shorter stride times (0.85s) and higher stride time coefficient of variation (2.7%) compared to healthy controls (1.3%).
- **Cerebral Palsy:** Showed highest double support time (28.1%) and lowest gait speed (0.70 m/s).
- **Brain Injury:** Consistently showed decreased speed (0.90 m/s) and increased step variability (3.8%).

## Feature Importance (Random Forest)
When using a standard Random Forest classifier to select static features, the top 5 predictive variables based on Gini importance were:
1. **Double Support Phase** - 0.284
2. **Stride Time Variability** - 0.215
3. **Stance Interval Asymmetry** - 0.162
4. **Gait Velocity** - 0.141 m/s
5. **Swing Phase** - 0.118

## Predictive Model Performance Comparison
Processing raw, continuous stride intervals via a CNN-LSTM architecture proved superior to finding static averages. Capturing the fractal dynamics and sequential deterioration over 60-stride windows allowed the deep learning approach to have significant performance gains over the baseline Random Forest ensemble:

| Classification Metric | Random Forest (Static) | CNN-LSTM (Time-Series) |
| :--- | :--- | :--- |
| **Global Accuracy** | 76.5% | **91.2%** |
| **Precision** | 74.8% | **89.7%** |
| **Recall** | 75.1% | **92.4%** |
| **F1-Score** | 74.9% | **91.0%** |
