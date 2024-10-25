import streamlit as st
import streamlit_authenticator as stauth
import yaml

def authenticate_user():
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

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    name, authentication_status, username = authenticator.login("Iniciar sesión", "main")

    if authentication_status:
        st.success(f"Bienvenido, {name}")
        return True
    elif authentication_status is False:
        st.error("Nombre de usuario o contraseña incorrectos")
        return False
    elif authentication_status is None:
        st.warning("Por favor, introduce tus credenciales")
        return False
