extends Sprite2D

var current_point = 0
@onready var path_follow = get_parent()

@export var _speed = 0

func _ready():
	pass
	
func _physics_process(delta):
	current_point += 1
	path_follow.progress_ratio = current_point /60.0
