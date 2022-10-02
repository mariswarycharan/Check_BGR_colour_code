import cv2
from matplotlib import image
import numpy as np

ima = np.zeros((512,512,3),np.uint8)

def main(x):
    print(x)
    
cv2.namedWindow("image")
 
cv2.createTrackbar("B" ,"image",0,255,main )
cv2.createTrackbar("G" ,"image",0,255,main )
cv2.createTrackbar("R" ,"image",0,255,main )


while True:
    
    cv2.imshow("image",ima)
    b = cv2.getTrackbarPos("B" ,"image")
    g = cv2.getTrackbarPos("G" ,"image")
    r= cv2.getTrackbarPos("R" ,"image")
    ima[:] = [b,g,r]
    font = cv2.FONT_HERSHEY_SIMPLEX
    s1 = str(b) + "," + str(g)  + "," +  str(r)
        
    
    cv2.rectangle(ima,(170,455),(352,487),(255,255,255),-1)
    cv2.putText(ima , s1,(180,480),font,.9,(255,56,8),2)
    if cv2.waitKey(1) == 81:
        break


cv2.destroyAllWindows()