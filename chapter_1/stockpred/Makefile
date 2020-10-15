build-image:
	docker build -t stockpred -f Dockerfile .

run:
	mlflow run .

serve:
 	mlflow models serve -m runs:/my-run-id/model-path &
