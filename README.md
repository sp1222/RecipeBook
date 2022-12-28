# RecipeBook

## Summary

A web-based site for managing recipes, built with Flask using Python.

## Run Locally

This method allows you to run the web app locally, given that the requirements are installed as below.

1. Clone the repository.
2. Open with your favorite IDE (I use PyCharm community edition).
3. In the terminal, run `python3 -mpip install requirements.txt` to install required packages from `requirements.txt` to your machine.
4. In the terminal, run `python3 app.py`.
5. In a browser, go to `localhost:5000` to see the home page.

## Run With Docker

This method allows you to run the web app without having to install the necessary requirements to your machine.

1. Clone the repository.
2. Open with your favorite IDE (I use PyCharm community edition).
3. Build the image with `docker build -t image-name .` ensuring there is a period at the end
4. Run the container with `docker run -d -p 5000:5000 image-name` and open a browser.
5. In the browser, go to `localhost:5000` to access the app running in the docker container.

### To Kill a Docker Container

1. Run `docker container ls` to get a list of running containers.
2. Get the `CONTAINER ID` and stop running the container with `docker container stop 123abc` where 123abc is the container ID.
