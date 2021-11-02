"""Utilities for exploratory data analysis, preprocessing and model validation."""


# =============================================================================
# Imports
# =============================================================================

# Third party
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.utils.multiclass import unique_labels
import pandas as pd
import plotly.figure_factory as ff


# =============================================================================
# Functions
# =============================================================================

def fit_evaluate(estimator, X_train, X_test, y_train, y_test):
    """Fit the estimator to the training dataset and evaluate in the testing dataset."""
    # Build the estimators from the training dataset
    estimator = estimator.fit(X_train, y_train)

    # Predict the classes for the testing dataset
    predictions = estimator.predict(X_test)

    # Build a text report (in a dictionary) showing the main classification metrics
    report = classification_report(y_test, predictions, output_dict=True)

    # Convert the report to a tabular representation
    report = pd.DataFrame(report).T

    # Compute the confusion matrix to evaluate the accuracy of a classification
    matrix = confusion_matrix(y_test, predictions)

    # Extract an ordered array of unique labels
    out = unique_labels(y_test, predictions)

    # Convert the unique labels to a list 
    x = y = list(out)

    # Create a figure with annotations to each cell of the heatmap
    matrix = ff.create_annotated_heatmap(matrix, x=x, y=y)

    # Define the label for the columns (predictions)
    xaxis = {"title": "Predicted label"}

    # Define the label for the rows (true classes) 
    yaxis = {"title": "True label"}

    # Update the confusion matrix to show the labels
    matrix.update_layout(xaxis=xaxis, yaxis=yaxis)

    return estimator, predictions, report, matrix