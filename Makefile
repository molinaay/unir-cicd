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
						docker exec -i contenedor-api-calculadora-server pytest unit/ --cov --cov-report=xml:resultados/cobertura/pruebas_unitarias.xml --cov-report=html:resultados/cobertura/pruebas_unitarias --junit-xml=resultados/junit/pruebas_unitarias_junit.xml

						docker exec -i contenedor-api-calculadora-server pytest rest/ --cov --cov-report=xml:resultados/cobertura/pruebas_rest.xml --cov-report=html:resultados/cobertura/pruebas_rest --junit-xml=resultados/junit/pruebas_rest_junit.xml

ejecutar-pruebas-e2e:
					docker compose up -d servicio-cypress


