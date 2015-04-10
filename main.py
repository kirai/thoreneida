from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

wp = Client('http://www.kirainet.com.com/xmlrpc.php', '', '')
wp.call(GetPosts())
wp.call(GetUserInfo())

print blog_post_text
print blog_post_title

post = WordPressPost()
post.title = 'test'
post.content = 'blog post'

post.terms_names = {
    'post_tag': ['test', 'firstpost'],
    'category': ['Introductions', 'Tests']
}

 wp.call(NewPost(post))
