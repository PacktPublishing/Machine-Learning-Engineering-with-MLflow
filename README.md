


# Machine Learning Engineering with MLflow

<a href="https://www.packtpub.com/product/Machine-Learning-Engineering-with-MLflow/9781800560796?utm_source=github&utm_medium=repository&utm_campaign=9781800560796"><img src="https://static.packt-cdn.com/products/9781800560796/cover/smaller" alt="Machine Learning Engineering with MLflow" height="256px" align="right"></a>

This is the code repository for [Machine Learning Engineering with MLflow](https://www.packtpub.com/product/Machine-Learning-Engineering-with-MLflow/9781800560796?utm_source=github&utm_medium=repository&utm_campaign=9781800560796), published by Packt.

**Manage the end-to-end machine learning life cycle with MLflow**

## What is this book about?
MLflow is a platform for the machine learning life cycle that enables structured development and iteration of machine learning models and a seamless transition into scalable production environments.

This book will take you through the different features of MLflow and how you can implement them in your ML project. You will begin by framing an ML problem and then transform your solution with MLflow, adding a workbench environment, training infrastructure, data management, model management, experimentation, and state-of-the-art ML deployment techniques on the cloud and premises. The book also explores techniques to scale up your workflow as well as performance monitoring techniques. As you progress, you’ll discover how to create an operational dashboard to manage machine learning systems. Later, you will learn how you can use MLflow in the AutoML, anomaly detection, and deep learning context with the help of use cases. In addition to this, you will understand how to use machine learning platforms for local development as well as for cloud and managed environments. This book will also show you how to use MLflow in non-Python-based languages such as R and Java, along with covering approaches to extend MLflow with Plugins.

By the end of this machine learning book, you will be able to produce and deploy reliable machine learning algorithms using MLflow in multiple environments.

This book covers the following exciting features: 
* Develop your machine learning project locally with MLflow’s different features
* Set up a centralized MLflow tracking server to manage multiple MLflow experiments
* Create a model life cycle with MLflow by creating custom models
* Use feature streams to log model results with MLflow
* Develop the complete training pipeline infrastructure using MLflow features
* Set up an inference-based API pipeline and batch pipeline in MLflow
* Scale large volumes of data by integrating MLflow with high-performance big data libraries

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1800560796) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
import mlflow
from sklearn.linear_model import LogisticRegression
mlflow.sklearn.autolog()
with mlflow.start_run():
  clf = LogisticRegression()
  clf.fit(X_train, y_train)

```

**Following is what you need for this book:**

This book is geared toward software, machine learning, and data science professionals or enthusiasts who want to explore the engineering side of machine learning systems in production. Machine learning practitioners will be able to put their knowledge to work with this practical guide to MLflow. The book takes a hands-on approach to implementation and associated methodologies that will have you up and running with MLflow in no time. The basic requirements for this book are experience in Python programming and knowledge of the Bash terminal and commands.

Ideally, before getting started with the book, you should have a good grasp of the Python programming language and should have already created basic machine learning models. One introductory course in machine learning will help contextualize the concepts discussed in the book.

With the following software and hardware list you can run all code files present in the book (Chapter 1 - 12).

### Software and Hardware List

| Chapter  | Software required                                                                    | OS required                        |
| -------- | -------------------------------------------------------------------------------------| -----------------------------------|
|  1 - 12  |   	Python 3.7+ (MLflow 1.18), Docker                                         			  | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it]( https://static.packt-cdn.com/downloads/9781800560796_ColorImages.pdf).


### Related products <Other books you may enjoy>
* Automated Machine Learning with AutoKeras [[Packt]](https://www.packtpub.com/product/automated-machine-learning-with-autokeras/9781800567641) [[Amazon]](https://www.amazon.com/dp/B08ZT2SP4J)

* Distributed Data Systems with Azure Databricks [[Packt]](https://www.packtpub.com/product/distributed-data-systems-with-azure-databricks/9781838647216) [[Amazon]](https://www.amazon.com/dp/183864721X)

## Get to Know the Author
**Natu Lauchande** is a principal data engineer in the fi ntech space currently tackling problems at the intersection of machine learning, data engineering, and distributed systems. He has worked in diverse industries, including biomedical/pharma research, cloud, fi ntech, and e-commerce/mobile. Along the way, he had the opportunity to be granted a patent (as co-inventor) in distributed systems, publish in a top academic journal, and contribute to open source soft ware. He has also been very active as a speaker at machine learning/tech conferences and meetups.


### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781800560796">https://packt.link/free-ebook/9781800560796 </a> </p>