package ai.psystock.jclient;

import org.mlflow.tracking.MlflowClient;
import org.mlflow.tracking.MlflowContext;
import org.mlflow.api.proto.Service.RunInfo;
import org.mlflow.api.proto.Service.RunStatus;
import org.mlflow.api.proto.Service.CreateRun;


import java.io.File;
import java.io.PrintWriter;

public class Main {
    public static void main(String[] args) {

        MlflowClient mlflowClient=new MlflowClient();
        String runId="test";
        RunStatus runStatus = RunStatus.FINISHED;
        
        MlflowContext mlflowContext = new MlflowContext();
        MlflowClient client = mlflowContext.getClient();
        
        client.logParam("test","alpha", "0.5");
        client.logMetric("test","rmse", 0.786);
        client.setTag("test","origin","HelloWorldFluent Java Example");

         mlflowClient.setTerminated(runId, runStatus, System.currentTimeMillis());
    }
}
