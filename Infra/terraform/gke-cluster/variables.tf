variable "region" {
  description = "Deployment region"
  default = "us-central1"
}
variable "clusterName" {
  description = "Name of our Cluster"
  default="tf-cluster"
}
variable "diskSize" {
  description = "Node disk size in GB"
  default = 100
}
variable "minNode" {
  description = "Minimum Node Count"
  default =1 
}
variable "maxNode" {
  description = "maximum Node Count"
  default = 5
}
variable "machineType" {
  description = "Node Instance machine type"
  default = "e2-medium"
}
variable vpc_name {
  type        = string
  default     = "mlops-vpc"
  description = "vpc-details"
}
