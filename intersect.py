import cv2
import numpy as np

# Step 1: Canny Edge Detection
def apply_canny_edge(image_path):
    # Image ko load karo
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Canny edge detection apply karo
    edges = cv2.Canny(image, 100, 200)

    return edges

# Step 2: Rectangle Drawing
def draw_rectangle_on_edges(edges, rectangle_coords):
    # Rectangle ke coordinates (x1, y1, x2, y2)
    x1, y1, x2, y2 = rectangle_coords
    # Rectangle ko draw karo
    image_with_rectangle = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(image_with_rectangle, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return image_with_rectangle

# Step 3: Find Intersecting Points
def find_intersections(edges, rectangle_coords):
    x1, y1, x2, y2 = rectangle_coords

    intersections = []

    # Rectangle ki har line ko edges ke saath compare karo
    # 1st line: (x1, y1) to (x2, y1)
    for x in range(x1, x2):
        if edges[y1, x] == 255:
            intersections.append((x, y1))

    # 2nd line: (x2, y1) to (x2, y2)
    for y in range(y1, y2):
        if edges[y, x2] == 255:
            intersections.append((x2, y))

    # 3rd line: (x2, y2) to (x1, y2)
    for x in range(x1, x2):
        if edges[y2, x] == 255:
            intersections.append((x, y2))

    # 4th line: (x1, y2) to (x1, y1)
    for y in range(y1, y2):
        if edges[y, x1] == 255:
            intersections.append((x1, y))

    return intersections

# Main function
def main(image_path, rectangle_coords):
    # Canny edge detection
    edges = apply_canny_edge(image_path)

    # Rectangle draw karna
    image_with_rectangle = draw_rectangle_on_edges(edges, rectangle_coords)

    # Intersecting points find karna
    intersections = find_intersections(edges, rectangle_coords)

    # Result print karna
    print(f"Intersecting Points: {intersections}")

    # Image ko display karo
    cv2.imshow("Rectangle with Edges", image_with_rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Rectangle ke coordinates (x1, y1, x2, y2) specify karo
rectangle_coords = (100, 100, 400, 400)

# Image path specify karo
image_path = 'path_to_your_image.jpg'

# Main function call karo
main(image_path, rectangle_coords)
