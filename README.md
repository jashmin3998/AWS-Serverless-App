# AWS-Serverless-App

The task is to create a serverless application using React js, AWS services : API Gateway, Lambda functions, DynamoDB, S3. 

## AWS Configuration steps:
# S3 Bucket
1.  create a bucket and give the accesss to putObject.
2.  upload a script.py file to the bucket and give access to EC2 so it run it.

# API Gateway
1.  create new API Gateway and choose REST API option.
2.  create a POST method with intigration type lambda and select uploadFileHandle function.
3.  After creation, enable CORS and deploy that.
4.  copy the URL to send the post request and attach at frontend side.

# Lambda - uploadFileHandle
1.  create above lambda function which will be triggered by API Gateway POST method.
2.  follow the python code and refer the comments.

# DynamoDB
1.  create a table under DynamoDB.
2.  Update setting >> Export and Stream >> Trigger - enable it with lambda triggerByDB.
3.  follow the python code and refer the comments.

# Lambda - triggerByDB
1.  create above lambda function which will be triggered by DynamoDB.
2.  follow the python code and refer the comments.

## Note: 
-   Use IAM role to configure all the services as per AWS best practices.
-   Manage the roles for lambda and EC2 instance.
-   Give only required permission at all.




## Frontend Installation and Deployment:

1.	Clone the UI system into a directory on your system using the below Github link.
2.	via SSH: > git clone git@github.com:jashmin3998/Stock_Trading_UI.git 
3.	via HTTPS: > git clone https://github.com/jashmin3998/Stock_Trading_UI.git
4.	change BaseApiURL in axios.js to communicate with API Gateway and bucket name to upload file to S3 bucket.
5.	set your AWS Access key and Seceret Access key.
6.	Install npm and Run 'npm run build' command. It creates the build directory in the project folder.
7.	Create S3 bucket in AWS with public access permission.
8.	Under configuration, select host a web-site option and enter a index page.
9.	After submitting, copy the url.
10.	Ready to hit the system URL from browser.


