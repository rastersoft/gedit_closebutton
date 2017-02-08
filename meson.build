project('closebutton',['c','vala'])

ATHOME = (get_option('ATHOME') != '')

add_global_arguments('-DGETTEXT_PACKAGE="closebutton"',language: 'c')

atk_dep = dependency('atk')
cairo_dep = dependency('cairo')
gdk_3_0_dep = dependency('gdk-3.0')
gdk_pixbuf_2_0_dep = dependency('gdk-pixbuf-2.0')
gedit_dep = dependency('gedit')
gee_0_8_dep = dependency('gee-0.8')
gio_2_0_dep = dependency('gio-2.0')
glib_2_0_dep = dependency('glib-2.0')
gobject_2_0_dep = dependency('gobject-2.0')
gobject_introspection_1_0_dep = dependency('gobject-introspection-1.0')
gtk_3_0_dep = dependency('gtk+-3.0')
gtksourceview_3_0_dep = dependency('gtksourceview-3.0')
libpeas_1_0_dep = dependency('libpeas-1.0')
pango_dep = dependency('pango')
x11_dep = dependency('x11')

if ATHOME
	meson.add_install_script(join_paths(meson.current_source_dir(),'meson_scripts','install_data.sh'),join_paths(get_option('prefix'),'share/gedit/plugins/closebutton'),join_paths(meson.current_source_dir(),'data','gedit_closebutton.plugin'))

else
	meson.add_install_script(join_paths(meson.current_source_dir(),'meson_scripts','install_data.sh'),join_paths(get_option('prefix'),'lib/gedit/plugins/closebutton'),join_paths(meson.current_source_dir(),'data','gedit_closebutton.plugin'))

endif
meson.add_install_script(join_paths(meson.current_source_dir(),'meson_scripts','install_data.sh'),join_paths(get_option('prefix'),get_option('datadir'),'closebutton'),join_paths(meson.current_source_dir(),'data/local','','*'))

meson.add_install_script(join_paths(meson.current_source_dir(),'meson_scripts','install_data.sh'),join_paths(get_option('prefix'),get_option('datadir'),'doc'),join_paths(meson.current_source_dir(),'doc','','*'))

cfg_closebutton = configuration_data()
cfg_closebutton.set('DATADIR', join_paths(get_option('prefix'),get_option('datadir')))
cfg_closebutton.set('PKGDATADIR', join_paths(get_option('prefix'),get_option('datadir'),'closebutton'))
cfg_closebutton.set('GETTEXT_PACKAGE', 'closebutton')
cfg_closebutton.set('RELEASE_NAME', 'closebutton')
cfg_closebutton.set('PREFIX', get_option('prefix'))
cfg_closebutton.set('VERSION', '1.0.0')
cfg_closebutton.set('TESTSRCDIR', meson.current_source_dir())

cfgfile_1 = configure_file(input: 'src/Config.vala.base',output: 'Config_1.vala',configuration: cfg_closebutton)

closebutton_deps = [atk_dep]
closebutton_deps += [cairo_dep]
closebutton_deps += [gdk_3_0_dep]
closebutton_deps += [gdk_pixbuf_2_0_dep]
closebutton_deps += [gedit_dep]
closebutton_deps += [gee_0_8_dep]
closebutton_deps += [gio_2_0_dep]
closebutton_deps += [glib_2_0_dep]
closebutton_deps += [gobject_2_0_dep]
closebutton_deps += [gobject_introspection_1_0_dep]
closebutton_deps += [gtk_3_0_dep]
closebutton_deps += [gtksourceview_3_0_dep]
closebutton_deps += [libpeas_1_0_dep]
closebutton_deps += [pango_dep]
closebutton_deps += [x11_dep]
closebutton_sources = [cfgfile_1]
closebutton_sources += ['src/closebutton.vala']
closebutton_vala_args = []
closebutton_c_args = []
if ATHOME
  closebutton_vala_args += ['-D', 'ATHOME']
  closebutton_c_args += ['-DATHOME']
endif
closebutton_vala_args += ['--gir=gedit_closebutton-1.0.gir']


gedit_closebutton_library = shared_library('gedit_closebutton',closebutton_sources,dependencies: closebutton_deps,vala_args: closebutton_vala_args,c_args: closebutton_c_args,version: '1.0.0',soversion: '1',install: true)

closebutton_requires = []
closebutton_requires += ['atk']
closebutton_requires += ['cairo']
closebutton_requires += ['gdk-3.0']
closebutton_requires += ['gdk-pixbuf-2.0']
closebutton_requires += ['gedit']
closebutton_requires += ['gee-0.8']
closebutton_requires += ['gio-2.0']
closebutton_requires += ['glib-2.0']
closebutton_requires += ['gobject-2.0']
closebutton_requires += ['gobject-introspection-1.0']
closebutton_requires += ['gtk+-3.0']
closebutton_requires += ['gtksourceview-3.0']
closebutton_requires += ['libpeas-1.0']
closebutton_requires += ['pango']
closebutton_requires += ['x11']
pkg_mod = import('pkgconfig')
pkg_mod.generate(libraries : gedit_closebutton_library,
	version : '1.0.0',
	name : 'gedit_closebutton',
	filebase : 'gedit_closebutton',
	description : 'gedit_closebutton',
	requires : closebutton_requires)

install_data(join_paths(meson.current_source_dir(),'src/gedit_closebutton.deps'),install_dir: join_paths(get_option('prefix'),'share','vala','vapi'))
meson.add_install_script(join_paths(meson.current_source_dir(),'meson_scripts','install_library.sh'),'gedit_closebutton','gedit_closebutton-1.0.gir')

