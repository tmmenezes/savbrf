# This is a sample Python script.
from cv2 import waitKey

from Classes.PhotoHandler import PhotoHandler


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    photo = PhotoHandler('Tests', 'Gal_gadot.webp')
    photo.show_faces(photo.find_faces())
    waitKey(0)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
