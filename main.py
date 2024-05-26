from PIL import Image, ImageDraw, ImageFont
import textwrap

class LineInfo:
    def __init__(self, textbox_width, top_padding, bottom_padding, left_padding, right_padding, font_size, bold, color, justify, invert, line_type, text):
        self.textbox_width = textbox_width
        self.top_padding = top_padding
        self.bottom_padding = bottom_padding
        self.left_padding = left_padding
        self.right_padding = right_padding
        self.font_size = font_size
        self.bold = bold
        self.color = color
        self.justify = justify
        self.invert = invert
        self.line_type = line_type
        self.text = text

# Create LineInfo objects for each line
line_info_list = [
    # textbox_width, top_padding, bottom_padding, left_padding, right_padding, font_size, bold, color, justify, invert, line_type, text
    LineInfo(250, 10,  10, 30, 10, 100, True, 'black', 'Left', False, "header", "10"),
    LineInfo(350, 50, 60, 10, 10, 100, True, 'black', 'center', False, "text", "Purification"),
    LineInfo(350, 10,  50, 10, 10, 25, True, 'black', 'center', False, "text", "नासतो विद्यते भावो नाभावो विद्यते सत: |  उभयोरपि दृष्टोऽन्तस्त्वनयोस्तत्त्वदर्शिभि: ||"),
    LineInfo(350, 0,  0, 10, 10, 25, True, 'black', 'center', False, "text", "नासतो विद्यते भावो नाभावो विद्यते सत: |  उभयोरपि दृष्टोऽन्तस्त्वनयोस्तत्त्वदर्शिभि: ||"),
    LineInfo(350, 0,  50, 10, 10, 25, True, 'black', 'center', False, "text", "नासतो विद्यते भावो नाभावो विद्यते सत: |  उभयोरपि दृष्टोऽन्तस्त्वनयोस्तत्त्वदर्शिभि: ||"),
    LineInfo(350, 40,  100, 10, 10, 25, True, 'black', 'center', False, "text", "BG 13.8-12: Humbleness; freedom from hypocrisy; non-violence; forgiveness; simplicity; service of the Guru; cleanliness of body and mind; steadfastness; and self-control; dispassion toward the objects of the senses; absence of egotism; keeping in mind the evils of birth, disease, old age, and death; non-attachment; absence of clinging to spouse, children, home, and so on; even-mindedness amidst desired and undesired events in life"),
    LineInfo(750, 100,  0, 640, 10, 100, True, 'black', 'Left', True, "footer", "10"),
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
    width, height = 750, 1050
    img = Image.new('RGBA', (width, height), color='gold')

    # Load an image
    bk_img = Image.open('background.jpg')

  #   # Define the size of the border
    border_size = 0  # Adjust this value to change the size of the border

  #   # Resize the background image to be slightly smaller than the main image
  #   bk_img = bk_img.resize((width - 2*border_size, height - 2*border_size), Image.ANTIALIAS)

  #  # Round the corners of the background image
  #   bk_img = round_corners(bk_img, 50)  # Adjust the radius as needed


  #   # Convert the images to 'RGBA' mode
  #   img = img.convert("RGBA")
  #   bk_img = bk_img.convert("RGBA")

    # Overlay the background onto the existing image, centered to create a border
    img.paste(bk_img, (border_size, border_size))

    # Define the initial position for the text
    pos = (0, 50)

    # Draw the text on the image
    for line_info in line_info_list:
        # Load the font with the size from LineInfo
        font = ImageFont.truetype('NotoSansDevanagari-Bold.ttf', line_info.font_size)

        # Create a draw object
        d = ImageDraw.Draw(img)

        # Adjust position for header and footer
        if line_info.line_type == "header":
            pos = (line_info.left_padding, line_info.top_padding)
        elif line_info.line_type == "footer":
            pos = (line_info.left_padding, height - line_info.bottom_padding - line_info.font_size)
        else:
            pos = (line_info.left_padding, pos[1]+line_info.top_padding)

        lines = textwrap.wrap(line_info.text, width=(line_info.textbox_width - line_info.left_padding - line_info.right_padding)//font.getsize(' ')[0])
        for line in lines:
            # Calculate the width of the line and adjust the position
            line_width = font.getsize(line)[0]
            if line_info.justify == 'center':
                pos = ((width - line_width) // 2, pos[1])
            elif line_info.justify == 'right':
                pos = (width - line_width - line_info.right_padding, pos[1])
            else:  # left
                pos = (line_info.left_padding, pos[1])

            # Check if the text should be inverted
            if line_info.invert:
                # Create a new image for the text
                text_img = Image.new('RGB', (line_width, font.getsize(line)[1]), color = (255,192,0))
                text_d = ImageDraw.Draw(text_img)

                # Draw the text on the new image
                text_d.text((0, 0), line, fill=line_info.color, font=font)

                # Rotate the image
                text_img = text_img.rotate(180)

                # Paste the rotated image on the main image
                img.paste(text_img, pos)
            else:
                d.text(pos, line, fill=line_info.color, font=font)

            pos = (line_info.left_padding, pos[1] + font.getsize(line)[1])

        pos = line_info.left_padding, pos[1] + line_info.bottom_padding

    # Save the image
    img.save('text_box.png')

if __name__ == "__main__":
    main()
