### CMakeLists automatically created with AutoVala
### Do not edit

if (ATHOME)
	IF(IS_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/gedit_closebutton.plugin)
	install(DIRECTORY
		${CMAKE_CURRENT_SOURCE_DIR}/gedit_closebutton.plugin
	DESTINATION
		share/gedit/plugins/closebutton
	)
ELSE()
	install(FILES
		${CMAKE_CURRENT_SOURCE_DIR}/gedit_closebutton.plugin
	DESTINATION
		share/gedit/plugins/closebutton
	)
ENDIF()

else ()
IF(IS_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/gedit_closebutton.plugin)
	install(DIRECTORY
		${CMAKE_CURRENT_SOURCE_DIR}/gedit_closebutton.plugin
	DESTINATION
		lib/gedit/plugins/closebutton
	)
ELSE()
	install(FILES
		${CMAKE_CURRENT_SOURCE_DIR}/gedit_closebutton.plugin
	DESTINATION
		lib/gedit/plugins/closebutton
	)
ENDIF()

endif ()
