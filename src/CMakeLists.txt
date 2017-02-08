### CMakeLists automatically created with AutoVala
### Do not edit

set (DATADIR "${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_DATAROOTDIR}")
set (PKGDATADIR "${DATADIR}/smarthome")
set (GETTEXT_PACKAGE "smarthome")
set (RELEASE_NAME "smarthome")
set (CMAKE_C_FLAGS "")
set (PREFIX ${CMAKE_INSTALL_PREFIX})
set (VERSION "1.0.0")
set (TESTSRCDIR "${CMAKE_SOURCE_DIR}")
set (DOLLAR "$")

configure_file (${CMAKE_SOURCE_DIR}/src/Config.vala.base ${CMAKE_BINARY_DIR}/src/Config.vala)
add_definitions(-DGETTEXT_PACKAGE=\"${GETTEXT_PACKAGE}\")
configure_file (${CMAKE_CURRENT_SOURCE_DIR}/gedit_smarthome.pc ${CMAKE_CURRENT_BINARY_DIR}/gedit_smarthome.pc)
configure_file (${CMAKE_CURRENT_SOURCE_DIR}/gedit_smarthome.deps ${CMAKE_CURRENT_BINARY_DIR}/gedit_smarthome.deps)
set (VERSION "1.0.0")
add_definitions (${DEPS_CFLAGS})
link_libraries ( ${DEPS_LIBRARIES} )
link_directories ( ${DEPS_LIBRARY_DIRS} )
find_package (Vala REQUIRED)
include (ValaVersion)
ensure_vala_version ("0.32" MINIMUM)
include (ValaPrecompile)

set (VALA_PACKAGES ${VALA_PACKAGES} atk)
set (VALA_PACKAGES ${VALA_PACKAGES} gdk-3.0)
set (VALA_PACKAGES ${VALA_PACKAGES} gedit)
set (VALA_PACKAGES ${VALA_PACKAGES} gio-2.0)
set (VALA_PACKAGES ${VALA_PACKAGES} glib-2.0)
set (VALA_PACKAGES ${VALA_PACKAGES} gobject-2.0)
set (VALA_PACKAGES ${VALA_PACKAGES} gobject-introspection-1.0)
set (VALA_PACKAGES ${VALA_PACKAGES} gtk+-3.0)
set (VALA_PACKAGES ${VALA_PACKAGES} gtksourceview-3.0)
set (VALA_PACKAGES ${VALA_PACKAGES} libpeas-1.0)

set (APP_SOURCES ${APP_SOURCES} ${CMAKE_CURRENT_BINARY_DIR}/Config.vala)
set (APP_SOURCES ${APP_SOURCES} smarthome.vala)

if (ATHOME)
	set (COMPILE_OPTIONS ${COMPILE_OPTIONS} -D ATHOME)
	set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DATHOME " )
	set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DATHOME " )
endif ()

if ((${CMAKE_BUILD_TYPE} STREQUAL "Debug") OR (${CMAKE_BUILD_TYPE} STREQUAL "RelWithDebInfo"))
	set(COMPILE_OPTIONS ${COMPILE_OPTIONS} "-g")
endif()

set (COMPILE_OPTIONS ${COMPILE_OPTIONS} --library=gedit_smarthome --gir gedit_smarthome-1.0.gir )

vala_precompile(VALA_C gedit_smarthome
	${APP_SOURCES}
PACKAGES
	${VALA_PACKAGES}
OPTIONS
	${COMPILE_OPTIONS}
GENERATE_VAPI
	gedit_smarthome
GENERATE_HEADER
	gedit_smarthome
)

add_library(gedit_smarthome SHARED ${VALA_C})

set_target_properties( gedit_smarthome PROPERTIES
VERSION
	1.0.0
SOVERSION
	1 )

if (ATHOME)
	set (INSTALL_LIBRARY_gedit_smarthome "share/gedit/plugins/smarthome" )
set (INSTALL_INCLUDE_gedit_smarthome "share/gedit/plugins/smarthome" )
set (INSTALL_VAPI_gedit_smarthome "share/gedit/plugins/smarthome" )
set (INSTALL_GIR_gedit_smarthome "share/gedit/plugins/smarthome" )
set (INSTALL_PKGCONFIG_gedit_smarthome "share/gedit/plugins/smarthome" )
else ()
set (INSTALL_LIBRARY_gedit_smarthome "lib/gedit/plugins/smarthome" )
set (INSTALL_INCLUDE_gedit_smarthome "lib/gedit/plugins/smarthome" )
set (INSTALL_VAPI_gedit_smarthome "lib/gedit/plugins/smarthome" )
set (INSTALL_GIR_gedit_smarthome "lib/gedit/plugins/smarthome" )
set (INSTALL_PKGCONFIG_gedit_smarthome "lib/gedit/plugins/smarthome" )
endif ()

install(TARGETS
	gedit_smarthome
LIBRARY DESTINATION
	${INSTALL_LIBRARY_gedit_smarthome}/
)
install(FILES
	${CMAKE_CURRENT_BINARY_DIR}/gedit_smarthome.h
DESTINATION
	${INSTALL_INCLUDE_gedit_smarthome}/
)
install(FILES
	${CMAKE_CURRENT_BINARY_DIR}/gedit_smarthome.vapi
DESTINATION
	${INSTALL_VAPI_gedit_smarthome}/
)
install(FILES
	${CMAKE_CURRENT_BINARY_DIR}/gedit_smarthome.deps
DESTINATION
	${INSTALL_VAPI_gedit_smarthome}/
)
install(FILES
	${CMAKE_CURRENT_BINARY_DIR}/gedit_smarthome-1.0.gir
DESTINATION
	${INSTALL_GIR_gedit_smarthome}/
)
install(FILES
	${CMAKE_CURRENT_BINARY_DIR}/gedit_smarthome.pc
DESTINATION
	${INSTALL_PKGCONFIG_gedit_smarthome}/
)
if(HAVE_VALADOC)
	valadoc(gedit_smarthome
		${CMAKE_BINARY_DIR}/valadoc/gedit_smarthome
		${APP_SOURCES}
	PACKAGES
		${VALA_PACKAGES}
	CUSTOM_VAPIS
		${CUSTOM_VAPIS_LIST}
	)
	install(DIRECTORY
		${CMAKE_BINARY_DIR}/valadoc
	DESTINATION
		${CMAKE_INSTALL_DATAROOTDIR}/doc/smarthome
	)
endif()

install(CODE "MESSAGE (\"
************************************************
* Run 'sudo ldconfig' to complete installation *
************************************************

\") " )