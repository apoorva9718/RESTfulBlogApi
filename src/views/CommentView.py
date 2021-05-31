#/src/views/Comments.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.CommentModel import CommentModel, CommentSchema

comment_api = Blueprint('comment_api', __name__)
comment_schema = CommentSchema()


@comment_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Comments Function
  """
  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  data = comment_schema.load(req_data) #,error
  #if error:
    #return custom_response(error, 400)
  post = CommentModel(data)      
  post.save()
  data = comment_schema.dump(post)
  return custom_response(data, 201)

@comment_api.route('/', methods=['GET'])
def get_all():
  """
  Get All Comments
  """
  posts = CommentModel.get_all_comments()
  data = comment_schema.dump(posts, many=True)
  return custom_response(data, 200)
  

@comment_api.route('/<int:comment_id>', methods=['GET'])
def get_one(comment_id):
  """
  Get A Blogpost along with all the comments
  """
  post = CommentModel.get_one_blogpost_with_comment(comment_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = comment_schema.dump(post)
  return custom_response(data, 200)


@comment_api.route('/<int:comment_id>', methods=['PUT'])
@Auth.auth_required
def update(comment_id):
  """
  Update A Comment
  """
  req_data = request.get_json()
  post = CommentModel.get_one_comment(comment_id)
  if not post:
    return custom_response({'error': 'post and comment not found'}, 404)
  data = comment_schema.dump(post)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)
  
  data = comment_schema.load(req_data, partial=True)
  #if error:
    #return custom_response(error, 400)
  post.update(data)
  
  data = comment_schema.dump(post)
  return custom_response(data, 200)

@comment_api.route('/<int:comment_id>', methods=['DELETE'])
@Auth.auth_required
def delete(comment_id):
  """
  Delete A Comment 
  """
  post = CommentModel.get_one_comment(comment_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = comment_schema.dump(post)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  post.delete()
  return custom_response({'message': 'deleted'}, 204)
  

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

