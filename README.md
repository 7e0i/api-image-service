# romix service
![logo](https://i.ibb.co/4ZqCyhFH/ronix-logo.png)

api for image processing built with fastapi and pillow

## project structure

```text
├── src
│   ├── routes
│   │   ├── health.py
│   │   ├── image.py
│   │   └── processes.py
│   ├── services
│   │   ├── background
│   │   ├── blur
│   │   ├── colorize
│   │   ├── compress
│   │   ├── convert
│   │   ├── crop
│   │   ├── enhance
│   │   ├── filter
│   │   ├── imagedb
│   │   ├── rotate
│   │   ├── size
│   │   └── watermark
│   └── utils
│       ├── __init__.py
│       └── image_utils.py
├── .env
├── .gitignore
├── index.py
├── readme.md
└── requirements.txt
```

## requirements

- <img src="https://img.shields.io/badge/python-3.10+-3776AB?style=flat&logo=python&logoColor=white" height="18">
- <img src="https://img.shields.io/badge/git-latest-F05032?style=flat&logo=git&logoColor=white" height="18">



## installation

```bash
git clone https://github.com/7e0i/api-image-service.git

cd romix-service
python -m pip install -r requirements.txt
```

## configuration

edit `.env` file in the root directory:

```env
port=8000
domain=localhost
app_name="romix service"
app_description="api for image processing"
app_version="0.1.0"
imagedb_path="./data/imagedb"
```

## run

```bash
python index.py
```

server starts at `http://localhost:8000`

interactive docs available at `http://localhost:8000/docs`

## how to customize

### add a new service
1. go to `src/services/<category>/`
2. create your new python file with a processing function
3. register it in `src/routes/processes.py`

### add a new api endpoint
1. open `src/routes/image.py`
2. add a new route:

```python
@router.post("/your-endpoint")
async def your_endpoint(file: UploadFile = File(...)):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("your_operation", img)
    output = image_to_bytes(result, format="PNG")
    return Response(content=output, media_type="image/png")
```

### change port or host
modify `port` or `domain` in `.env` without touching any python code
