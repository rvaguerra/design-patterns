from composite import Composite


class Room(Composite):
    pass


class Wall(Composite):
    pass


class Window:
    pass


room = Room()
[room.add(Wall()) for _ in range(0, 4)]

for wall in room.children:
    wall.add(Window())

print(f'Room has {len(room.children)} wall(s).')

childToBeRemoved = room.children[0]
room.remove(childToBeRemoved)

print(f'Room has {len(room.children)} wall(s) after removal.')

for wall in room.children:
    print(f'Wall has {len(wall.children)} window(s).')

print(f'Removed child still exists: {childToBeRemoved.children}')
