# Flask MongoDB Blog API

A RESTful API for managing blog authors and posts, built with Flask and MongoDB.

## Features

- **Authors Management**
  - Create new authors
  - List all authors
- **Posts Management**  
  - Create, read, update, and delete posts
  - Posts linked to authors
- **Data Validation**
  - Marshmallow schemas for request validation
  - MongoDB ObjectID validation

## API Endpoints

### Authors
| Method | Endpoint       | Description                | Request Body                              |
|--------|----------------|----------------------------|------------------------------------------|
| GET    | `/get_authors` | Get all authors           | None                                     |
| POST   | `/add_authors` | Create a new author       | `{"name": "string", "email": "email"}`   |

### Posts
| Method | Endpoint          | Description                | Request Body                                                                 |
|--------|-------------------|----------------------------|-----------------------------------------------------------------------------|
| POST   | `/posts`          | Create new post            | `{"title": "string", "content": "string", "author_id": "valid_object_id"}`  |
| PUT    | `/posts/<post_id>`| Update post                | `{"title": "string", "content": "string"}` (at least one required)         |
| DELETE | `/posts/<post_id>`| Delete post                | None                                                                       |

## Test Data
### Valid Author Creation:
```
{
    "name": "Akinyemi Ayomide",
    "email": "femi@gmail.com"
}
```
### Success Response (201):
```
{
"id": "685e39b3e83157c90fc38c01"
}
```
## Error Responses:

```
400 - Validation Error 
{
    "name": ["Missing data for required field."],
    "email": ["Not a valid email address."]
}

 400 - Duplicate Email 
{
    "error": "Validation error",
    "message": "Email already exists"
}
```
### GET /get_authors
```
[
    {
        "_id": "685e39b3e83157c90fc38c01",
        "email": "femi@gmail.com",
        "name": "Akinyemi Ayomide"
    },
    {
        "_id": "685e39dfe83157c90fc38c02",
        "email": "onyii@gmail.com",
        "name": "Onyinye Ifeanyi"
    }
]
```
### Valid Post Creation:
```
{
    "title": "Life",
    "content": "Life is a journey",
    "author_id": "685e39dfe83157c90fc38c02"
}
```
### Success Response (201):
```
{
"id": "685e3f85e83157c90fc38c04"
}
```
### Error Responses:

```
 400 - Validation Error 
{
    "title": ["Missing data for required field."],
    "author_id": ["Not a valid ObjectId."]
}

404 - Author Not Found 
{
    "error": "Author not found",
    "message": "No author exists with ID 665a1f8b4e3a8f7d4c9b2a99"
}
```
### PUT /posts/:post_id
```
{
    "title": "Java Language",
    "content": "Java is an object oriented language..."
    
  }
```
### Success Response (200):
```
{
    "message": "Post deleted"
}
```
### Error Responses:

```
 400 - No Valid Fields 
{
    "error": "Invalid request",
    "message": "Must provide at least one of: title, content"
}

 404 - Post Not Found
{
    "error": "Post not found",
    "message": "No post exists with ID 665a1f8b4e3a8f7d4c9b2a99"
}
```
## DELETE /posts/:post_id
### Success Response (200):

```
{
    "message": "Post deleted"
}
```

