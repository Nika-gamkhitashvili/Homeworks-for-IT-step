class User:
    def __init__(self, name):
        self.name = name
        self.posts = []
        self.friends = set()
        self.likes = 0

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def add_friend(self, friend):
        self.friends.add(friend)
        friend.friends.add(self)

    def add_like(self):
        self.likes += 1


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = 0

    def add_comment(self, comment_content, commenter):
        comment = Comment(comment_content, commenter)
        self.comments.append(comment)
        return comment

    def add_like(self):
        self.likes += 1


class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author

    def add_like(self):
        pass


user1 = User("User1")
user2 = User("User2")

user1.add_friend(user2)

post1 = user1.create_post("This is my first post!")

comment1 = post1.add_comment("Nice post!", user2)

post1.comments[0].add_like()
comment1.add_like()


post2 = user1.create_post("Here's another post!")

post2.add_like()

print(f"{user1.name} has {len(user1.posts)} posts.")
print(f"{user2.name} has {len(user2.posts)} posts.")
print(f"Post1 has {post1.likes} likes and {len(post1.comments)} comments.")
print(f"Post2 has {post2.likes} likes and {len(post2.comments)} comments.")
