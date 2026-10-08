from fastapi import APIRouter, UploadFile, File, Form, Response
from typing import Optional
from src.routes.processes import process
from src.utils.image_utils import bytes_to_image, image_to_bytes

router = APIRouter(tags=["Images"])

@router.post("/background")
async def background(file: UploadFile = File(...), threshold: int = Form(240)):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("background", img, threshold=threshold)
    output = image_to_bytes(result, format="PNG")
    return Response(content=output, media_type="image/png")

@router.post("/enhance")
async def enhance(file: UploadFile = File(...), factor: float = Form(1.5)):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("enhance", img, factor=factor)
    output = image_to_bytes(result, format="PNG")
    return Response(content=output, media_type="image/png")

@router.post("/size")
async def size(file: UploadFile = File(...), width: Optional[int] = Form(None), height: Optional[int] = Form(None)):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("size", img, width=width, height=height)
    output = image_to_bytes(result, format="PNG")
    return Response(content=output, media_type="image/png")

@router.post("/convert")
async def convert(file: UploadFile = File(...), format: str = Form("jpeg")):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("convert", img, format=format)
    output = image_to_bytes(result, format=format)
    return Response(content=output, media_type=f"image/{format.lower()}")

@router.post("/compress")
async def compress(file: UploadFile = File(...), quality: int = Form(75)):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("compress", img, quality=quality)
    output = image_to_bytes(result, format="JPEG", quality=quality)
    return Response(content=output, media_type="image/jpeg")

@router.post("/filter")
async def filter(file: UploadFile = File(...), filter_type: str = Form("grayscale")):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("filter", img, filter_type=filter_type)
    output = image_to_bytes(result, format="PNG")
    return Response(content=output, media_type="image/png")

@router.post("/watermark")
async def watermark(file: UploadFile = File(...), text: str = Form("ROMIX"), opacity: int = Form(128)):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("watermark", img, text=text, opacity=opacity)
    output = image_to_bytes(result, format="PNG")
    return Response(content=output, media_type="image/png")

@router.post("/colorize")
async def colorize(file: UploadFile = File(...), black: str = Form("black"), white: str = Form("white")):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("colorize", img, black=black, white=white)
    output = image_to_bytes(result, format="PNG")
    return Response(content=output, media_type="image/png")

@router.post("/rotate")
async def rotate(file: UploadFile = File(...), degrees: float = Form(90.0)):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("rotate", img, degrees=degrees)
    output = image_to_bytes(result, format="PNG")
    return Response(content=output, media_type="image/png")

@router.post("/crop")
async def crop(file: UploadFile = File(...), left: int = Form(0), top: int = Form(0), right: int = Form(100), bottom: int = Form(100)):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("crop", img, left=left, top=top, right=right, bottom=bottom)
    output = image_to_bytes(result, format="PNG")
    return Response(content=output, media_type="image/png")

@router.post("/blur")
async def blur(file: UploadFile = File(...), radius: float = Form(2.0)):
    contents = await file.read()
    img = bytes_to_image(contents)
    result = process("blur", img, radius=radius)
    output = image_to_bytes(result, format="PNG")
    return Response(content=output, media_type="image/png")