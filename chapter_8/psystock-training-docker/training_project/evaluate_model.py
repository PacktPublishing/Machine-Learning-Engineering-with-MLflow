import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.metrics import  \
    classification_report, \
    confusion_matrix, \
    accuracy_score, \
    auc, \
    average_precision_score, \
    balanced_accuracy_score, \
    f1_score, \
    fbeta_score, \
    hamming_loss, \
    jaccard_score, \
    log_loss, \
    matthews_corrcoef, \
    precision_score, \
    recall_score, \
    zero_one_loss


def classification_metrics(df:None):
    metrics={}
    metrics["accuracy_score"]=accuracy_score(df["y_pred"], df["y_test"]  )
    metrics["average_precision_score"]=average_precision_score( df["y_pred"], df["y_test"]  )
    metrics["f1_score"]=f1_score( df["y_pred"], df["y_test"]  )
    metrics["jaccard_score"]=jaccard_score( df["y_pred"], df["y_test"]  )
    metrics["log_loss"]=log_loss( df["y_pred"], df["y_test"]  )
    metrics["matthews_corrcoef"]=matthews_corrcoef( df["y_pred"], df["y_test"]  )
    metrics["precision_score"]=precision_score( df["y_pred"], df["y_test"]  )
    metrics["recall_score"]=recall_score( df["y_pred"], df["y_test"]  )
    metrics["zero_one_loss"]=zero_one_loss( df["y_pred"], df["y_test"]  )
    return metrics
    
if __name__ == "__main__":

    with mlflow.start_run(run_name="evaluate_model") as run:
        mlflow.set_tag("mlflow.runName", "evaluate_model")
        df=pd.read_csv("data/predictions/test_predictions.csv")
        metrics = classification_metrics(df)
        mlflow.log_metrics(metrics)