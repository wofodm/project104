import cv2

img=cv2.imread("solar-system.jpg")

text_to_show="SUN"
text_to_show1="MERCURY"
text_to_show2="VENUS"
text_to_show3="EARTH"
text_to_show4="MARS"
text_to_show5="JUPITER"
text_to_show6="SATURN"
text_to_show7="URANUS"
text_to_show8="NAPTUNE"


cv2.putText(img,text_to_show,(80,100),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,color=(0,0,255))
cv2.putText(img,text_to_show1,(80,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.9,color=(255,255,255))
cv2.putText(img,text_to_show2,(200,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.9,color=(255,255,255))
cv2.putText(img,text_to_show3,(300,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.9,color=(255,255,255))
cv2.putText(img,text_to_show4,(400,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.9,color=(255,255,255))
cv2.putText(img,text_to_show5,(600,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.9,color=(255,255,255))
cv2.putText(img,text_to_show6,(800,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.9,color=(255,255,255))
cv2.putText(img,text_to_show7,(900,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.9,color=(255,255,255))
cv2.putText(img,text_to_show8,(1100,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.9,color=(255,255,255))
cv2.imshow("output",img)
cv2.waitKey(0)