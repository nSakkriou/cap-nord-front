variable "bucket_name" {
  type = string
  default = "nsakkriou-prod-backup-bucket"
}

variable "access_key" {
  type = string
}

variable "secret_key" {
  type = string
}

variable "region" {
    type = string
    default = "eu-west-3"
}