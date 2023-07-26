extends Sprite2D

var current_point = 0
@onready var path_follow = get_parent()

@export var _speed = 0

func _ready():
	lurker()
	download_image()
	csv_to_dict()
	pass
	
func _physics_process(delta):
	current_point += 1
	path_follow.progress_ratio = current_point /1000.0
	
	
func lurker():
	var file = FileAccess.open("F://Coding with Strangers//Path2partnership//lurker_points.csv", FileAccess.READ)
	var content = file.get_csv_line()
	while not file.eof_reached():
		content = file.get_csv_line()
		print(content, 'hell yea')
	return content
	
	#get image
#make var for image link
func download_image():
	# Create an HTTP request node and connect its completion signal.
	var http_request = HTTPRequest.new()
	add_child(http_request)
	http_request.request_completed.connect(self._http_request_completed)
	print("Yo mother lover")

	# Perform the HTTP request. The URL below returns a PNG image as of writing.
	var error = http_request.request("https://static-cdn.jtvnw.net/jtv_user_pictures/e1cc6f85-5198-4cc0-b60b-ad3a42eaa3ab-profile_image-300x300.png")
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
		
	#save image to folder
	var image_path = "res://lurkers_images/"
	error = image.save_png(image_path)
	if error !=OK:
		push_error('That shit didnt save')
	
	var texture = ImageTexture.create_from_image(image)
	# Display the image in a TextureRect node.
	var texture_rect = TextureRect.new()
	add_child(texture_rect)
	texture_rect.texture = texture

#function to read csv and convert to dict.
func csv_to_dict():
	var file = FileAccess.open("F://Coding with Strangers//Path2partnership//lurker_points.csv", FileAccess.READ)
	var user_info_dict ={}
	while not file.eof_reached():
		var content = file.get_csv_line()
		print(content, 'hell yea')
		if content.size() > 1:
			user_info_dict[content[0]] = {"points": int(content[1]), "image_url": content[2]}
	print(user_info_dict)
	return user_info_dict
	

	
	
	

		
			




