import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
from PIL import ImageFont
from IPython.display import display


# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

width, height = image.size
fonts = ImageFont.truetype('readonly/fanwood-webfont.ttf',50)

images=[]
intensity = [0.1,0.5,0.9]
for i in range(1,4):
    for val in intensity :
        newim = Image.new(image.mode,(width,height+50))
        caption = ImageDraw.Draw(newim)
        caption.text((0, newim.height - 50), 'channel {} intensity {}'
                         .format(i-1, val), font=fonts, fill=(255, 255, 255))
        im = image.copy()
        for x in range(height) :
            for y in range(width) :
                if i == 1 :
                    cur = im.getpixel((y,x))
                    r,g,b = cur
                    r = int(r*val)
                    newim.putpixel((y,x),(r,g,b))
                elif i == 2 :
                    cur = im.getpixel((y,x))
                    r,g,b = cur
                    g = int(g*val)
                    newim.putpixel((y,x),(r,g,b))
                else :
                    cur = im.getpixel((y,x))
                    r,g,b = cur
                    b = int(b*val)
                    newim.putpixel((y,x),(r,g,b))
        images.append(newim)

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0


for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
