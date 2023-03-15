# Definir la función y su derivada
f <- function(x) {
  return((2*x^2)*cos(x) - 5*x)
}

f_prime <- function(x) {
  return((4*x*cos(x) - 2*x^2*sin(x)) - 5)
}

# Seleccionar un valor inicial y una tasa de aprendizaje
x <- 1
learning_rate <- 0.01

# Crear una lista para guardar los valores de x
x_list <- list(x)

# Realizar varias actualizaciones de x
for (i in 1:1000) {
  x <- x - learning_rate * f_prime(x)
  x_list[[i+1]] <- x
}

# El valor final de x es una aproximación al mínimo de la función
print(x)

# Graficar la función y los puntos
library(ggplot2)

ggplot(data.frame(x = c(-10, 10)), aes(x)) +
  geom_line(aes(y = f(x))) +
  geom_point(aes(x = unlist(x_list), y = f(unlist(x_list))), color = "red") +
  labs(title = "Función (2*x^2)*cos(x) - 5x",
       x = "x", y = "f(x)")
