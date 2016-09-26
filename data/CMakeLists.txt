### CMakeLists automatically created with AutoVala
### Do not edit

if (ATHOME)
	IF(IS_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/gedit_smarthome.plugin)
	install(DIRECTORY
		${CMAKE_CURRENT_SOURCE_DIR}/gedit_smarthome.plugin
	DESTINATION
		share/gedit/plugins/autovala
	)
ELSE()
	install(FILES
		${CMAKE_CURRENT_SOURCE_DIR}/gedit_smarthome.plugin
	DESTINATION
		share/gedit/plugins/autovala
	)
ENDIF()

else ()
	IF(IS_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/gedit_smarthome.plugin)
	install(DIRECTORY
		${CMAKE_CURRENT_SOURCE_DIR}/gedit_smarthome.plugin
	DESTINATION
		lib/gedit/plugins/autovala
	)
ELSE()
	install(FILES
		${CMAKE_CURRENT_SOURCE_DIR}/gedit_smarthome.plugin
	DESTINATION
		lib/gedit/plugins/autovala
	)
ENDIF()

endif ()

