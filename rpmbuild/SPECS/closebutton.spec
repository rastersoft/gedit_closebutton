Name: closebutton
Version: 1.0.0
Release: 1
License: Unknown/not set
Summary: This is a plugin for GEdit 3 that enables the Close Button when the left panel is visible and the user moved the close button to the left.

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: vala
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: gtk3-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: gedit-devel
BuildRequires: libgee-devel
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtksourceview3-devel
BuildRequires: libpeas-devel
BuildRequires: pango-devel
BuildRequires: libX11-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: intltool

Requires: atk
Requires: glib2
Requires: cairo
Requires: gtk3
Requires: pango
Requires: gdk-pixbuf2
Requires: cairo-gobject
Requires: gtksourceview3
Requires: libpeas
Requires: gobject-introspection
Requires: libgee
Requires: libX11

%description
This is a plugin for GEdit 3 that enables the Close Button when the
left panel is visible and the user moved the close button to the left.
.

%files
*

%build
mkdir -p ${RPM_BUILD_DIR}
cd ${RPM_BUILD_DIR}; cmake -DCMAKE_INSTALL_PREFIX=/usr -DGSETTINGS_COMPILE=OFF -DICON_UPDATE=OFF ../..
make -C ${RPM_BUILD_DIR}

%install
make install -C ${RPM_BUILD_DIR} DESTDIR=%{buildroot}

%post
ldconfig

%postun
ldconfig

%clean
rm -rf %{buildroot}

