from PIL import Image, ImageDraw
import argparse

parser = argparse.ArgumentParser(description="Generate circular images with borders")
parser.add_argument("import_path", type=str, help="Input folder containing original images", default="images_in/image.png", nargs="?")
parser.add_argument("export_path", type=str, help="Output folder for saving edited images", default="images_out/image_bordered.png", nargs="?")
args = parser.parse_args()

import_path = args.import_path
export_path = args.export_path

def create_circular_image_with_border(image_path, border_thickness=5, border_color=(150, 150, 150)):
    img = Image.open(image_path).convert("RGBA")
    size = min(img.size)
    img = img.crop(((img.width - size) // 2,
                    (img.height - size) // 2,
                    (img.width + size) // 2,
                    (img.height + size) // 2))
    
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    
    circular_img = Image.new('RGBA', (size, size))
    circular_img.paste(img, (0, 0), mask=mask)
    
    bordered_size = size + border_thickness * 2
    final_img = Image.new('RGBA', (bordered_size, bordered_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(final_img)
    draw.ellipse((0, 0, bordered_size - 1, bordered_size - 1), fill=border_color)
    final_img.paste(circular_img, (border_thickness, border_thickness), mask=mask)
    
    return final_img

circular_image = create_circular_image_with_border(import_path)
circular_image.save(export_path)
