# data_engineering2026
Datatalksclub DE 2026 zoomcamp - Module 1
- Docker is a lean-er 'bash/command line-oriented' virtual machine.
- Can use various images from ubuntu to python
- Docker allow us to provide a simple mechanism to reproduce container for coding

Linux bash customization
- To shorten/customized bash prompt at every 'terminal' instance use:
- PS1=">" \\ This is to change the default prompt to just '>'
- add the line to .bashrc
- echo 'PS1=">"' > ~/.bashrc

Docker
- To check if docker is installed
    docker --version
- To run some simple containers
    1. docker run hello-world
    or 
    2. docker run ubuntu
    or
    3. docker run python3
    etc
- To run things interactively add -it flags
    1. docker run -it ubuntu
- To run specific images, add tags 
    1. docker run -it python:3.13.11-slim
- To run python using bash entry point
    1. docker run -it --entrypoint=bash python:3.13.11-slim
- Docker is stateless, shouldnt continue working on the same state/snapshot
- But there are stopped snapshot
    1. docker ps -a \\ Check all stopped snapshots
    2. docker ps -aq \\ Check only container ids
    3. docker start <container_name_or_id>
- For more details ask LLM for variety ways to restart a stopped/saved previous snapshots
- To free storages and remove previously stopped snapshots/environementsdocke use rm flag
    1. docker rm `docker ps -aq`
- We can restore/recreate/reproduce any 'environment' using docker

- But how do we access files on host-machine from our environment?
- This can be accomplished using volumes using -v flags, host directory is specified to the left of the colon while container dir is specified to the right of the colon, using the following example:
    1. docker run -it --entrypoint=bash -v $(pwd)/test:/app/test python:3.13.11-slim

- Data pipeline/parameterizing python calls
    1. Checkout pipeline.py