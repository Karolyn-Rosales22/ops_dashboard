variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "app_name" {
  description = "Application name"
  type        = string
  default     = "dc-dashboard-karol"
}

variable "account_id" {
  description = "AWS Account ID"
  type        = string
}