extends PathFollow2D

var current_point = 0
@onready var path_follow = get_parent()

@export var _speed = 0
var user_info_dict = {}
func _ready():
	lurker()
	csv_to_dict()
	download_image()
#	create_user_sprite()
	
	pass
	
func _physics_process(delta):
	current_point += 1
	progress_ratio = current_point /1000.0
	pass
	
	
func lurker():
	var file = FileAccess.open("F://Coding with Strangers//Path2partnership//lurker_points.csv", FileAccess.READ)
	var content = file.get_csv_line()
	while not file.eof_reached():
		content = file.get_csv_line()
		print(content, 'hell yea')
	return content

#function to read csv and convert to dict.
func csv_to_dict():
	var file = FileAccess.open("F://Coding with Strangers//Path2partnership//lurker_points.csv", FileAccess.READ)
	var user_info_dict = {}
	while not file.eof_reached():
		var content = file.get_csv_line()
		print(content, 'hell yea')
		if content.size() > 1:
			user_info_dict[content[0]] = {"points": int(content[1]), "image_url": content[2]}
	print(user_info_dict)
	return user_info_dict
	
#func create_user_sprite():
#	add_child(user_info_dict)


	
#then makes them a sprite with certain code
#loop throught the dict to check on users inside
#func create_user_sprite():
#	var user_info_dict = {}
#	for user_name in user_info_dict.keys():
#		#how to get user info from 
#		var user_info = user_info_dict.keys()
#		var points = user_info_dict['points']
#		var image_url = user_info_dict['image_url']
#
#		#new sprite for each entery 
#		var user_sprite = Sprite2D.new()
###add as a child
#		add_child(user_sprite)

#get image
#make var for image link
func download_image():
	# Create an HTTP request node and connect its completion signal.
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed.connect(self._http_request_completed)
	print("Yo mother lover")

	# Perform the HTTP request. The URL below returns a PNG image as of writing.
	var csv_pix = csv_to_dict()
#	var csv_info = create_user_sprite()
	
	var error = http_request.request(csv_pix['productivetime']['image_url'])
	
	var error2 = http_request.request(csv_pix['thestrangest_bot']['image_url'])
	if error != OK:
		push_error("An error occurred in the HTTP request.")		
		print('is the download working')
		#return download_image()

# Called when the HTTP request is completed.
func _http_request_completed(result, response_code, headers, body):
	if result != HTTPRequest.RESULT_SUCCESS:
		push_error("https://static-cdn.jtvnw.net/jtv_user_pictures/e1cc6f85-5198-4cc0-b60b-ad3a42eaa3ab-profile_image-300x300.png")
	var image = Image.new()
	var error = image.load_png_from_buffer(body)
	if error != OK:
		push_error("Couldn't load the image.")
		
	
	var texture = ImageTexture.create_from_image(image)
	# Display the image in a TextureRect node.
	var sprite = Sprite2D.new()
	add_child(sprite)
	#assign  texture to sprite
	sprite.texture = texture



#extends PathFollow2D
#var current_point = 0
#@onready var path_follow = get_parent()
#
#@export var _speed = 0
#var user_info_dict ={}
#
## Common starting position for all sprites
#var starting_position = Vector2(100, 100)
#
## Called when the node enters the scene tree for the first time.
#func _ready():
#	lurker()
#	download_image()
#	csv_to_dict()
#	pass
#
#	pass # Replace with function body.
#
#func _physics_process(delta):
#	current_point += 1
#	progress_ratio = (current_point /1000)
#	pass
#
#func lurker():
#	var file = FileAccess.open("F://Coding with Strangers//Path2partnership//lurker_points.csv", FileAccess.READ)
#	var content = file.get_csv_line()
#	while not file.eof_reached():
#		content = file.get_csv_line()
#		print(content, 'hell yea')
#	return content
#
#
##make var for image link
#func download_image():
#	# Create an HTTP request node and connect its completion signal.
#	var http_request = HTTPRequest.new()
#	add_child(http_request)
#	http_request.request_completed.connect(self._http_request_completed)
#	print("Yo mother lover")
#
#	# Perform the HTTP request. The URL below returns a PNG image as of writing.
#	var csv_pix = csv_to_dict()
#	user_info_dict['thestrangest_bot']['image_url']
#	var error = http_request.request("image_url")
#	if error != OK:
#		push_error("An error occurred in the HTTP request.")		
#		print('is the download working')
#
#
#
#	# Called when the HTTP request is completed.
#func _http_request_completed(result, response_code, headers, body):
#	if result != HTTPRequest.RESULT_SUCCESS:
#		push_error("https://static-cdn.jtvnw.net/jtv_user_pictures/e1cc6f85-5198-4cc0-b60b-ad3a42eaa3ab-profile_image-300x300.png")
#	var image = Image.new()
#	var error = image.load_png_from_buffer(body)
#	if error != OK:
#		push_error("Couldn't load the image.")
#
#	var texture = ImageTexture.create_from_image(image)
#	# Display the image in a TextureRect node.
#	var texture_rect = TextureRect.new()
#	add_child(texture_rect)
#	texture_rect.texture = texture
##
##
##Need to write a function that gets every user from csv #function to read csv and convert to dict.
#func csv_to_dict():
#	var file = FileAccess.open("F://Coding with Strangers//Path2partnership//lurker_points.csv", FileAccess.READ)
#	while not file.eof_reached():
#		var content = file.get_csv_line()
#		print(content, 'hell yea')
#		if content.size() > 1:
#			user_info_dict[content[0]] = {"points": int(content[1]), "image_url": content[2]}
#	print(user_info_dict)
#	return user_info_dict
#
#
## then makes them a sprite with certain code
##loop throught the dict to check on users inside
#func create_user_sprite():
#	for user_name in user_info_dict.keys():
#		#how to get user info from 
#		var user_info = user_info_dict.keys()
#		var points = user_info['points']
#		var image_url = user_info['image_url']
#
#		#new sprite for each entery 
#		var user_sprite = Sprite2D.new()
#
#
#		#add as a child
#		add_child(user_sprite)
			
		
	
