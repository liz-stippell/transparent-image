import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

### ----- image name and save image as name. image must be saved as png ----- ###
image_name = "spongebob-white.jpg"
save_as = "spongebob-print.png"
### ----- END ----- ###

### ----- read image, set it to be a writeable file ----- ###
image = img.imread(image_name)
image = image.copy()
image.setflags(write=1)
### ----- END ----- ###

### ----- normalize image RGB ----- ###
image_normalized = image.astype(np.float32) / 255.0
### ----- END ----- ###

### ----- insert final column to all pixels to transform from RGB to RGBA (RGBA includes extra value that describes transparency) ----- ###
b = np.ones((image_normalized.shape[0], image_normalized.shape[1], 1))
image_normalized = (np.append(image_normalized, b, axis=-1))
### ----- END ----- ###

### ----- change transparency for pixels with RGB codes greater than [230 230 230] (these will be white pixels) ----- ###
for i in range(len(image_normalized)):
    for r in range(len(image_normalized[i])):
        if (image_normalized[i][r][0] >= 0.9 and image_normalized[i][r][1] >= 0.9 and image_normalized[i][r][2] >= 0.9):
            image_normalized[i][r][3] = 0
        else:
            continue
### ----- END ----- ###

### ----- format final image and save it ----- ###
fig = plt.figure(frameon=False)
ax = plt.Axes(fig, [0, 0, 1, 1])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(image_normalized)
plt.savefig(save_as, format="png")
### ----- END ----- ###
