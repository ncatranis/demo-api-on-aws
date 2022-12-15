# Demo Project: Deploy a Service to AWS Lambda

## Problem Statement: 
Write a service that will receive a string as input, 
potentially a mixture of upper and lower case, numbers, special characters etc. 
The task is to determine if the string contains at least one of each letter of the alphabet. 
Return true if all are found and false if not. 
Write it as a RESTful web service (no authentication necessary) and document the service. 
Describe how you would deploy this application into AWS, 
including which AWS services you would use, and what deployment method or tools.

## About my solution
I wrote a simple Python/Flask service, and in order to deploy it to the internet I used 
[serverless.com's framework](https://serverless.com), where I am using AWS Lambda as the provider. 
I chose this method because going with a managed provider suited my needs very well: get this service online in under
an hour, make sure its secure, easy to debug and monitor, and easy to tear down. 
Choosing a pay-per-request model made sense for me since I will only be calling this service a few times, and don't want
to pay for unused compute time by renting an EC2 instance. While I could have tinkered with terraform, a CI/CD pipeline,
docker, and other technologies, due to my experience I knew it would take me a bit of time to get everything set up in
a satisfactory way.


## Future Considerations
There are many ways to approach deploying a web application on AWS or another cloud provider, and the best approach
depends on customer/client needs. Here are some example questions I'd want to ask:
* What problem are we trying to solve? Is there a product roadmap?
* What are our expectations for scalability and traffic patterns? 
* Are we restricted in our technology choices? (this could be due to regulations, deal-breakers for a client, etc.)
* Is there anything we're anticipating to deal with in the future that is worth considering but isn't pressing right now?
* What provider does the client use/need? Do they need an on-prem or offline-first solution?
  * At Indeed we used AWS, had many different internal services for self provisioning,
  and a jenkins pipeline for CI/CD. Indeed also had a philosophy of microservices, A/B testing and data collection.
  * At Gecko we used GCP for internal services and on-prem for govt services handling classified information. Each team
  had to figure out CI/CD on their own, and there were 3 main monoliths in the company with no A/B tests. 
  My team dealt with locally hosted python notebooks with plans to deploy with k8s in the far future so that we could 
  have both a cloud hosted and on-prem solution for customers.
* What release process do they want to follow? What about rollbacks?
  * The client may be okay with things breaking and then manually fixing them. 
  This could also be completely unacceptable.
* Does the client want staging, QA, and production environments? Branch deployments? Canary deploys?


## Local Setup (Simple server)
My API is written using Python/Flask.
### To run a local dev server:
1. Create a virtual environment and install package requirements
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Run the server using Flask's dev server
```shell
python3 app.py
```
You should see the following output
```shell
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
```
3. Test it.
```shell
pytest
```
Your output should look something like this
```shell
==== test session starts ====
platform darwin -- Python 3.9.12, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/nick/Desktop/demo-api-on-aws
plugins: anyio-3.6.1
collected 6 items                                                                                                                                                                   

tests/functional/test_endpoints.py ..                                                                                                                                         [ 33%]
tests/unit/test_lib.py ....                                                                                                                                                   [100%]

==== 6 passed in 0.26s ====
```

# Serverless Deploys
## Local setup (serverless.com framework)
I am using serverless.com's framework to manage my applications deploys to AWS. 
This is mainly to save time and for convenience, as it handles a LOT out of the box.
In a more professional environment, it may be prudent to run a custom solution with docker, terraform, 
and a CI/CD platform such as Jenkins.

1. Install node using [nvm](https://github.com/nvm-sh/nvm)
2. Install serverless framework's cli with `npm install -g serverless`
3. Install plugins
```shell
npm i
```
4. Set up the python virtual environment and install requirements (if you didn't do this already)
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
5. Serve the app locally using serverless framework
```shell
serverless wsgi serve -p 8000
```
Note 1: the port is set to 8000 since the default is 5000, which may be reserved on Mac/OSX.

Note 2: you may need to go to 127.0.0.1 instead of localhost

## Configure for remote deploys
In my case, I used Serverless Dashboard to manage AWS credentials instead of manually creating accounts and setting
permissions (see [this page](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)
that compares both methods). 

To make this work on your machine, do the following:
1. Go to [app.serverless.com] and sign up for an account
2. Go to 'org' -> 'providers' -> and add a new AWS provider. Give it any name you want.
3. in `serverless.yml`, remove these lines
```shell
org: ncatranis
app: demo-api-on-aws
```
4. run `serverless login` and choose the dashboard option.
5. run `serverless` to configure the project and deploy it

## Deploy changes
1. First, run tests.
```shell
source venv/bin/activate
pytest
```
2. Then, deploy.
```shell
serverless deploy
```
Use the link in the output to see the service live in action!
My URL (subject to change) is [https://5ckrdljpn1.execute-api.us-east-1.amazonaws.com/dev/]
