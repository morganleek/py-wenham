from PIL import Image

im = Image.open('david-sample.jpg')
pix = im.load()
# Get size
size = im.size
# Dots
# dots = []
dots = [[0 for _ in range(int(size[0] / 12))] for _ in range(int(size[1] / 12))]

for y in range(0, size[1], 12) :
	for x in range(0, size[0] - 12, 12) :
		dx = int(x / 12)
		dy = int(y / 12)
		if sum(pix[x,y]) > 750 :
			dots[dx][dy] = 0
			# print("<circle cx='", x, "' cy='", y, "' r='0'/>", sep="")
		else :
			# Move x over until white is found
			# print(sum(pix[x,y]))
			for xn in range(x, x + 20) :
				if(pix[xn,y] == (255, 255, 255)) :
					dots[dx][dy] = (xn - x) * 2
					radius = (xn - x)
					print("<circle cx='", x, "' cy='", y, "' r='", radius, "'/>", sep="")
					break

# print(dots)