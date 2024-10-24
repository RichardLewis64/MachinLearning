import streamlit as st
import streamlit_authenticator as stauth
import yaml

# Sistema de autenticación
def authenticate_user():
    # Crear un archivo de configuración para los usuarios
    config = {
        'credentials': {
            'usernames': {
                'usuario1': {
                    'name': 'Alexander',
                    'password': '12345'  # ¡Recuerda usar contraseñas encriptadas en un proyecto real!
                },
                'usuario2': {
                    'name': 'Richard',
                    'password': 'abcdef'  # Ejemplo de otra contraseña
                }
            }
        },
        'cookie': {
            'expiry_days': 30,
            'key': 'my_secret_key'  # Cambia esto por una clave segura
        },
        'preauthorized': {}
    }

    # Autenticador
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    # Mostrar la interfaz de inicio de sesión
    name, authentication_status, username = authenticator.login("Iniciar sesión", "main")

    # Verificar el estado de autenticación
    if authentication_status:
        st.success(f"Bienvenido, {name}")
        return True
    elif authentication_status is False:
        st.error("Nombre de usuario o contraseña incorrectos")
        return False
    elif authentication_status is None:
        st.warning("Por favor, introduce tus credenciales")
        return False

# Programa principal
def main():
    # Verificar si el usuario está autenticado
    if authenticate_user():
        # Aquí puedes mostrar el contenido de la aplicación principal
        st.title("Sistema de Predicción de Ventas")

        # Continúa con la lógica de tu aplicación principal
        st.write("Aquí va el contenido de la aplicación después del login.")
    else:
        st.write("Esperando autenticación...")

if __name__ == '__main__':
    main()