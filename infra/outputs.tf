output "cluster_name" {
  value = aws_ecs_cluster.cluster.name
}

output "alb_dns_name" {
  value = aws_lb.app.dns_name
}

output "app_url" {
  value = "http://${aws_lb.app.dns_name}"
}