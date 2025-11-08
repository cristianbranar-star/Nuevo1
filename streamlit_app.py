import streamlit as st

# --- CONTENIDO DE LAS GUÍAS ---
# Definimos todo el contenido de los descartes en un diccionario.
# (El contenido de GUIAS no cambia, se omite aquí por brevedad,
# pero está en el código final)
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
    if 'guia_actual' not in st.session_state:
        st.session_state.guia_actual = None
    if 'estado_final' not in st.session_state:
        st.session_state.estado_final = None # 'Resuelto en N1' o 'Escalado a N2'
    
    # NUEVO: Almacenará la bitácora de {paso_idx: {'comentario': ..., 'imagenes': [...]}}
    if 'documentacion_pasos' not in st.session_state:
        st.session_state.documentacion_pasos = {}

def mostrar_menu():
    """Muestra la pantalla del menú principal con botones."""
    st.title("👨‍🔧 Asistente de Descartes N1")
    st.header("Seleccione la categoría del problema:")

    for clave_guia, config in GUIAS.items():
        # Usamos st.button para crear un botón. Si se presiona, devuelve True.
        if st.button(f"{config['icono']} {config['titulo']}", use_container_width=True):
            # 1. Guardamos la guía seleccionada
            st.session_state.guia_actual = clave_guia
            # 2. Cambiamos la 'vista' en la memoria
            st.session_state.vista = clave_guia
            # 3. Reseteamos el contador de pasos
            st.session_state.paso_actual = 0
            # 4. NUEVO: Reseteamos la bitácora para el nuevo ticket
            st.session_state.documentacion_pasos = {}
            # 5. Forzamos un 'rerun' para que la app se redibuje con la nueva vista
            st.rerun()

def guardar_datos_paso():
    """NUEVA FUNCIÓN: Guarda los datos del paso actual en session_state."""
    paso_idx = st.session_state.paso_actual
    # Usamos .get() para leer los valores de los widgets (vinculados por 'key')
    # Si la clave no existe (p.ej. el widget aún no se ha renderizado), devuelve "" o []
    comentario = st.session_state.get(f"comment_{paso_idx}", "")
    imagenes = st.session_state.get(f"uploader_{paso_idx}", [])
    
    # Solo guardamos si hay algo que guardar
    if comentario or imagenes:
        guia = GUIAS[st.session_state.guia_actual]
        titulo_paso = guia['pasos'][paso_idx]['titulo']
        
        st.session_state.documentacion_pasos[paso_idx] = {
            'titulo_paso': titulo_paso,
            'comentario': comentario,
            'imagenes': imagenes
        }

def mostrar_guia_descarte(clave_guia):
    """Muestra el paso a paso de una guía específica."""
    
    guia = GUIAS[clave_guia]
    paso_idx = st.session_state.paso_actual
    total_pasos = len(guia['pasos'])

    st.header(f"{guia['icono']} {guia['titulo']}")
    
    # Botón para regresar al menú
    if st.button("‹‹ Cancelar y Volver al Menú"):
        st.session_state.vista = 'menu'
        st.session_state.guia_actual = None
        st.session_state.documentacion_pasos = {} # Limpiar bitácora
        st.rerun()

    st.divider()

    # Comprobar si hemos completado todos los pasos
    if paso_idx >= total_pasos:
        # --- Pantalla de Escalar a N2 ---
        st.session_state.vista = 'finalizar_ticket'
        st.session_state.estado_final = 'Escalado a N2'
        st.rerun()
    else:
        # --- Pantalla del Paso Actual ---
        paso_actual = guia['pasos'][paso_idx]
        
        # Barra de progreso visual
        st.progress((paso_idx + 1) / total_pasos, text=f"Paso {paso_idx + 1} de {total_pasos}")
        
        # Instrucción del paso
        st.subheader(paso_actual['titulo'])
        st.info(paso_actual['instruccion'])
        
        # --- INICIO DE NUEVOS CAMBIOS ---
        st.subheader("Bitácora de este Paso (Opcional)")
        
        # Usamos una clave ('key') única para cada widget.
        # Esto es VITAL para que Streamlit guarde su estado.
        st.text_area(
            "Comentarios sobre este paso:", 
            key=f"comment_{paso_idx}",
            placeholder="Escriba aquí lo que observó o la respuesta del usuario..."
        )
        
        st.file_uploader(
            "Subir evidencia para este paso:", 
            key=f"uploader_{paso_idx}",
            accept_multiple_files=True, 
            type=['png', 'jpg', 'jpeg']
        )
        # --- FIN DE NUEVOS CAMBIOS ---
        
        st.divider()

        # Botones de acción (Resuelto vs Siguiente)
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✅ Problema Resuelto", type="primary", use_container_width=True):
                guardar_datos_paso() # Guardar datos del último paso
                st.session_state.vista = 'finalizar_ticket'
                st.session_state.estado_final = 'Resuelto en N1'
                st.rerun()

        with col2:
            if st.button("❌ No se resolvió, siguiente paso", use_container_width=True):
                guardar_datos_paso() # Guardar datos del paso actual
                st.session_state.paso_actual += 1 # Avanzar al siguiente
                st.rerun()

def mostrar_pantalla_final():
    """Muestra la pantalla de tipificación, comentarios y carga de evidencia."""
    
    estado = st.session_state.estado_final
    guia_info = GUIAS[st.session_state.guia_actual]

    # Título dinámico basado en el estado
    if estado == 'Resuelto en N1':
        st.success(f"✅ ¡Ticket Resuelto! - {guia_info['titulo']}", icon="✅")
    else:
        st.error(f"⚠️ Ticket para Escalar a N2 - {guia_info['titulo']}", icon="🚨")

    # --- INICIO DE NUEVOS CAMBIOS: Resumen de Bitácora ---
    st.header("Resumen de Bitácora por Paso")
    if not st.session_state.documentacion_pasos:
        st.write("No se agregó documentación durante los pasos.")
    else:
        # Ordenamos por el índice del paso (clave del diccionario)
        for paso_idx, datos in sorted(st.session_state.documentacion_pasos.items()):
            with st.expander(f"**Paso {paso_idx + 1}: {datos['titulo_paso']}**", expanded=False):
                if datos['comentario']:
                    st.write(f"**Comentario:**")
                    st.markdown(f"> {datos['comentario'].replace('\n', '\n> ')}")
                if datos['imagenes']:
                    st.write(f"**Evidencia:** {len(datos['imagenes'])} archivo(s)")
                    for img in datos['imagenes']:
                        st.image(img, width=150, caption=img.name)
    st.divider()
    # --- FIN DE NUEVOS CAMBIOS ---
    
    # SE ELIMINA EL st.header("Documentación y Cierre Final")
    # SE ELIMINA EL st.write("Añada un comentario de cierre final para el ticket.")
    # SE ELIMINA el st.text_area("Comentarios de Cierre Final:...")
    
    # --- INICIO DE NUEVA LÓGICA ---
    
    # Generar el resumen consolidado para copiar y pegar
    resumen_para_copiar = []
    resumen_para_copiar.append(f"CATEGORÍA: {guia_info['titulo']}")
    resumen_para_copiar.append(f"ESTADO FINAL: {estado}")
    resumen_para_copiar.append("="*30)
    resumen_para_copiar.append("BITÁCORA DE DESCARTES REALIZADOS:")
    
    if not st.session_state.documentacion_pasos:
        resumen_para_copiar.append("\n- No se registraron comentarios durante los pasos.")
    else:
        for paso_idx, datos in sorted(st.session_state.documentacion_pasos.items()):
            resumen_para_copiar.append(f"\nPASO {paso_idx + 1}: {datos['titulo_paso']}")
            
            if datos['comentario']:
                # Formatear comentario para que sea legible
                comentario_limpio = '\n  '.join(datos['comentario'].splitlines())
                resumen_para_copiar.append(f"  Comentario: {comentario_limpio}")
            else:
                resumen_para_copiar.append("  Comentario: (Sin comentario)")
            
            if datos['imagenes']:
                resumen_para_copiar.append(f"  Evidencia: {len(datos['imagenes'])} imagen(es) adjunta(s).")

    # Unir todas las líneas del resumen en un solo string
    resumen_string_final = "\n".join(resumen_para_copiar)
    
    st.subheader("Resumen de Tipificación (Para Copiar)")
    st.write("Usa el siguiente resumen para documentar tu ticket en el sistema oficial.")
    
    st.text_area(
        "Resumen del Ticket:",
        value=resumen_string_final,
        height=300,
        disabled=True, # Deshabilitado para que sea solo de lectura (pero copiable)
        key="resumen_final_generado"
    )
    # --- FIN DE NUEVA LÓGICA ---
    
    # SE ELIMINA EL st.subheader("Resumen de Tipificación")
    # SE ELIMINA el st.write(f"**Categoría:** {guia_info['titulo']}")
    # SE ELIMINA el st.write(f"**Estado de Cierre:** {estado}")
    # SE ELIMINA el bloque 'if comentarios_finales:'
            
    st.divider()

    # Botón final para "guardar" y volver al menú
    if st.button("Guardar Ticket y Volver al Menú", type="primary", use_container_width=True):
        # Aquí es donde, en una app real, guardarías la info en una base de datos.
        
        # Limpiamos todo para el próximo ticket
        st.session_state.vista = 'menu'
        st.session_state.paso_actual = 0
        st.session_state.guia_actual = None
        st.session_state.estado_final = None
        st.session_state.documentacion_pasos = {}
        
        # Limpiamos los widgets finales manualmente por si acaso
        # SE ELIMINA LA LÍNEA 'st.session_state.comentarios_finales = ""'
        
        st.balloons()
        st.rerun()

# --- Punto de Entrada Principal de la App ---

# 1. Asegurarnos de que la "memoria" (session_state) esté inicializada
inicializar_estado()

# 2. "Enrutador": Decide qué pantalla mostrar basado en la 'vista' actual
if st.session_state.vista == 'menu':
    mostrar_menu()
elif st.session_state.vista == 'finalizar_ticket':
    mostrar_pantalla_final()
else:
    # Si la vista no es 'menu' ni 'finalizar_ticket', 
    # debe ser una de las claves de guía (ej: 'internet')
    mostrar_guia_descarte(st.session_state.vista)
