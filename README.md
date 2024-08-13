# Final_Project

This project is a showcase from my training at the Data Science Institute, where I aimed to highlight the capabilities that arise when you combine 8 years of professional experience as an Industrial Engineer with newly acquired Data Science skills.

I selected a dataset from Kaggle.com that contains process data from a specific machine. In addition to following the standard Data Science and Machine Learning pipeline, I developed a Key Performance Indicator (KPI) from the data to support further optimization. 

The results were visualized using Streamlit in an initial mock-up, demonstrating the potential for creating customized dashboards. For a clearer understanding, I recommend viewing the files in the following order:

1. Roasting_Machine_V2
2. OEE_Data
3. OEE_Dashboard + quality_prediction_app (You’re welcome to try running the code on your own server).

# Project description:

## Predictive Quality - Production of roastied coffee

### About Dataset:
Context:

You need to build a model that, on the basis of data arriving every minute, determines the quality of products produced on a roasting machine.

Content:

The roasting machine is an aggregate consisting of 5 chambers of equal size, each chamber has 3 temperature sensors. In addition, for this task, you have collected data on the height of the raw material layer and its moisture content. Layer height and humidity are measured when raw materials enter the machine. Raw materials pass through the kiln in an hour.

Acknowledgements:

Product quality is measured in the laboratory by samples that are taken every hour, data on known analyzes are contained in the file data_Y.csv. The file indicates the time of sampling, the sample is taken at the exit of the roasting machine.

Inspiration:

You agreed with the customer that the model will be estimated by the MAE indicator, to evaluate the model, it is necessary to generate predictions for the period specified in the file sample_submission.csv (5808 predictions).