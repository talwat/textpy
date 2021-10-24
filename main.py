from PIL import Image

def getInput():
    global path
    global resolution
    path = input("INPUT: What is the path to the image? ")
    resolution = (int)(input("INPUT: What should the resolution be? "))
    if(resolution > 500):
        print("WARNING: Resolutions over 500 have a very high chance of producing a corrupted output, and using too much system resources.")
        answer = input("INPUT: Are you sure you would like to continue? (y/n) ")
        if(answer == "y"):
            return
        else:
            quit()

def main():
    getInput()
    gradient = ".'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    img = Image.open(path) 
    img = img.convert('LA')
    width, height = img.size
    finalWidth = round(width / (width / resolution))
    finalHeight = round(height / (height / resolution))
    img = img.resize((finalWidth, finalHeight))
    width, height = img.size
    line = ""
    final = ""

    for i in range(height):
        for j in range(width):
            pixel = img.getpixel((j, i))
            brightness = pixel[0]
            brightness = round(brightness/(256/(len(gradient)-1)))
            if(brightness > 0):
                line = line + gradient[brightness] + gradient[brightness]
            else:
                line = line + "  "
        final = final + "\n" + line
        line = ""
    output = open("outputPY.txt","w+")
    output.write(final)
    output.close()
if __name__ == "__main__":
    main()