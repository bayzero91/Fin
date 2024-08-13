# Final_Project
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