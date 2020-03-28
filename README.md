# Hack The Crisis - Covitbot

The cloud functions are in `cloud_functions/main.py``

They can be unit tested locally as follows:

(assumes installation of Docker)

````bash
$ ./bin/build_img.sh
[...]
Successfully tagged chatbot-functions:latest

$ ./bin/test_functions.sh
[...]
== 2 passed in 0.35s ==
````

For the moment, deployment of the cloud functions to Google Cloud is done manually.
