import numpy as np

def get_closest_centroid(points, K, centroids):
    """
    points.shape = (m, n)
    centroids.shape = (K, n)
    """

    # storing length of points (# of pixels)
    m = points.shape[0]

    # finding how far away each centroid is from each pixel
    diff = points[:, np.newaxis, :] - centroids[np.newaxis, :, :]
    distances = np.sum(diff**2, axis=2)
    # finding closest centroid to each pixel
    closest_centroids = np.argmin(distances, axis=1)


    return closest_centroids


def compute_new_centroids(points, K, closest_centroids):
    new_centroids = np.zeros((K, points.shape[1]))
    # storing how many each centroid is a pixel's closest centroid 
    frequencies = np.zeros(K)
    for i in range(points.shape[0]):
        index = closest_centroids[i]
        frequencies[index] += 1
        for j in range(points.shape[1]):
            new_centroids[index][j] += points[i][j]
    for i in range(K):
        if(frequencies[i] != 0):
            for j in range(points.shape[1]):
                new_centroids[i][j] = new_centroids[i][j]/frequencies[i]

    return new_centroids