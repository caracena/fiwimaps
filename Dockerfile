FROM ubuntu:15.10
MAINTAINER Claudio Aracena <claudio.aracena2@gmail.com>
RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y build-essential cmake git pkg-config
RUN apt-get install -y libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
RUN apt-get install -y libgtk2.0-dev
RUN apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
RUN apt-get install -y libatlas-base-dev gfortran
ADD get-pip.py /
RUN python get-pip.py
#RUN pip install virtualenv virtualenvwrapper
#RUN export WORKON_HOME=$HOME/.virtualenvs
#RUN bash /usr/local/bin/virtualenvwrapper.sh
#RUN mkvirtualenv cv
RUN apt-get -y install python2.7-dev
RUN pip install numpy
RUN pip install scipy

COPY opencv /src/opencv
COPY opencv_contrib /src/opencv_contrib
WORKDIR /src
RUN cd opencv && mkdir build && cd build &&  cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=OFF \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=/src/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON .. && make -j8 && make install && ldconfig

# install python dependencies
COPY requirements.txt tmp/requirements.txt
RUN pip install -r tmp/requirements.txt

COPY . /src

# run app
CMD ["python", "-u", "fiwiMaps.py"]
