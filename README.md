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

## Reference 

The open cv installation process was extracted from http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/

The saliency map codes were extracted from https://github.com/mayoYamasaki/saliency-map and http://www.tatome.de/fileadmin/code/saliency.py
