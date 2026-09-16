/* 
SAS Data Visualization 
Visualizes the highly correlated variables extracted from the Random Forest model
*/

PROC IMPORT DATAFILE="../data/merged_gait_dataset.csv" 
    OUT=gait_data 
    DBMS=CSV 
    REPLACE; 
    GETNAMES=YES; 
RUN;

ODS GRAPHICS ON;

/* Correlation Matrix */
TITLE "Correlation Matrix of Gait Biomechanics";
PROC CORR DATA=gait_data PLOTS=MATRIX(HISTOGRAM);
    VAR stride_interval_sec swing_interval_percent stance_interval_percent double_support_percent step_length_asymmetry;
RUN;

/* Comparative Boxplot */
TITLE "Double Support Time Distribution by Neurological Condition";
PROC SGPLOT DATA=gait_data;
    VBOX double_support_percent / CATEGORY=condition GROUP=condition DATASKIN=GLOSS;
    XAXIS LABEL="Neurological Condition";
    YAXIS LABEL="Double Support Phase (% of Gait Cycle)";
RUN;

ODS GRAPHICS OFF;
