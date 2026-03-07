variable "region"        { default = "ap-southeast-2" }
variable "app_name"      { default = "devops-practice-ecs" }
variable "image_tag"     { default = "bootstrap" }
variable "cpu"           { default = 256 }
variable "memory"        { default = 512 }
variable "desired_count" { default = 1 }