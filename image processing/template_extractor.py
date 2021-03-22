from ezdxf.addons import r12writer #pip3 install ezdxf
import cv2 #pip3 install opencv-python (can be a bit finicky with versions)
import numpy                 
import os
import time

#contour detection based on simple greyscale thresholding
def threshold(img):
    #get image dimensions
    img_height, img_width = img.shape 
    #perform morphological closing transforms if necessary
    # img = cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)), iterations=2)
    # img = cv2.erode(img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2)), iterations=2)
    #threshold the image and display
    thresholded = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow("Thresholded", thresholded)
    #identify contours, plot on empty array and display
    contours = cv2.findContours(thresholded,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
    contour_image = numpy.ones((img_height,img_width,3), numpy.uint8)
    cv2.drawContours(contour_image, contours, -1, (255, 0, 0), 3) 
    cv2.imshow("Threshold Contours", contour_image)
    return contours

#contour detection based on canny edge detection algorithm
def edgedetect(img):
    #get image dimensions
    img_height, img_width = img.shape
    #perform morphological closing transforms if necessary
    # img = cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3)), iterations=2)
    # img = cv2.erode(img, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2)), iterations=2)
    edgedetected = cv2.Canny(img, 100, 200)
    cv2.imshow("EdgeDetected", edgedetected)
    #identify contours, plot on empty array and display
    contours = cv2.findContours(edgedetected,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
    contour_image = numpy.ones((img_height,img_width,3), numpy.uint8)
    cv2.drawContours(contour_image, contours, -1, (255, 0, 0), 3)
    cv2.imshow("EdgeDetect Contours", contour_image)
    return contours


#request path to folder containg input images
input_path = input("Input path: ") or os.path.dirname(os.path.abspath(__file__))

#loop through the given folder exploring all subdirectories
for subdir, dirs, files in os.walk(input_path):
    #for each file...
    for file in files:
        #create a dxf document to write to
        with r12writer(file+".dxf") as doc:
            #read image from input file
            print(os.path.join(subdir, file))
            raw_img = cv2.imread(os.path.join(subdir,file),cv2.IMREAD_GRAYSCALE)
            #check if input file is valid image and display
            if raw_img is None:
                continue
            cv2.imshow("Raw", raw_img)
            #apply the two contour detection methods
            threshold_contours = threshold(raw_img)
            edgedetect_contours = edgedetect(raw_img)
            #plot threshold contour points onto layer 0 of the dxf
            for thresh_contour in threshold_contours:
                points_list = []
                for points in thresh_contour:
                    points_list.append(points[0])
                doc.add_polyline(points_list,layer="0", closed = True)
            #plot edgedetect contour points onto layer 1 of the dxf
            for edge_contour in edgedetect_contours:
                points_list = []
                for points in edge_contour:
                    points_list.append(points[0])
                doc.add_polyline(points_list,layer="1", closed = True)

cv2.waitKey(0)  
cv2.destroyAllWindows()  