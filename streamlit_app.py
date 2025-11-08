import streamlit as st

# --- CONTENIDO DE LAS GUÍAS ---
# Definimos todo el contenido de los descartes en un diccionario.
# Esta es la única sección que necesitas modificar para agregar o cambiar pasos.
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
    },
    'vpn': {
        'icono': "🛡️",
        'titulo': "Descartes VPN (FortiClient)",
        'pasos': [
            {
                "titulo": "Verificar Conectividad Básica",
                "instruccion": """
                * **¿El usuario tiene internet?** Pida al usuario que abra una página web pública (ej: google.com).
                * La VPN no funciona si no hay una conexión a internet primero.
                """
            },
            {
                "titulo": "Verificar Credenciales y Errores",
                "instruccion": """
                * Pida al usuario que le lea el error exacto que muestra FortiClient (Ej: "Error -8", "Credenciales incorrectas").
                * **(Si es "Credenciales incorrectas"):** Es la misma contraseña de Windows/AD. Pida al usuario que la verifique o que intente iniciar sesión en otro servicio (ej: Outlook Web) para confirmar la contraseña.
                """
            },
            {
                "titulo": "Reiniciar el Servicio de FortiClient",
                "instruccion": """
                * A veces el servicio "se pega". Pida al usuario que reinicie el equipo (la solución más fácil).
                * **(Avanzado N1):** Abra `services.msc` (Servicios), busque "FortiClient Service Scheduler", y haga clic en "Reiniciar".
                """
            },
            {
                "titulo": "Verificar Versión del Cliente",
                "instruccion": """
                * Verifique que el usuario tenga la versión de FortiClient aprobada por la empresa.
                * Si la versión es muy antigua, es posible que la política de seguridad la esté bloqueando.
                * (Documente la versión y escale si es necesario reinstalar).
                """
            }
        ]
    },
    'telefonia': {
        'icono': "🎧",
        'titulo': "Descartes Telefonía (Cisco Webex Desktop)",
        'pasos': [
            {
                "titulo": "Verificar Dispositivos de Audio (El más común)",
                "instruccion": """
                * **1. En Windows:** Haga clic en el ícono de altavoz (junto al reloj) y verifique que el dispositivo de salida sea la diadema/audífonos (Ej: "Jabra", "Plantronics").
                * **2. En Webex:** Vaya a `Configuración > Audio` y asegúrese de que **Altavoz** y **Micrófono** estén seleccionados en la diadema correcta (no en los "Altavoces del PC").
                """
            },
            {
                "titulo": "Cerrar y Reabrir Webex",
                "instruccion": """
                * Cierre Webex completamente.
                * **Importante:** Vaya al Administrador de Tareas (Ctrl+Shift+Esc) y finalice cualquier proceso de "Webex" que pueda seguir colgado.
                * Vuelva a abrir la aplicación.
                """
            },
            {
                "titulo": "Verificar Estado de Conexión de Webex",
                "instruccion": """
                * Dentro de Webex, ¿aparecen todos los servicios con un punto verde?
                * ¿Muestra "Conectado" o algún error de "Sin conexión"?
                * Si está desconectado, el problema puede ser de red/VPN (verifique esa guía).
                """
            },
            {
                "titulo": "Borrar Caché de Webex",
                "instruccion": """
                * Cierre Webex completamente (incluyendo el Administrador de Tareas).
                * Abra "Ejecutar" (Tecla Windows + R) y escriba `%appdata%`.
                * Busque y elimine las carpetas relacionadas con "Cisco" o "Webex".
                * (Este paso usualmente requiere escalado o un instructivo detallado).
                """
            }
        ]
    },
    'carpetas': {
        'icono': "📁",
        'titulo': "Permisos y Mapeo de Carpetas Compartidas",
        'pasos': [
            {
                "titulo": "Verificar Conexión a la Red (VPN)",
                "instruccion": """
                * **¿El usuario está en la oficina o en casa?**
                * Si está en casa, **DEBE** estar conectado a la VPN para acceder a las carpetas compartidas.
                * Pida que verifique su conexión a la VPN (Ver guía de FortiClient).
                """
            },
            {
                "titulo": "Distinguir el Error (Clave)",
                "instruccion": """
                * Pida al usuario que intente acceder a la ruta (ej: `\\servidor\carpeta`) y le lea el error exacto:
                * **"No se encuentra la ruta" (Path not found):** Es un problema de red. Verifique el Paso 1 (VPN) o que la ruta esté bien escrita.
                * **"Acceso Denegado" (Access Denied):** Es un problema de permisos. Vaya al Paso 3.
                """
            },
            {
                "titulo": "Verificar Permisos (Si es 'Acceso Denegado')",
                "instruccion": """
                * Este error significa que el usuario SÍ PUEDE ver la carpeta, pero no tiene permisos.
                * **Acción N1:** Verifique en Active Directory (AD) que el usuario pertenezca al Grupo de Seguridad correcto para esa carpeta (Ej: "Finanzas_Lectura").
                * Si no está, debe gestionar la solicitud de permiso con el dueño de la carpeta (Data Owner).
                """
            },
            {
                "titulo": "Cómo Mapear la Carpeta (Si no existe)",
                "instruccion": """
                * Vaya a **"Este Equipo"**.
                * Haga clic en los tres puntos "..." > **"Conectar a unidad de red"** (Map network drive).
                * **Unidad:** Elija una letra disponible (Ej: `S:`).
                * **Carpeta:** Escriba la ruta completa (Ej: `\\servidor\compartido\finanzas`).
                * Asegúrese de marcar **"Reconectar al iniciar sesión"**.
                """
            },
            {
                "titulo": "Forzar Actualización de Políticas (gpupdate)",
                "instruccion": """
                * Si acaba de agregar al usuario a un grupo de permisos en AD, los cambios no son instantáneos.
                * Pida al usuario que **REINICIE** el equipo.
                * **(Avanzado N1):** Abra CMD y escriba `gpupdate /force`. Espere a que termine e intente acceder de nuevo.
                """
            }
        ]
    }
}


# --- LÓGICA DE LA APLICACIÓN ---
# (No modificar a menos que se cambie la funcionalidad)

def inicializar_estado():
    """Configura el estado inicial de la sesión."""
    # 'st.session_state' es un diccionario que Streamlit guarda entre ejecuciones.
    # Es la "memoria" de la app.
    
    # 'vista' controla qué pantalla mostramos: 'menu', 'guia', 'finalizar'
    if 'vista' not in st.session_state:
        st.session_state.vista = 'menu'
        
    # 'clave_guia' guarda la guía que estamos viendo (ej: 'internet')
    if 'clave_guia' not in st.session_state:
        st.session_state.clave_guia = None
        
    # 'paso_actual' es el índice del paso (ej: 0, 1, 2...)
    if 'paso_actual' not in st.session_state:
        st.session_state.paso_actual = 0
        
    # 'documentacion_pasos' guarda la bitácora de comentarios e imágenes
    if 'documentacion_pasos' not in st.session_state:
        st.session_state.documentacion_pasos = {} # Ej: {0: {"comentario": "...", "imagenes": [...]}}
        
    # 'estado_final' guarda si fue 'Resuelto' o 'Escalado'
    if 'estado_final' not in st.session_state:
        st.session_state.estado_final = None

def guardar_datos_paso():
    """
    Toma los datos de los widgets del paso actual y los guarda
    en st.session_state.documentacion_pasos antes de avanzar.
    """
    paso_idx = st.session_state.paso_actual
    guia_actual = GUIAS[st.session_state.clave_guia]
    titulo_paso = guia_actual['pasos'][paso_idx]['titulo']
    
    # Claves únicas para los widgets de este paso
    key_comentario = f"comentario_paso_{paso_idx}"
    key_imagenes = f"imagenes_paso_{paso_idx}"
    
    # Leer datos de los widgets (si existen en el estado)
    comentario = st.session_state.get(key_comentario, "")
    imagenes = st.session_state.get(key_imagenes, [])
    
    # Guardar en el diccionario de documentación
    st.session_state.documentacion_pasos[paso_idx] = {
        "titulo_paso": titulo_paso,
        "comentario": comentario,
        "imagenes": [img.name for img in imagenes] # Guardamos solo los nombres por simplicidad
    }

def mostrar_menu():
    """Muestra la pantalla del menú principal con botones."""
    st.title("👨‍🔧 Asistente de Descartes N1")
    st.header("Seleccione la categoría del problema:")

    # Iterar sobre el diccionario GUIAS para crear los botones
    for clave_guia, config in GUIAS.items():
        if st.button(f"{config['icono']} {config['titulo']}", use_container_width=True, key=f"btn_{clave_guia}"):
            # 1. Guardar la guía seleccionada
            st.session_state.clave_guia = clave_guia
            # 2. Cambiar la 'vista' a 'guia'
            st.session_state.vista = 'guia'
            # 3. Resetear contadores y bitácora
            st.session_state.paso_actual = 0
            st.session_state.documentacion_pasos = {}
            st.session_state.estado_final = None
            # 4. Forzar un 'rerun' para que la app se redibuje
            st.rerun()

def mostrar_guia_descarte():
    """Muestra el paso a paso de una guía específica."""
    
    clave_guia = st.session_state.clave_guia
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
        # --- Pantalla de Escalar a N2 (automático) ---
        st.error("⚠️ **DESCARTE N1 AGOTADO** ⚠️", icon="🚨")
        st.subheader("Acción Requerida:")
        st.markdown(
            """
            1.  **No se pudo resolver en N1.**
            2.  Todos los pasos de descarte se han completado.
            3.  El ticket debe ser escalado al equipo de N2 (Nivel 2).
            """
        )
        
        # Botón para ir a la pantalla final de documentación
        if st.button("Continuar para Documentar y Escalar", use_container_width=True, type="primary"):
            st.session_state.estado_final = "Escalado a N2"
            st.session_state.vista = 'finalizar'
            st.rerun()
    else:
        # --- Pantalla del Paso Actual ---
        paso_actual = guia['pasos'][paso_idx]
        
        # Barra de progreso visual
        st.progress((paso_idx + 1) / total_pasos, text=f"Paso {paso_idx + 1} de {total_pasos}")
        
        # Instrucción del paso
        st.subheader(paso_actual['titulo'])
        st.info(paso_actual['instruccion'])
        
        st.divider()
        
        # --- Sección de Bitácora por Paso ---
        st.subheader("Bitácora de este paso (Opcional)")
        
        # Claves únicas para los widgets
        key_comentario = f"comentario_paso_{paso_idx}"
        key_imagenes = f"imagenes_paso_{paso_idx}"

        st.text_area(
            f"Comentarios (Paso {paso_idx + 1}):", 
            key=key_comentario,
            placeholder="Escriba aquí cualquier detalle relevante de este paso..."
        )
        st.file_uploader(
            f"Adjuntar evidencia (Paso {paso_idx + 1}):", 
            key=key_imagenes,
            type=["png", "jpg", "jpeg", "bmp"],
            accept_multiple_files=True
        )
        
        st.divider()

        # Botones de acción (Resuelto vs Siguiente)
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✅ Problema Resuelto", type="primary", use_container_width=True):
                # 1. Guardar datos del paso actual
                guardar_datos_paso()
                # 2. Marcar estado final y cambiar vista
                st.session_state.estado_final = "Resuelto en N1"
                st.session_state.vista = 'finalizar'
                st.rerun()

        with col2:
            if st.button("❌ No se resolvió, siguiente paso", use_container_width=True):
                # 1. Guardar datos del paso actual
                guardar_datos_paso()
                # 2. Aumentar el contador de pasos
                st.session_state.paso_actual += 1
                # 3. Forzar un rerun para mostrar el siguiente paso
                st.rerun()

def mostrar_pantalla_final():
    """
    Muestra la pantalla final.
    Genera un resumen consolidado de la bitácora para copiar y pegar.
    """
    
    estado = st.session_state.estado_final
    guia_info = GUIAS[st.session_state.clave_guia]
    
    if estado == "Resuelto en N1":
        st.success(f"✅ ¡Problema Resuelto! - {guia_info['titulo']}")
    else:
        st.error(f"🚨 Escalado a N2 - {guia_info['titulo']}")
    
    st.divider()

    # --- Generar el resumen consolidado para copiar y pegar ---
    
    resumen_para_copiar = []
    resumen_para_copiar.append(f"CATEGORÍA: {guia_info['titulo']}")
    resumen_para_copiar.append(f"ESTADO FINAL: {estado}")
    resumen_para_copiar.append("="*30)
    resumen_para_copiar.append("BITÁCORA DE DESCARTES REALIZADOS:")
    
    # Revisar si el diccionario de documentación está vacío
    if not st.session_state.documentacion_pasos:
        resumen_para_copiar.append("\n- No se registraron comentarios durante los pasos.")
    else:
        # Iterar sobre los pasos documentados, ordenados por índice
        for paso_idx, datos in sorted(st.session_state.documentacion_pasos.items()):
            resumen_para_copiar.append(f"\nPASO {paso_idx + 1}: {datos['titulo_paso']}")
            
            if datos['comentario']:
                # Formatear comentario para que sea legible (indentar)
                comentario_limpio = '\n  '.join(datos['comentario'].splitlines())
                resumen_para_copiar.append(f"  Comentario: {comentario_limpio}")
            else:
                resumen_para_copiar.append("  Comentario: (Sin comentario)")
            
            if datos['imagenes']:
                resumen_para_copiar.append(f"  Evidencia: {len(datos['imagenes'])} imagen(es) adjunta(s).")
            else:
                resumen_para_copiar.append("  Evidencia: (Sin evidencia)")

    # Unir todas las líneas del resumen en un solo string
    resumen_string_final = "\n".join(resumen_para_copiar)
    
    st.subheader("Resumen de Tipificación (Para Copiar)")
    st.write("Usa el siguiente resumen para documentar tu ticket en el sistema oficial (ServiceNow, JIRA, etc.).")
    
    # Mostrar el resumen en un área de texto deshabilitada (fácil de copiar)
    st.text_area(
        "Resumen del Ticket:",
        value=resumen_string_final,
        height=350,
        disabled=True, 
        key="resumen_final_generado"
    )
            
    st.divider()

    # Botón final para "guardar" y volver al menú
    if st.button("Finalizar y Volver al Menú", use_container_width=True, type="primary"):
        # Limpiar todo y volver al menú
        st.session_state.vista = 'menu'
        st.session_state.clave_guia = None
        st.session_state.paso_actual = 0
        st.session_state.estado_final = None
        st.session_state.documentacion_pasos = {}
        
        st.balloons()
        st.rerun()


# --- Punto de Entrada Principal de la App ---

# 1. Asegurarnos de que la "memoria" (session_state) esté inicializada
inicializar_estado()

# 2. "Enrutador": Decide qué pantalla mostrar basado en la 'vista' actual
if st.session_state.vista == 'menu':
    mostrar_menu()
elif st.session_state.vista == 'guia':
    mostrar_guia_descarte()
elif st.session_state.vista == 'finalizar':
    mostrar_pantalla_final()
