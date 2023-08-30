from PIL import Image

def image_to_ascii_art(img_path: str, output_file: str) -> str:

    img = Image.open(img_path).convert("L")  # convert pic to black and white

    width, height = img.size
    aspect_ratio = height / width
    new_width = 100
    new_height = aspect_ratio * new_width * 0.50
    img = img.resize((new_width, int(new_height)))

    pixels = img.getdata()
    print("PIXELS OF IMAGE: \n",pixels)
    for i in pixels:
        print(i, end=" ")
    chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = "".join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [
        new_pixels[index : index + new_width]
        for index in range(0, new_pixels_count, new_width)
    ]
    ascii_image = "\n".join(ascii_image)

    with open(f"{output_file}.txt", "w") as f:
        f.write(ascii_image)
    return ascii_image

#driver code
image_to_ascii_art("jojo.jpg", "jojo_output")