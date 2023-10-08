import cv2
import numpy as np;

num_rec_lst = []
def blob_det(i):
    Path = "Test2/dice_"+str(i+1)+".jpg"
    im_gray = cv2.imread(Path,cv2.IMREAD_GRAYSCALE)
    #gray scale image
    output = im_gray.copy() 
    #binarize image
    thresh = 180
    im_bin = cv2.threshold(output, thresh, 255, cv2.THRESH_BINARY)[1]
    #crop image
    x = 125
    y = 220
    width = 350
    height = 500
    im_crop = im_bin[y:y+height, x:x+width]
    #invert image
    im_fin = cv2.bitwise_not(im_crop)
    #detect blobs of black dots
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 25
    params.maxThreshold = 150
    params.filterByArea = True
    params.minArea = 200
    params.maxArea=2500
    params.filterByCircularity = False
    params.filterByConvexity = False
    params.filterByInertia = False
    detector = cv2.SimpleBlobDetector_create(params)
    keypt = detector.detect(im_fin)
    #count number of black dots
    nblobs = len(keypt) 
    num_rec_lst.append(nblobs)
    #draw the keypoints on show image
    im_keypts = cv2.drawKeypoints(im_fin, keypt, np.array([]), (0,0,255),
                                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #add number of dots/keypts text on image
    font = cv2.QT_FONT_NORMAL
    org = (25, 35)
    fontScale = 1
    color = (0, 0, 0)
    thickness = 2
    image_fin = cv2.putText(im_keypts, str(nblobs), org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    cv2.imwrite("Img_out/dice_img#"+str(i)+"_"+str(nblobs)+".jpg",image_fin)

for x in range(3250):
    blob_det(x)
# create count dictionary
counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,}
total = 0
# Count the occurrences of each number in the list and print em BITCCHHHH
for num in num_rec_lst:
    if num in counts:
        counts[num] += 1
        total = total +1
for num, count in counts.items():
    print(f"Probability of {num}s: {round(count/total*100,2)}%")




