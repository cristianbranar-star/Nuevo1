import streamlit as st

# --- CONTENIDO DE LAS GUÍAS ---
# Definimos todo el contenido de los descartes en un diccionario.
# Esto hace que sea fácil de agregar o modificar pasos sin tocar la lógica.
GUIAS = {
    'internet': {
        'icono': "🌐",
        'titulo': "Problemas de Conexión a Internet o Red",
        'pasos': [
            {
                "titulo": "Verificar Conexión Física (Cable/WiFi)",
                "instruccion": """
                * **(Si usa cable):** ¿Está el cable de red bien conectado en ambos extremos (computadora y puerto de red)?
                * **(Si usa WiFi):** ¿Está conectado a la red WiFi correcta de la empresa?
                * Pida al usuario que intente *olvidar la red* y volver a conectarse.
                """
            },
            {
                "titulo": "Reinicio Básico (Equipo)",
                "instruccion": """
                * Pida al usuario que **REINICIE** el equipo.
                * (El 90% de los problemas se resuelven aquí).
                """
            },
            {
                "titulo": "Probar conexión básica (Ping)",
                "instruccion": """
                * Abra **CMD** (Símbolo del sistema) en el equipo del usuario.
                * Escriba `ping 8.8.8.8` y presione Enter.
                * ¿Muestra 'Respuesta desde...' o 'Tiempo de espera agotado'?
                """
            },
            {
                "titulo": "Reiniciar comandos de red",
                "instruccion": """
                * En el **CMD**, ejecute los siguientes comandos (uno por uno):
                1.  `ipconfig /release`
                2.  `ipconfig /renew`
                * Esto forzará al equipo a solicitar una nueva dirección IP.
                """
            }
        ]
    },
    'impresora': {
        'icono': "🖨️",
        'titulo': "Problemas con la Impresora",
        'pasos': [
            {
                "titulo": "Verificar Estado Físico",
                "instruccion": """
                * ¿Está la impresora encendida?
                * ¿Tiene papel y tóner/tinta?
                * ¿Muestra algún código de error en su pantalla?
                """
            },
            {
                "titulo": "Reiniciar Impresora y Equipo",
                "instruccion": """
                * Apague la impresora, espere 30 segundos y vuelva a encenderla.
                * Pida al usuario que reinicie su equipo.
                """
            },
            {
                "titulo": "Reiniciar la Cola de Impresión (Spooler)",
                "instruccion": """
                * Vaya a **'Servicios'** (busque `services.msc` en Windows).
                * Busque el servicio **'Cola de impresión'** (Print Spooler).
                * Haga clic derecho > **Reiniciar**.
                """
            },
            {
                "titulo": "Verificar Impresora Predeterminada",
                "instruccion": """
                * Vaya a 'Configuración > Impresoras y escáneres'.
                * Asegúrese de que la impresora correcta esté seleccionada como predeterminada.
                * Intente imprimir una página de prueba desde allí.
                """
            }
        ]
    },
    'password': {
        'icono': "🔑",
        'titulo': "Problemas de Contraseña o Acceso (Login)",
        'pasos': [
            {
                "titulo": "Verificar Datos Básicos",
                "instruccion": """
                * ¿Está el **'Bloq Mayús'** (Caps Lock) activado?
                * ¿Está el usuario ingresando el nombre de usuario correcto? (Ej: 'juan.perez' en lugar de 'jperez')
                * ¿El teclado numérico (Num Lock) está activado si la clave usa números?
                """
            },
            {
                "titulo": "Desbloquear Cuenta (Active Directory)",
                "instruccion": """
                * Verifique en el **Active Directory (AD)** si la cuenta del usuario está bloqueada.
                * (Usualmente por muchos intentos fallidos).
                * Si está bloqueada, desbloquéela.
                """
            },
            {
                "titulo": "Forzar Restablecimiento de Contraseña (AD)",
                "instruccion": """
                * Si el usuario olvidó la contraseña, restablézcala desde el AD.
                * Asigne una contraseña temporal.
                * **¡IMPORTANTE!** Marque la casilla: *'El usuario debe cambiar la contraseña en el siguiente inicio de sesión'*.
                """
            },
            {
                "titulo": "(Si aplica) Portal de Autoservicio",
                "instruccion": """
                * Guíe al usuario para que utilice el portal de autoservicio de contraseñas, si la empresa tiene uno.
                * Recuérdele registrar sus preguntas de seguridad para el futuro.
                """
            }
        ]
    },
    'software': {
        'icono': "💻",
        'titulo': "Software Lento o No Responde (Outlook, Teams, etc.)",
        'pasos': [
            {
                "titulo": "Cerrar y Reabrir",
                "instruccion": """
                * Cierre completamente el programa (Outlook, Teams, Chrome, etc.).
                * **Tip:** Use el Administrador de Tareas (Ctrl+Shift+Esc) para 'Finalizar tarea' si no responde.
                * Espere 10 segundos y vuelva a abrirlo.
                """
            },
            {
                "titulo": "Reiniciar el Equipo",
                "instruccion": """
                * (El más efectivo) Pida al usuario que **REINICIE** su computadora.
                * Esto libera memoria RAM y cierra procesos 'colgados' que no se ven.
                """
            },
            {
                "titulo": "Verificar Administrador de Tareas",
                "instruccion": """
                * Pida al usuario que abra el **Administrador de Tareas** (Ctrl + Shift + Esc).
                * Revise la pestaña 'Procesos'.
                * ¿Están la **CPU** o la **Memoria (RAM)** al 90-100%?
                * Si es así, identifique el proceso que consume recursos.
                """
            },
            {
                "titulo": "(Si aplica) Borrar Caché",
                "instruccion": """
                * **Navegador (Chrome/Edge):** Pida borrar caché y cookies.
                * **Teams:** Existe un procedimiento para borrar la caché de Teams (implica cerrar Teams y borrar carpetas en %appdata%).
                * **Outlook:** Revise el tamaño del archivo .OST.
                """
            }
        ]
    }
}

# --- LÓGICA DE LA APLICACIÓN ---

def inicializar_estado():
    """Configura el estado inicial de la sesión."""
    # 'st.session_state' es un diccionario que Streamlit guarda entre ejecuciones.
    # Es la "memoria" de la app.
    if 'vista' not in st.session_state:
        st.session_state.vista = 'menu'
    if 'paso_actual' not in st.session_state:
        st.session_state.paso_actual = 0

def mostrar_menu():
    """Muestra la pantalla del menú principal con botones."""
    st.title("👨‍🔧 Asistente de Descartes N1")
    st.header("Seleccione la categoría del problema:")

    for clave_guia, config in GUIAS.items():
        # Usamos st.button para crear un botón. Si se presiona, devuelve True.
        if st.button(f"{config['icono']} {config['titulo']}", use_container_width=True):
            # 1. Cambiamos la 'vista' en la memoria
            st.session_state.vista = clave_guia
            # 2. Reseteamos el contador de pasos
            st.session_state.paso_actual = 0
            # 3. Forzamos un 'rerun' para que la app se redibuje con la nueva vista
            st.rerun()

def mostrar_guia_descarte(clave_guia):
    """Muestra el paso a paso de una guía específica."""
    
    guia = GUIAS[clave_guia]
    paso_idx = st.session_state.paso_actual
    total_pasos = len(guia['pasos'])

    st.header(f"{guia['icono']} {guia['titulo']}")
    
    # Botón para regresar al menú
    if st.button("‹‹ Volver al Menú Principal"):
        st.session_state.vista = 'menu'
        st.rerun()

    st.divider()

    # Comprobar si hemos completado todos los pasos
    if paso_idx >= total_pasos:
        # --- Pantalla de Escalar a N2 ---
        st.error("⚠️ **DESCARTE N1 AGOTADO** ⚠️", icon="🚨")
        st.subheader("Acción Requerida:")
        st.markdown(
            """
            1.  **No se pudo resolver en N1.**
            2.  **Documente** todos los pasos realizados en el ticket.
            3.  **Escale** el ticket al equipo de N2 (Nivel 2) con toda la información.
            """
        )
    else:
        # --- Pantalla del Paso Actual ---
        paso_actual = guia['pasos'][paso_idx]
        
        # Barra de progreso visual
        st.progress((paso_idx + 1) / total_pasos, text=f"Paso {paso_idx + 1} de {total_pasos}")
        
        # Instrucción del paso
        st.subheader(paso_actual['titulo'])
        st.info(paso_actual['instruccion'])
        
        st.divider()

        # Botones de acción (Resuelto vs Siguiente)
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✅ Problema Resuelto", type="primary", use_container_width=True):
                st.success("¡Excelente! Registre el ticket como resuelto.")
                st.balloons()
                # Volvemos al menú
                st.session_state.vista = 'menu'
                # st.rerun() no es necesario aquí, Streamlit lo hará al terminar el script
                # pero lo añadimos para claridad.
                st.rerun()

        with col2:
            if st.button("❌ No se resolvió, siguiente paso", use_container_width=True):
                # Aumentamos el contador de pasos en la memoria
                st.session_state.paso_actual += 1
                # Forzamos un rerun para mostrar el siguiente paso
                st.rerun()


# --- Punto de Entrada Principal de la App ---

# 1. Asegurarnos de que la "memoria" (session_state) esté inicializada
inicializar_estado()

# 2. "Enrutador": Decide qué pantalla mostrar basado en la 'vista' actual
if st.session_state.vista == 'menu':
    mostrar_menu()
else:
    # Si la vista no es 'menu', debe ser una de las claves de guía (ej: 'internet')
    mostrar_guia_descarte(st.session_state.vista)
