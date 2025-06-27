from marshmallow import Schema, fields

class AuthorSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)