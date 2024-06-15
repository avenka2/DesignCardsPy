from PIL import Image, ImageDraw, ImageFont
import textwrap

class LineInfo:
    def __init__(self, textbox_width, x, y, font_size, bold, color, justify, invert, line_type, text):
        self.textbox_width = textbox_width
        self.x = x
        self.y = y
        self.font_size = font_size
        self.bold = bold
        self.color = color
        self.justify = justify
        self.invert = invert
        self.line_type = line_type
        self.text = text

# Create LineInfo objects for each line
line_info_list = [
    # textbox_width, x, y, font_size, bold, color, justify, invert, line_type, text
    LineInfo(250, 15, 15, 100, True, 'black', 'Left', False, "header", "10"),
    LineInfo(250, 0, 65, 100, True, 'orange', 'center', False, "text", "Training"),
    LineInfo(400, 0, 200, 35, True, 'black', 'center', False, "text", "अभयं सत्त्वसंशुद्धिर्ज्ञानयोगव्यवस्थिति: | दानं दमश्च यज्ञश्च स्वाध्यायस्तप आर्जवम् || अहिंसा सत्यमक्रोधस्त्याग: शान्तिरपैशुनम् | दया भूतेष्वलोलुप्त्वं मार्दवं ह्रीरचापलम् ||  तेज: क्षमा धृति: शौचमद्रोहोनातिमानिता | भवन्ति सम्पदं दैवीमभिजातस्य भारत ||"),
    LineInfo(290, 0, 600, 30, True, 'black', 'center', False, "text", "These saintly virtues are practices that prepares one for freedom by focussing your mind. fearlessness, noble thoughts, commitment to learning, generosity, sense-control, sacrifice, simple life, honesty,non-violence, truthfullness, calm, peace, detachment, and avoid fault finding with others."),
    LineInfo(250, 0, 960, 70, True, 'yellow', 'center', False, "text", "Karma Yoga"),
    LineInfo(750, 620, 1020, 100, True, 'black', 'Left', True, "footer", "10"),
]


from PIL import Image

from PIL import Image, ImageDraw

def round_corners(image, radius):
    """
    Rounds the corners of a PIL Image.

    Parameters:
        image: The image to round.
        radius: The radius of the rounded corners.

    Returns:
        The image with rounded corners.
    """
    # Create a mask of the same size as the image
    mask = Image.new('L', image.size, 0)

    # Draw four filled circles of the specified radius in the corners of the mask
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
    draw.ellipse((image.width - radius * 2, 0, image.width, radius * 2), fill=255)
    draw.ellipse((0, image.height - radius * 2, radius * 2, image.height), fill=255)
    draw.ellipse((image.width - radius * 2, image.height - radius * 2, image.width, image.height), fill=255)

    # Draw four rectangles to fill in the rest of the mask
    draw.rectangle((radius, 0, image.width - radius, image.height), fill=255)
    draw.rectangle((0, radius, image.width, image.height - radius), fill=255)

    # Apply the mask to the image
    result = Image.new('RGBA', image.size)
    result.paste(image, mask=mask)

    return result



def main():
    # Create a blank white image
    # width and height for a standard playing card at 300 dpi
    width, height = 750, 1127
    img = Image.new('RGBA', (width, height))

    # Load an image
    bk_img = Image.open('background.jpg')

    # Define the size of the border
    border_size = 15  # Adjust this value to change the size of the border

    # Resize the background image to be slightly smaller than the main image
    bk_img = bk_img.resize((width - 2*border_size, height - 2*border_size), Image.ANTIALIAS)

   # Round the corners of the background image
    #bk_img = round_corners(bk_img, 50)  # Adjust the radius as needed



    # Set the floodfill parameters
    seed = (10, 10)  # The starting point
    fill_color = (255, 0, 0)  # The replacement color

    bk_img = bk_img.convert("RGB")

    # Perform the floodfill
    ImageDraw.floodfill(bk_img, seed, fill_color)


    # Convert the images to 'RGBA' mode
    img = img.convert("RGBA")
    bk_img = bk_img.convert("RGBA")

    # Overlay the background onto the existing image, centered to create a border
    img.paste(bk_img, (border_size, border_size))


    # Draw the text on the image
    for line_info in line_info_list:
        # Load the font with the size from LineInfo
        font = ImageFont.truetype('NotoSansDevanagari-Bold.ttf', line_info.font_size)

        # Create a draw object
        d = ImageDraw.Draw(img)

        # Define the initial position for the text
        pos = (0, line_info.y)
        

        lines = textwrap.wrap(line_info.text, width=(line_info.textbox_width - line_info.x)//font.getsize(' ')[0])
        
        # Ensure 9 lines are returned
        if len(line_info.text) > 30 and len(lines) < 9:
            padding_lines = 9 - len(lines)
            lines = [" " * (len(lines[0]) // 2)] * (padding_lines // 2) + lines + [" " * (len(lines[0]) // 2)] * (padding_lines - padding_lines // 2)


        for line in lines:
            # Calculate the width of the line and adjust the position
            line_width = font.getsize(line)[0]
            if line_info.justify == 'center':
                pos = ((width - line_width) // 2 + line_info.x, pos[1])
            elif line_info.justify == 'right':
                pos = (width - line_width - line_info.x, pos[1])
            else:  # left
                pos = (line_info.x, line_info.y)

            # Check if the text should be inverted
            if line_info.invert:
                # Create a new image for the text
                text_img = Image.new('RGB', (line_width, font.getsize(line)[1]), color = 'red')
                text_d = ImageDraw.Draw(text_img)

                # Draw the text on the new image
                text_d.text((0, 0), line, fill=line_info.color, font=font)

                # Rotate the image
                text_img = text_img.rotate(180)

                # Paste the rotated image on the main image
                img.paste(text_img, pos)
            else:
                d.text(pos, line, fill=line_info.color, font=font)

            pos = (line_info.x, pos[1] + font.getsize(line)[1])

        pos = line_info.x, pos[1] + line_info.y

    # Save the image
    img.save('text_box.png')

if __name__ == "__main__":
    main()
