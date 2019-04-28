# scenario_based_testing
This repo explores ways of using meta-programming to run pytest with different scenarios
## First things first
Clone this repo, install python2.7, install pip, install pytest, and desired requirements
### `
    #ensure you have python and its tests dependencies installed
    pip install pytest

`
## How to run the tests
Run the run_test.py to test different scenarios
### `cd tests; pytest run_test.py`

## Running tests with docker
first build the image and run the following command
### `
    #build image called pyfred
    docker build -t pyfred .
    #
    docker run -i -t pyfred
 `
 ## Expected
 two tests passed and one failed, this was intentional in order to fix this just update the scenarios file, or change the test runner file.
