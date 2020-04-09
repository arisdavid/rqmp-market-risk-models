## Market Risk Models

### Introduction
Sample models to execute on the platform


### Build a docker image

```
docker build -t market-risk-models:latest .
```

### Execute manually
```
docker run -it market-risk-models:latest python3 main.py gbm 1000 200 0.2 0.18 365 250

```