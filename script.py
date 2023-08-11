from fastapi import FastAPI, UploadFile, File
from rembg import remove
from PIL import Image
import io

app = FastAPI()

@app.post("/remove_background/")
async def remove_background(image: UploadFile = File(...)):
    try:
        # Load the uploaded image using PIL
        image_bytes = await image.read()
        input_image = Image.open(io.BytesIO(image_bytes))

        # Remove background using rembg
        output_image = remove(input_image)

        # Save the output image to a BytesIO buffer
        output_buffer = io.BytesIO()
        output_image.save(output_buffer, format='PNG')
        output_buffer.seek(0)

        return {"image": output_buffer}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
