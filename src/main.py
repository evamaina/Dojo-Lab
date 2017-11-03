from Office import Office
from LivingSpace import LivingSpace

if __name__ == '__main__':
    # room = Room()
    # room.create_room(room_name="mahiga", room_type="office")
    room1 = Office()
    room2 = LivingSpace()
    print(room2.allocations)
    print(room2.select_room())
    print(room1.allocations)
    print(room1.select_room())
