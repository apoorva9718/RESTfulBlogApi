# RESTfulBlogApi

Building a RESTful Blog APIs using python and flask for 4 Basic CRUD (Create, Read, Update, Delete) Operations

User
- POST /api/v1/users - create a user(CREATE)
- POST /api/v1/users/login - User Login
- GET /api/v1/users/me - get my info(READ)
- GET /api/v1/users - get all registered users(READ)
- PUT /api/v1/users/me - update my account(UPDATE)
- DELETE /api/v1/users/me - Delete my account(DELETE)

Blogpost of Users
- POST api/v1/blogposts - Create a Blogpost (CREATE)
- GET api/v1/blogposts - Get All Blogposts (READ)
- GET api/v1/blogposts/<int:blogpost_id> - Get A Blogposts (READ)
- PUT api/v1/blogposts/<int:blogpost_id> - Update A Blogpost (UPDATE)
- DELETE api/v1/blogposts/<int:blogpost_id> - Delete A Blogpost (DELETE)
