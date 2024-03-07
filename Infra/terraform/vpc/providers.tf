provider "google" {
  credentials = file("../sa-keys.json")
  project     = "spherical-elf-334814"
  region      = "us-central1"
}