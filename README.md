
Starting tutorial dockerizing flask

ERROR: Docker Desktop requires Windows 10 Pro or Enterprise version 14393 to run.

SOLUTION: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v

(Remember to enable Hiper-V)


## Installing Docker on Windows 10 Home


https://forums.docker.com/t/installing-docker-on-windows-10-home/11722/26
Is not easy to doit: new license, some cool hacking...

Try to install ububtu... also problems with this laptop
https://askubuntu.com/questions/946480/installing-ubuntu-alongside-windows-on-lenovo-yoga-720


## Ill try with VM and Docker-toolbox

Since it seems that virtualization is already enabled

https://www.virtualbox.org/wiki/Downloads
https://github.com/docker/kitematic/releases

And last docker-toolbox
https://github.com/docker/toolbox/releases



https://blog.theodo.fr/2015/04/docker-and-virtualenv-a-clean-way-to-locally-install-python-dependencies-with-pip-in-docker/

https://stackoverflow.com/questions/49631146/how-do-you-add-a-path-to-pythonpath-in-a-dockerfile



Modified requirements to previous version of wezkeru

docker rm $(docker ps -a -f status=exited -q)



