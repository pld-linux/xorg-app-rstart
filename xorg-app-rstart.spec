Summary:	rstart application
Summary(pl):	Aplikacja rstart
Name:		xorg-app-rstart
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/rstart-%{version}.tar.bz2
# Source0-md5:	0026fc78b94f5596587b1f6e5ff10bc4
Patch0:		rstart-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rstart application.

%description -l pl
Aplikacja rstart.

%prep
%setup -q -n rstart-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/rstart/config
%attr(755,root,root) %{_libdir}/X11/rstart/rstartd.real
%{_mandir}/man1/*.1*
