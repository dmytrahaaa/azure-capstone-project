terraform {
  required_version = ">=1.0.1"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.65.0"
    }
  }
}

provider "azurerm" {
  subscription_id = var.subscription_id
  features {}
}

module "observability" {
  source = "../modules/observability"
  prefix   = var.prefix
  location = var.location
}

module "faas" {
  source = "../modules/faas_eh_sa"

  prefix   = var.prefix
  location = var.location

  log_analytics_workspace_id = module.observability.log_analytics_workspace_id
}
