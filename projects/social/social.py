from random import shuffle




class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        def comb2(s):
            combos = []
            for i, v1 in enumerate(s):
                for j in range(i+1, len(s)):
                    combos.append([v1, s[j]])
            return combos

        if numUsers > avgFriendships:
        # Add users
            users = []
            for i in range(1, numUsers+1):
                self.addUser(i)
                users.append(i)
        # Create friendships
            combos = comb2(users)
            shuffle(combos)
            print(combos)
            
            combos = [combo for combo in combos if combo[0] < combo[1]]
            combos = combos[:numUsers * avgFriendships//2]

            for combo in combos:
                self.addFriendship(combo[0], combo[1])
                
        else:
            print("Error, number of users is greater than the avg number of friendships")


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # Create an empty Queue and enqueue A PATH TO the starting vertex
        q = []
        q.append([userID])
        # While the queue is not empty...
        while len(q) > 0:
            # Dequeue the first PATH
            p = q.pop(0)
            # GRAB THE userID FROM THE END OF THE PATH
            v = p[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited[v] = p
                # Then add A PATH TO all of its neighbors to the back of the queue
                for friend in self.friendships[v]:
                    # Copy the path
                    path_copy = list(p)
                    # Append the neighbor to the back of the copy
                    # Enqueue copy
                    path_copy.append(friend)
                    q.append(path_copy)
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print("Friendships")
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print("Connections:")
    print(connections)
