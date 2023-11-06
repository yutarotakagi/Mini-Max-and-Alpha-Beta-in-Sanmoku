# Note: You can use any Debian/Ubuntu based image you want. 
FROM python:3.10.11

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
RUN python -m pip install --upgrade pip

WORKDIR /workspace

COPY requirements.txt /workspace/

RUN pip install -r requirements.txt

ENV JUPYTER_ENABLE_LAB = yes
