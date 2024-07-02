import requests
from PIL import Image
import io

def get_desk_bottom_coordinates(image_path):
    url = "http://localhost:5000/mark_desk_bottom"
    files = {'image': open(image_path, 'rb')}
    response = requests.post(url, files=files)
    data = response.json()
    return data['coordinates']

def move_robot_to_coordinates(robot, coordinates):
    xmin = coordinates['xmin']
    ymin = coordinates['ymin']
    xmax = coordinates['xmax']
    ymax = coordinates['ymax']

    target_x = (xmin + xmax) // 2
    target_y = (ymin + ymax) // 2

    robot.move_to(target_x, target_y)

class Go1Robot:
    def __init__(self):
        pass

    def move_to(self, x, y):
        print(f"Moving robot to coordinates: ({x}, {y})")
        # 控制代码 control code
#





not finish




#

if __name__ == "__main__":
    image_path = "path_to_your_image.png"
    coordinates = get_desk_bottom_coordinates(image_path)
    print(f"获取到的坐标: {coordinates}")

    robot = YourGo1Robot()
    move_robot_to_coordinates(robot, coordinates)
