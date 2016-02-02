# Saliency maps for fiwi dataset

## How to use it

- [Install docker](https://docs.docker.com/linux/)

- Clone this repo and inside of it clone these two repos: 
```
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout 3.1.0
cd ..
git clone https://github.com/Itseez/opencv_contrib.git
cd opencv_contrib
git checkout 3.1.0
cd ..
```

- Paste folder with [stimuli images](https://www.ece.nus.edu.sg/stfpage/eleqiz/webpage_saliency.html) inside this repo (folder name has to be `stimuli`)

- Build image
```
docker build -t fiwimaps .
```

- Run container: This is going to generate saliency maps files (txt) in /app folder in your host machine. 
```
docker run -v /app:/src/results fiwimaps 
```

- Run container in command line: You can access to the container environment and playing around. Code inside the container and if you want to extract your work from it, just dump it in the /src/results folder and look for it in /app in your host machine.
```
docker run -v /app:/src/results -ti fiwimaps bash
```

## How to use with image from docker hub

- Pull image from docker hub
```
docker pull caracena/fiwimaps
```

- Run container
```
docker run -v /app:/src/results caracena/fiwimaps
```

## How to create reduced fixation matrix files

The steps for doing this process are similar than the steps for creating saliency maps:

- Include the folder with fixation files for each subject and page (also you can do it with aggregate fixation files for all users for a page) 
- Build the image as same as before
```
docker build -t fiwimaps .
```
- Run the container but now the volume where the files will be published is different (folder app in your host machine will be overwritten)
```
docker run -ti -v /app:/src/matrix fiwimaps bash 
```
- When you are inside of the container run the script
```
python filestoredumatrix.py
```
The output will be a log of which files are being processed and you have to check app folder to the output files


## Reference 

The open cv installation process was extracted from http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/

The saliency map codes were extracted from https://github.com/mayoYamasaki/saliency-map and http://www.tatome.de/fileadmin/code/saliency.py
