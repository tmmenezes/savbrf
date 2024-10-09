# This is a sample Python script.
import os

from cv2 import waitKey
from Classes.FacesHandler import FacesHandler
from Classes.Person import Person

def main():
    person = Person('Gal Gadot', 'Tests/Target/Gal_gadot.webp')
    handler = FacesHandler(person.photo_path)
    handler.show_target_face(person.name)
    handler.search_target(person.name, 'Tests/Images/provavel-liga-da-justica.webp')

    waitKey(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
