from PIL import Image, ImageDraw, ImageFont
import textwrap

class CardInfo:
    def __init__(self, yoga, color, number, title, vno, vdesc, sanskrit):
        self.yoga = yoga
        self.color = color
        self.number = number
        self.title = title
        self.vno = vno
        self.vdesc = vdesc
        self.sanskrit = sanskrit

card_deck = [
    CardInfo("Jnana Yoga","Yellow","0","ignorance","2.42","lost in misunderstanding, many are: Crave for fame, power, gold and sense pleasures in exhchange for rituals the books prescribe, but miss the deeper truth they hide. Through wisdom and compassion, the truth we connect, not through passion and selfish effect.","यामिमां पुष्पितां वाचं प्रवदन्त्यविपश्चित: | वेदवादरता: पार्थ नान्यदस्तीति वादिन: || कामात्मान: स्वर्गपरा जन्मकर्मफलप्रदाम् | क्रियाविशेषबहुलां भोगैश्वर्यगतिं प्रति ||"),
    CardInfo("Jnana Yoga","Yellow","10","Enlightenment","4.24,3.17","Completely one with God-consciousness is such a one for whom: the offering is Brahman, the ladle with which it is offered is Brahman, the act of offering is Brahman, and the sacrificial fire is also Brahman. They understand the mystery of one appearing as infinitely many!","ब्रह्मार्पणं ब्रह्म हविर्ब्रह्माग्नौ ब्रह्मणा हुतम् | ब्रह्मैव तेन गन्तव्यं ब्रह्मकर्मसमाधिना || यस्त्वात्मरतिरेव स्यादात्मतृप्तश्च मानव: | आत्मन्येव च सन्तुष्टस्तस्य कार्यं न विद्यते ||"),
    CardInfo("Jnana Yoga","Yellow","AV","Avatar","4.7","Whenever there is a decline in righteousness and an increase in unrighteousness O Arjun at that time I manifest Myself on earth. ","यदा यदा हि धर्मस्य ग्लानिर्भवति भारत | अभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम्  ||"),
]

class CardInfoLayout:
    def __init__(self, textbox_width, x, y, font_size, bold, color, justify, invert, text):
        self.textbox_width = textbox_width
        self.text_type = text
        self.x = x
        self.y = y
        self.font_size = font_size
        self.bold = bold
        self.color = color
        self.justify = justify
        self.invert = invert


# Create CardInfoLayout objects for each line
card_info_layouts = [
    # textbox_width, x, y, font_size, bold, color, justify, invert, line_type, text
    CardInfoLayout(250, 25, 15, 100, True, 'black', 'Left', False, "number"),
    CardInfoLayout(300, 15, 65, 60, True, 'orange', 'center', False, "title"),
    CardInfoLayout(400, 0, 200, 35, True, 'black', 'center', False, "sanskrit"),
    CardInfoLayout(290, 0, 600, 30, True, 'black', 'center', False, "vdesc"),
    CardInfoLayout(250, 0, 960, 70, True, 'yellow', 'center', False, "yoga"),
]

def color_to_rgb(color_name):
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        # add more colors here
    }
    return colors.get(color_name.lower(), (0, 0, 0))  # return black if the color is not found


def main():
    for card_info in card_deck:
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



        fill_color = color_to_rgb(card_info.color)

        bk_img = bk_img.convert("RGB")

        # Perform the floodfill
        ImageDraw.floodfill(bk_img, seed, fill_color)


        # Convert the images to 'RGBA' mode
        img = img.convert("RGBA")
        bk_img = bk_img.convert("RGBA")

        # Overlay the background onto the existing image, centered to create a border
        img.paste(bk_img, (border_size, border_size))
        

        # Draw the text on the image
        for card_info_layout in card_info_layouts:
          # Load the font with the size from CardInfoLayout
          font = ImageFont.truetype('NotoSansDevanagari-Bold.ttf', card_info_layout.font_size)

          # Create a draw object
          d = ImageDraw.Draw(img)

          # Define the initial position for the text
          pos = (card_info_layout.x, card_info_layout.y)

          if card_info_layout.text_type == "number":
              lines = textwrap.wrap(str(card_info.number), width=(card_info_layout.textbox_width - card_info_layout.x)//font.getsize(' ')[0])
          elif card_info_layout.text_type == "title":
              lines = textwrap.wrap(card_info.title, width=(card_info_layout.textbox_width - card_info_layout.x)//font.getsize(' ')[0])
          elif card_info_layout.text_type == "sanskrit":
              lines = textwrap.wrap(card_info.sanskrit, width=(card_info_layout.textbox_width - card_info_layout.x)//font.getsize(' ')[0])
          elif card_info_layout.text_type == "vdesc":
              lines = textwrap.wrap(card_info.vdesc, width=(card_info_layout.textbox_width - card_info_layout.x)//font.getsize(' ')[0])
          elif card_info_layout.text_type == "yoga":
              lines = textwrap.wrap(card_info.yoga, width=(card_info_layout.textbox_width - card_info_layout.x)//font.getsize(' ')[0])

          if len(str(lines)) > 30 and len(lines) < 9:
              padding_lines = 9 - len(lines)
              lines = [" " * (len(lines[0]) // 2)] * (padding_lines // 2) + lines + [" " * (len(lines[0]) // 2)] * (padding_lines - padding_lines // 2)

          for line in lines:
              # Calculate the width of the line and adjust the position
              line_width = font.getsize(line)[0]
              if card_info_layout.justify == 'center':
                  pos = ((width - line_width) // 2 + card_info_layout.x, pos[1])
              elif card_info_layout.justify == 'right':
                  pos = (width - line_width - card_info_layout.x, pos[1])
              else:  # left
                  pos = (card_info_layout.x, card_info_layout.y)

              d.text(pos, line, fill=card_info_layout.color, font=font)


              # Check if the text should be inverted
              if card_info_layout.text_type == "number":
                  # Create a new image for the text
                  text_img = Image.new('RGB', (line_width, font.getsize(line)[1]), color = card_info.color)
                  text_d = ImageDraw.Draw(text_img)

                  # Draw the text on the new image
                  text_d.text((0, 0), line, fill=card_info_layout.color, font=font)

                  # Rotate the image
                  text_img = text_img.rotate(180)

                  # Paste the rotated image on the main image
                  img.paste(text_img, (620,1020))

              pos = (card_info_layout.x, pos[1] + font.getsize(line)[1])

          pos = card_info_layout.x, pos[1] + card_info_layout.y
        # Save the image
        img.save(card_info.yoga+card_info.number+card_info.vno+'.png')

if __name__ == "__main__":
    main()
