limpiar-contenedores:
					docker rm -f contenedor-api-calculadora-server
					docker rm -f contenedor-api-calculadora-tests
					docker rm -f contenedor-web-calculadora
					docker rm -f contenedor-cypress
limpiar-imagenes:
					docker rmi -f imagen-api-calculadora:v1
					docker rmi -f imagen-web-calculadora:v1					
arrancar-server-api:
					docker compose up -d servicio-api-calculadora
arrancar-server-web:
					docker compose up -d servicio-web-calculadora
ejecutar-pruebas-unitarias:
						docker compose up -d servicio-api-calculadora-tests
ejecutar-pruebas-e2e:
					docker compose up -d servicio-cypress


