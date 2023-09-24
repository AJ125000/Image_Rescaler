import cv2

source  = input('enter the name of image ')

# image_name_without_extension = source.rpartition('.')[0]  #this code can also be used to get image name without extension

extension = input('enter the extension (with a "." )')
destination = f'new{source}.jpg'
scale_percent = int(input("Enter the scaling percentage "))

src = cv2.imread(source+extension, cv2.IMREAD_UNCHANGED)


width = int(src.shape[1]*scale_percent/100)
height = int(src.shape[0]*scale_percent/100)

output = cv2.resize(src, (width,height))

cv2.imwrite(destination,output)
cv2.waitKey(0)