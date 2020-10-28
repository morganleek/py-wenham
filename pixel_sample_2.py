from PIL import Image

im = Image.open('david-full_3.jpg')
pix = im.load()
# Get size
size = im.size

xOffset = 0
yOffset = 0

svg_circles = ""

for y in range(0, size[1], 24) :
	xOffset = (y % 48)
	for x in range(0, size[0], 48) :
		xFinal = x + xOffset
		yFinal = y
		radius = 0
		if sum(pix[x + xOffset, y]) < 750 :
			radius = 18
			# for xCrawl in range(x + xOffset, x + xOffset + 20) :
			for xCrawl in range(0, 20) :
				if sum(pix[xFinal + xCrawl, y]) > 750 :
					# radius = ((xCrawl - (x + xOffset)) - 1) * 2
					radius = xCrawl
					break
		
		if radius == 0 :
			svg_circles += "<circle fill=\"#FF0000\" cx=\"" + str(xFinal) + "\" cy=\"" + str(yFinal) + "\" r=\"1\"/>\n"
		else :
			svg_circles += "<circle cx=\"" + str(xFinal) + "\" cy=\"" + str(yFinal) + "\" r=\"" + str(radius) + "\"/>\n"

print("<svg id=\"Layer_1\" data-name=\"Layer 1\" xmlns=\"http://www.w3.org/2000/svg\" width=\"" + str(size[0]) + "\" height=\"" + str(size[1]) + "\" viewBox=\"0 0 " + str(size[0]) + " " + str(size[1]) + "\">")
print(svg_circles)
print("</svg>")