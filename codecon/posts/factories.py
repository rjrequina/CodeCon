from django.db.models import Q

from posts.models import Post, Like

from comments.models import Comment


class PostFactory:

    def list(self, user, profile=0):
        posts = Post.objects.filter(owner=user)

        for post in posts:
            comments = Comment.objects.filter(commented_post=post)
            for item in comments:
                if item.owner == user:
                    item.is_owner = True
                else:
                    item.is_owner = False
            post.all_comments = comments
            post.all_likes = Like.objects.filter(liked_post=post)

        return posts

    def list_profile(self, user):
        posts = Post.objects.filter(owner=user)

        for post in posts:
            comments = Comment.objects.filter(commented_post=post)
            for item in comments:
                if item.owner == user:
                    item.is_owner = True
                else:
                    item.is_owner = False
            post.all_comments = comments
            post.all_likes = Like.objects.filter(liked_post=post)

        return posts

    def detail(self, pk):
        post = Post.objects.get(pk=pk)
        post.all_comments = Comment.objects.filter(commented_post=post)
        post.all_likes = Like.objects.filter(liked_post=post)

        return post


post_factory = PostFactory()