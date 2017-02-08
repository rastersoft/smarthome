Name: smarthome
Version: 1.0.0
Release: 1
License: Unknown/not set
Summary: This is a plugin for GEdit 3 that enables the SmartHome mode. That means that the *HOME* key will move the cursor to the first non-space character in the line, and not to the first column. This is very useful when using Gedit as a code editor.

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: vala
BuildRequires: atk-devel
BuildRequires: gtk3-devel
BuildRequires: gedit-devel
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtksourceview3-devel
BuildRequires: libpeas-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: intltool

Requires: atk
Requires: glib2
Requires: gtk3
Requires: pango
Requires: gdk-pixbuf2
Requires: cairo-gobject
Requires: cairo
Requires: gtksourceview3
Requires: libpeas
Requires: gobject-introspection

%description
This is a plugin for GEdit 3 that enables the SmartHome mode. That
means that the *HOME* key will move the cursor to the first non-space
character in the line, and not to the first column. This is very
useful when using Gedit as a code editor.
.
The main advantage of this plugin over others, is that this has been
written in Vala, which compiles to native code and, thus, it is very lightweight.
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

