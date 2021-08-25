resource "azurerm_resource_group" "faas_eh_sa" {
  name     = "${var.prefix}-faas-eh-sa-rg"
  location = var.location
}

resource "random_string" "faas_salt" {
  length  = 4
  special = false
  upper   = false
}
