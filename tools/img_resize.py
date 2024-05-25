
import cv2

def resize_image(image1_path, image2_path, save_path):
    # 读取图片1
    image1 = cv2.imread(image1_path)
    # 读取图片2
    image2 = cv2.imread(image2_path)
    # 检查图片是否成功加载
    if image1 is None or image2 is None:
        print("Error loading images!")
        return
    # 获取图片2的尺寸
    height, width = image2.shape[:2]
    # 调整图片1到图片2的大小
    resized_image1 = cv2.resize(image1, (width, height))
    # 保存调整大小后的图片1
    cv2.imwrite(save_path, resized_image1)
    print(f'Resized image saved at {save_path}')

# 使用示例
resize_image('/Users/demac/Desktop/final-assignment/wwwroot/img/core-img/logo.png', 
             '/Users/demac/Desktop/final-assignment/wwwroot/img/core-img/logo-white.png', 
             '/Users/demac/Desktop/final-assignment/wwwroot/img/core-img/logo.1.png')