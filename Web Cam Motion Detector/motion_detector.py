----------------------------------------
### PROJECT: WEB CAM MOTION DETECTOR ###
----------------------------------------
import cv2, time, pandas
from datetime import datetime

first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    #setting the status to 0 until the object appears 
    status=0
    #transforming frame into gray scale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #applying gaussian blur
    gray=cv2.GaussianBlur(gray,(21,21),0)

    #storing first frame in first_frame
    if first_frame is None:
        first_frame=gray
        continue

    #calculating difference between first_frame and gray scale image
    #explore absdiff function for more details
    #https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html
    delta_frame=cv2.absdiff(first_frame,gray)
    
    #calculating threshold; creating black and white image;
    #explore threshold function for more details
    #https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    #finding contours of the moving objects
    #explore countour function for more details
    #https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html
    #https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        #defining the contour Area size
        if cv2.contourArea(contour) < 10000:
            continue
        #setting the status to 1 when the object appears 
        status=1

        #extracting the bounding Rectangle coordinates
        (x, y, w, h)=cv2.boundingRect(contour)
        #creating the rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
        
    #appending the list by the (0,1) status
    status_list.append(status)

    #selecting the last 2 elements of the list
    status_list=status_list[-2:]

    
    if status_list[-1]==1 and status_list[-2]==0:
        #appending the list when the object appears
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        #appending the list when the object removes
        times.append(datetime.now())

    #showing images
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(1)

    #defining 'q' letter for exiting the motion detector
    if key==ord('q'):
        if status==1:
            #appending the list if the status is 1 and if the user exit and if the motion detector
            times.append(datetime.now())
        break

print(status_list)
print(times)

#using the pandas, we are updating the Pandas Data Frame with Start and End Time
for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

#exporting the data into csv file
df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows
