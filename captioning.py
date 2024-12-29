import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

def getCaption(imageUrl):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

    raw_image = Image.open(requests.get(imageUrl, stream=True).raw).convert('RGB')

    # conditional image captioning
    text = "a photography of"
    inputs = processor(raw_image, text, return_tensors="pt")

    out = model.generate(**inputs)
    return (processor.decode(out[0], skip_special_tokens=True))