This project is useful for if you want to compress an image with a lot of unecessarily different shades of colors which are all very similar to one another. 
Once you select the amount of colors you want to compress the original image into, the algorithm creates those many random centroids. It then repeatedly shifts the shades of those
centroids until they best reflect the pixels which are closest to them. Finally, all pixels are set to the shade of their closest centroid. 
