Summary:	GObject introspection library
Name:		gobject-introspection
Version:	1.42.0
Release:	1
License:	LGPL v2+ (giscanner) and GPL v2+ (tools)
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gobject-introspection/1.42/%{name}-%{version}.tar.xz
# Source0-md5:	4fa52f6b67367d9c1b99b98683ced202
Patch0:		%{name}-libtool.patch
URL:		http://live.gnome.org/GObjectIntrospection
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cairo-gobject-devel
BuildRequires:	glib-gio-devel >= 1:2.42.0
BuildRequires:	libffi-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/girepository-1.0
%define		optcppflags	%{nil}

%description
GObject introspection library.

%package devel
Summary:	Header files for gobject-introspection library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gobject-introspection library.

%package apidocs
Summary:	GI API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GI API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gobject-introspection/giscanner/*.{la,py}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gobject-introspection/giscanner/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{_libdir}/girepository-1.0
%attr(755,root,root) %ghost %{_libdir}/libgirepository-1.0.so.?
%attr(755,root,root) %{_libdir}/libgirepository-1.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)

%dir %{_datadir}/gir-1.0
%dir %{_datadir}/gobject-introspection-1.0
%dir %{_libdir}/gobject-introspection
%dir %{_libdir}/gobject-introspection/giscanner
%dir %{_libdir}/gobject-introspection/giscanner/collections
%dir %{_libdir}/gobject-introspection/giscanner/doctemplates

%attr(755,root,root) %{_bindir}/g-ir-annotation-tool
%attr(755,root,root) %{_bindir}/g-ir-compiler
%attr(755,root,root) %{_bindir}/g-ir-generate
%attr(755,root,root) %{_bindir}/g-ir-scanner
%attr(755,root,root) %{_libdir}/lib*.so

%{_datadir}/gir-1.0/*.gir
%{_datadir}/gobject-introspection-1.0/*.c
%{_datadir}/gobject-introspection-1.0/Makefile.introspection
%{_datadir}/gobject-introspection-1.0/tests
%{_includedir}/gobject-introspection-1.0

%{_datadir}/aclocal/introspection.m4
%{_pkgconfigdir}/*.pc

%attr(755,root,root) %{_libdir}/gobject-introspection/giscanner/*.so
%{_libdir}/gobject-introspection/giscanner/*.py[co]
%{_libdir}/gobject-introspection/giscanner/collections/*.py[co]

%{_libdir}/gobject-introspection/giscanner/doctemplates/C
%{_libdir}/gobject-introspection/giscanner/doctemplates/Gjs
%{_libdir}/gobject-introspection/giscanner/doctemplates/Python
%{_libdir}/gobject-introspection/giscanner/doctemplates/*.tmpl

%{_mandir}/man1/g-ir-compiler.1*
%{_mandir}/man1/g-ir-generate.1*
%{_mandir}/man1/g-ir-scanner.1*

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gi
%endif

