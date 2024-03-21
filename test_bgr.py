import numpy as np
from nvjpeg import NvJpeg
import cv2

def test_nvjpeg_encode_decode():
    
    
    nvjpeg = NvJpeg()
    
    image = cv2.imread("/lyx/nvjpeg-python/tests/test-image/1.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    y, u, v = np.split(image, 3, axis=2)
    encoded_yuv = nvjpeg.encode(y, u, v, 90)
    # use opencv to decode
    decoded_yuv = cv2.imdecode(np.frombuffer(encoded_yuv, dtype=np.uint8), cv2.IMREAD_UNCHANGED) 

    print("NvJpeg encode and decode test passed!")
    cv2.imwrite("./output.jpg", decoded_yuv)

if __name__ == "__main__":
    test_nvjpeg_encode_decode()