posts = [{
    "id": "some-uuid",
    "title": "aTitle",
    "author": "anAuthor",
    "content": "aContent",
    "created_at": "2023-01-19T15:56:38.015865",
    "published_at": None,
    "published": False
},
    {
        "id": "7a75a41b-1acb-4a18-8ea6-441f877cb812",
        "title": "el bueno",
        "author": "pepe",
        "content": "peliculon",
        "created_at": "2023-01-19T16:17:38.725225",
        "published_at": None,
        "published": False
    },
    {
        "id": "7a75a41b-1acb-4a18-8ea6-441f877cb992",
        "title": "el loco",
        "author": "pepe",
        "content": "peliculon",
        "created_at": "2023-01-19T16:17:38.725225",
        "published_at": None,
        "published": False
    }
]


class PostService:

    def get_posts(self):
        return posts

    async def find_and_update(self, post_id, postData):
        for post in posts:
            found = self.evaluate_post(post, post_id)
            if found:
                await self.update_att(post, postData, "title")
                await self.update_att(post, postData, "author")
                await self.update_att(post, postData, "content")
                return post
        return None

    def evaluate_post(self, post, post_id: str, title=None):
        exists = post["id"] == post_id
        if exists and title:
            exists = post["title"] == title
        return exists


    async def update_att(post, postData, att: str):
        if postData.keys().__contains__(att):
            post[att] = postData[att]

