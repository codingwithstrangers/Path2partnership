extends Sprite

var current_point = 0
onready var path_follow = get_parent()

export var _speed = 0

func _ready():
	lurker()
	pass
	
func _physics_process(delta):
	current_point += 1
	path_follow.progress_ratio = current_point /60.0
	
	
func lurker():
	var file = "F://Coding with Strangers//Path2partnership//lurker_points.csv"
	var content = file.get_csv_line()
	while not file.eof_reached():
		content = file.get_csv_line()
		print(content, 'hell yea')
	return content

