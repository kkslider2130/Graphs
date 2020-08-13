from room import Room
from player import Player
from world import World

from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# MVP 1000 steps

traversal_path = []
backtrack = []
traversed = {}
reverse = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

traversed[player.current_room.id] = player.current_room.get_exits()

while len(traversed) < len(room_graph):

    # if the room is new, add the room into our traversed dictionary
    room_id = player.current_room.id
    if room_id not in traversed.keys():
        # add the room's exits into each dictionary entry with the key being the id
        traversed[room_id] = player.current_room.get_exits()
        # remove the path it took to get to this room from the exits list so it can continue
        traversed[room_id].remove(backtrack[-1])

    # if there is no valid unexplored exits, backtrack in reverse order until there is
    if len(traversed[room_id]) == 0:
        prev_action = backtrack.pop()
        traversal_path.append(prev_action)
        player.travel(prev_action)

    # when there is a valid exit in the room in the dictionary, travel to that exit
    # append the reverse path to the backtracking sequence
    else:
        next = traversed[room_id].pop()
        traversal_path.append(next)
        backtrack.append(reverse[next])
        player.travel(next)


# traversal_path = []
# previous_direction = []
# previous_id = []
# traversed = {}
# reverse = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
# player.current_room = world.starting_room
# path = list(traversal_path)

# class Queue():
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, value):
#         self.queue.append(value)

#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None

#     def size(self):
#         return len(self.queue)

# def traverse():
#     global path
#     while player.current_room.id not in traversed.keys():
#         print('room-id', player.current_room.id)
#         exits = player.current_room.get_exits()
#         print('room-exits', player.current_room.get_exits())
#         action = random.choice(exits)
#         if len(player.current_room.get_exits()) == 1:
#             traversed[player.current_room.id] = {
#                 'n': '?', 's': '?', 'e': '?', 'w': '?'}
#             traversed[player.current_room.id][action] = player.current_room.get_room_in_direction(
#                 action).id
#             return
#         if player.current_room.get_room_in_direction(action):
#             while player.current_room.get_room_in_direction(action).id in traversed.keys():
#                 action = random.choice(exits)
#         traversed[player.current_room.id] = {
#             'n': '?', 's': '?', 'e': '?', 'w': '?'}
#         traversed[player.current_room.id][action] = player.current_room.get_room_in_direction(
#             action).id
#         if len(previous_direction) > 0:
#             traversed[player.current_room.id][reverse[previous_direction[-1]]
#                                               ] = previous_id[-1]
#         previous_direction.append(action)
#         previous_id.append(player.current_room.id)
#         traversal_path.append(action)
#         player.travel(action)
#         path = list(traversal_path)
#         print('path iteration', path)
#         print(traversal_path)


# traverse()

# while len(traversed) < len(room_graph):
#     print('pathpop', path)
#     last_step = path.pop()
#     retrace = reverse[last_step]
#     traversal_path.append(retrace)
#     path.append(retrace)
#     player.travel(retrace)
#     exits = player.current_room.get_exits()

#     action = []
#     print('#####', traversed)
#     for e in exits:
#         if traversed[player.current_room.id][e] == '?':
#             action = e
#             print('action', action)
#             if player.current_room.get_room_in_direction(action).id not in traversed.keys():
#                 traversed[player.current_room.id] = {
#                     'n': '?', 's': '?', 'e': '?', 'w': '?'}
#                 traversal_path.append(action)
#                 player.travel(action)
#                 traverse()
#                 break

#         else:
#             path.pop()


# use bfs to go back and explore any unexplored rooms as the target vertex
[0, 1, 2, 5, 50, 66, 96, 179, 201, 206, 232, 265, 268, 276, 459, 467, 6, 23, 58]

# TRAVERSAL TEST
print('&&&&', traversed)
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
