Summary:	Network extensions for GLib using OpenSSL
Summary(pl.UTF-8):	Rozszerzenia sieciowe biblioteki GLib wykorzystujące OpenSSL
Name:		glib-openssl
Version:	2.50.8
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glib-openssl/2.50/%{name}-%{version}.tar.xz
# Source0-md5:	db7ae779bbd45c2043186fdba08764b0
Patch0:		openssl.patch
URL:		https://github.com/GNOME/glib-openssl
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.19.4
BuildRequires:	glib2-devel >= 1:2.46.0
BuildRequires:	libtool >= 2:2
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.46.0
Suggests:	ca-certificates
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Network extensions for GLib using OpenSSL.

%description -l pl.UTF-8
Rozszerzenia sieciowe biblioteki GLib wykorzystujące OpenSSL.

%prep
%setup -q
%patch0 -p1

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--with-ca-certificates=/etc/certs/ca-certificates.crt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gio/modules/libgioopenssl.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/gio/modules/libgioopenssl.so
