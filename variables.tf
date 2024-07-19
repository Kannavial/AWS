variable "aws_region" {
  description = "The AWS region to create resources in"
  default     = "ap-southeast-1"
}

variable "instance_type" {
  description = "Type of EC2 instance"
  default     = "t2.micro"
}