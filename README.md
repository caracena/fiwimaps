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

- Paste folder with [stimuli images](https://www.ece.nus.edu.sg/stfpage/eleqiz/webpage_saliency.html) inside this repo

- Build image
```
docker build -t fiwimaps .
```

- Run container
```
docker run -v /app:/src/results -ti fiwimaps bash
```

- Code inside the container and if you want to extract your work from it, just dump it in the /src/results folder and look for it in /app in your host machine.


## How to use with image from docker hub (coming soon)

- Run container
```
docker run -v /app:/src/results -ti caracena/fiwimaps bash
```

