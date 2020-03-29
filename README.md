# Hack The Crisis - Covidbot

The cloud functions are in `cloud_functions/main.py`

## How to run unit tests

(assumes Docker is installed)

````bash
$ ./bin/build_img.sh
[...]
Successfully tagged chatbot-functions:latest

$ ./bin/test_functions.sh
[...]
== 2 passed in 0.35s ==
````

## How to prepare timestamped ZIP file for deployment

````bash
$ ./bin/prepare_zip.sh
[...]
````

For the moment, deployment Google Cloud Platform and Twilio is done manually.
