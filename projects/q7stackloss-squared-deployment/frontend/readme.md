## Build the image

```bash
docker build -t berry2012/ui-q7stackloss-quadratic-model:v1 .
```

## Run container locally

```bash
docker run -d --name ui -p 8501:8501 berry2012/ui-q7stackloss-quadratic-model:v1 
```

## test the app from the browser

```bash
http://0.0.0.0:8501