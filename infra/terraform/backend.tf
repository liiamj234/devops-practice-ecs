terraform {
  backend "s3" {
    bucket       = "liam-tfstate-ecs-2026-12345"
    key          = "devops-practice-ecs/terraform.tfstate"
    region       = "ap-southeast-2"
    encrypt      = true
    use_lockfile = true
  }
}