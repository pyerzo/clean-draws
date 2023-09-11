**IMAGE THRESHOLD**
===

### **Requirements**

- [Docker](https://www.docker.com)
- [Docker compose](https://github.com/docker/compose)
- [jjanzic/docker-python3-opencv](https://hub.docker.com/r/jjanzic/docker-python3-opencv)

### **Setup**

- Create `.env` file using `.env.sample` as source
- Add allowed types to `ALLOWED_FILES` value using comma as separator
- Add images to `app/source/`
- Run `docker-compose up`
- Get output images from `app/output`
