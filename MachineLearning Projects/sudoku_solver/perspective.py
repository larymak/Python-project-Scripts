import cv2
import numpy as np
from pytesseract import pytesseract as pt

def resolve_perspective(source_image:np.ndarray, points:np.ndarray, target_shape:tuple[int,int]) -> np.ndarray:
    """Takes an source image and transforms takes the region demarkated by points and creates a rectangular image of target.

    Args:
        source_image (np.ndarray): the source image.
        points (np.ndarray): a numpy array of 4 points that will demarkate the vertices of the region to be transformed.\n
        \tShould be in the form of points from the point that would be transformed to the top left of the rectangle, clockwise
        target_shape (tuple[int,int]): the target shape of the rectangular output image. Format [height, width].

    Returns:
        np.ndarray: the output image transformed
    """
    output_points:np.ndarray = np.array([
        [0,0],
        [target_shape[0]-1, 0],
        [target_shape[0]-1, target_shape[1]-1],
        [0,target_shape[1]-1]
        ], dtype=np.float32)
    transformation_matrix:cv2.typing.MatLike = cv2.getPerspectiveTransform(points.astype(np.float32), output_points)
    output:cv2.typing.MatLike = cv2.warpPerspective(source_image, transformation_matrix, (target_shape[1], target_shape[0]), flags=cv2.INTER_LINEAR)
    return output

def get_grid_size(image:np.ndarray, boxes:list[list[int]], allowed_sizes:list[tuple[int,int]]=[(2,3),(3,3),(4,4)]) -> tuple[int,int]:
    h,w = image.shape
    for size in allowed_sizes:
        s1 = float(w)/float(size[0])
        s2 = float(h)/float(size[1])
        for box in boxes:
            _,x1,y1,x2,y2 = box
            if (abs(int(x1/s1) - int(x2/s1)) + abs(int((h - y1)/s2) - int((h - y2)/s2))) > 0:
                break
        else:
            return size
        
def get_points(image:np.ndarray, boxes:list[list[int]], grid_size:tuple[int,int]) -> list[tuple[int,tuple]]:
    h,w = image.shape
    size = grid_size[0] * grid_size[1]
    s1 = float(w)/float(size)
    s2 = float(h)/float(size)
    results = []
    for box in boxes:
        val,x1,y1,x2,y2 = box
        center_x = int((x1+x2)/2)
        center_y = int((y1+y2)/2)
        results.append((val, (int((h-center_y)/s2), int(center_x/s1))))
    return results

def resolve_image(path:str) -> tuple[tuple,list[tuple[int,tuple]]]:
    # img = cv2.imread("images/image210.jpg")
    img = cv2.imread(path)
    numbers = [str(i) for i in range(10)]
    max_size = 500
    min_area = 150
    *img_shape,_ = img.shape
    max_ind = np.argmax(img_shape)
    min_ind = np.argmin(img_shape)
    next_shape = [0,0]
    if max_ind != min_ind:
        next_shape[max_ind] = max_size
        next_shape[min_ind] = int(img_shape[min_ind]*max_size/img_shape[max_ind])
    else:
        next_shape = [max_size, max_size]
    img = cv2.resize(img, tuple(reversed(next_shape)))
    points = np.array([6,97,219,99,216,309,7,310])
    points = points.reshape((4,2))
    target_shape = (400,400)
    output = resolve_perspective(img, points, target_shape)
    output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    norm_img = np.zeros((output.shape[0], output.shape[1]))
    output = cv2.normalize(output, norm_img, 0, 255, cv2.NORM_MINMAX)
    output1 = cv2.threshold(output, 140, 255, cv2.THRESH_BINARY_INV)[1]
    if np.average(output1.flatten()) > 128:
        output = cv2.threshold(output, 140, 255, cv2.THRESH_BINARY)[1]
    else:
        output = output1
    output = cv2.GaussianBlur(output, (1,1), 0)
    boxes = pt.image_to_boxes(output, "eng", config=r'-c tessedit_char_whitelist=0123456789 --psm 13 --oem 3')
    print(boxes)
    h,w = output.shape
    new_boxes_str = ""
    new_boxes = []
    for bt in boxes.splitlines():
        b = bt.split(' ')
        area = (int(b[1]) - int(b[3]))*(int(b[2]) - int(b[4]))
        if b[0] in numbers and area > min_area:
            output = cv2.rectangle(output, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (255, 255, 255), 2)
            new_boxes_str += bt + "\n"
            new_boxes.append(list(int(i) for i in b[:5]))
    grid_size = get_grid_size(output, new_boxes)
    final_points = get_points(output, new_boxes, grid_size)
    return grid_size,final_points

if "__main__" == __name__:
    print(resolve_image("f2.jpg"))